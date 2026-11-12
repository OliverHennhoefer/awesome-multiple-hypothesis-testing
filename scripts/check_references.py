#!/usr/bin/env python3
"""Check the README bibliography; optionally verify publisher-deposited DOI metadata."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date
from difflib import SequenceMatcher
import hashlib
import html
import json
from pathlib import Path
import re
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
NON_RESEARCH = {"Contents", "Orientation", "Software", "Related Lists", "Contributing"}
ENTRY = re.compile(
    r"^- \[(?P<title>.+?)\]\((?P<url>\S+)\) - "
    r"(?P<authors>.+?) \((?P<year>\d{4}), \*(?P<venue>[^*]+)\*\)\. (?P<note>.+)$"
)
PREPRINT_HOSTS = {"arxiv.org", "biorxiv.org", "medrxiv.org", "ssrn.com", "hal.science"}


@dataclass(frozen=True)
class Reference:
    line: int
    section: str
    title: str
    url: str
    authors: str
    year: int
    venue: str
    note: str

    @property
    def doi(self):
        parts = urlsplit(self.url)
        return unquote(parts.path.lstrip("/")).lower() if parts.hostname == "doi.org" else None


def normalize(text):
    """Ignore typography, XML markup, accents, and a few common mathematical forms."""
    text = html.unescape(re.sub(r"<[^>]*>", "", text))
    text = text.replace("α", "alpha").replace(r"\alpha", "alpha")
    text = re.sub(r"\\(?:rm|mathrm|text|sb|sp)\b", "", text)
    text = unicodedata.normalize("NFKD", text).casefold()
    return "".join(c for c in text if c.isalnum())


def canonical_url(url):
    parts = urlsplit(url)
    # DOI identifiers are case-insensitive. Other URL paths need not be.
    if parts.hostname in {"doi.org", "dx.doi.org"}:
        return "https://doi.org/" + unquote(parts.path.lstrip("/")).lower()
    return url.rstrip("/")


def doi_links(markdown):
    """Extract DOI targets, including secondary citation links with parentheses."""
    return {
        unquote(urlsplit(url).path.lstrip("/")).lower()
        for url in re.findall(r"\]\((https://doi\.org/\S+)\)", markdown)
    }


def read_references(markdown):
    references, errors = [], []
    section = None
    for line_number, line in enumerate(markdown.splitlines(), 1):
        if line.startswith("## "):
            section = line[3:]
        if not section or section in NON_RESEARCH or not line.startswith("- "):
            continue
        match = ENTRY.fullmatch(line)
        if not match:
            errors.append(f"line {line_number}: expected title, URL, authors, year, venue, and annotation")
            continue
        fields = match.groupdict()
        fields["year"] = int(fields["year"])
        references.append(Reference(line_number, section, **fields))
    if not references:
        errors.append("no research references found")
    return references, errors


def check_catalog(references, exceptions, current_year=None):
    errors, urls, titles, used_exceptions = [], {}, {}, set()
    current_year = current_year or date.today().year
    for ref in references:
        where = f"line {ref.line}"
        key = canonical_url(ref.url)
        title = normalize(ref.title)
        if key in urls:
            errors.append(f"{where}: duplicate reference URL (first on line {urls[key]})")
        if title in titles:
            errors.append(f"{where}: duplicate title (first on line {titles[title]})")
        urls[key], titles[title] = ref.line, ref.line
        parts = urlsplit(ref.url)
        if parts.scheme != "https" or not parts.hostname:
            errors.append(f"{where}: use an absolute HTTPS publication URL")
        if not 1800 <= ref.year <= current_year:
            errors.append(f"{where}: invalid or future publication year {ref.year}")
        if not ref.note.endswith("."):
            errors.append(f"{where}: annotation must end with a period")
        if ref.doi and (parts.query or parts.fragment):
            errors.append(f"{where}: use a clean DOI URL without query or fragment")
        exception = exceptions.get(key)
        is_preprint = any(
            parts.hostname == host or (parts.hostname or "").endswith("." + host)
            for host in PREPRINT_HOSTS
        )
        if ref.section == "Authoritative Monographs":
            if not exception or exception.get("kind") != "monograph":
                errors.append(f"{where}: monograph requires an explicit exception")
            if "**Monograph.**" not in ref.note:
                errors.append(f"{where}: monograph must be visibly labelled")
        elif is_preprint or re.search(r"\b(preprint|working paper|technical report)\b", ref.venue, re.I):
            if not exception or exception.get("kind") != "expert-preprint":
                errors.append(f"{where}: unpublished work requires a documented expert exception")
        if exception:
            used_exceptions.add(key)
            evidence = exception.get("evidence")
            if not isinstance(exception.get("reason"), str) or not exception["reason"].strip():
                errors.append(f"{where}: exception needs a reason and primary-source evidence")
            if not isinstance(evidence, list) or not evidence or any(
                not isinstance(url, str) or urlsplit(url).scheme != "https" or not urlsplit(url).hostname
                for url in evidence
            ):
                errors.append(f"{where}: exception evidence must be a nonempty list of HTTPS URLs")
            if exception.get("kind") not in {"monograph", "expert-preprint", "metadata-correction"}:
                errors.append(f"{where}: unknown exception kind")
            if exception.get("kind") == "monograph" and ref.section != "Authoritative Monographs":
                errors.append(f"{where}: put monographs in the labelled monograph section")
            if exception.get("kind") == "metadata-correction" and exception.get("year") != ref.year:
                errors.append(f"{where}: metadata correction must match the cited year")
            if exception.get("kind") == "expert-preprint" and "**Not peer reviewed.**" not in ref.note:
                errors.append(f"{where}: preprint exception must be visibly labelled as not peer reviewed")
    for key in exceptions.keys() - used_exceptions:
        errors.append(f"unused publication exception: {key}")
    return errors


def publication_years(record):
    years = set()
    for field in ("published", "published-print", "published-online", "issued"):
        for part in record.get(field, {}).get("date-parts", []):
            if part:
                years.add(part[0])
    issue = record.get("journal-issue", {})
    for field in ("published-print", "published-online"):
        for part in issue.get(field, {}).get("date-parts", []):
            if part:
                years.add(part[0])
    return years


def check_metadata(ref, record, exception=None):
    """These checks detect metadata mistakes; they cannot establish peer review."""
    errors = []
    if record.get("DOI", "").lower() != ref.doi:
        errors.append("Crossref returned a different DOI")
    expected = normalize(ref.title)
    candidates = []
    for title in record.get("title", []):
        candidates.append(normalize(title))
        for subtitle in record.get("subtitle", []):
            candidates.append(normalize(title + " " + subtitle))
    # Some deposits omit a subtitle (for example Efron's 2004 paper).
    title_matches = any(
        SequenceMatcher(None, expected, actual).ratio() >= 0.88
        or (len(actual) >= 35 and expected.startswith(actual))
        for actual in candidates
    )
    if not title_matches:
        errors.append("title does not match DOI metadata: " + " / ".join(record.get("title", [])))
    years = publication_years(record)
    corrected_year = (
        exception.get("year") if exception and exception.get("kind") == "metadata-correction"
        else None
    )
    if ref.year not in years and ref.year != corrected_year:
        errors.append(f"year {ref.year} does not match deposited publication years {sorted(years)}")
    authors = record.get("author", [])
    if authors:
        first = normalize(authors[0].get("family", authors[0].get("name", "")))
        if first and first not in normalize(ref.authors):
            errors.append("first author does not match DOI metadata")
    kind = record.get("type")
    if exception and exception["kind"] == "monograph":
        if kind not in {"book", "monograph", "edited-book"}:
            errors.append(f"expected a book, found Crossref type {kind!r}")
    elif not exception or exception["kind"] != "expert-preprint":
        venues = " ".join(record.get("container-title", []))
        if kind not in {"journal-article", "proceedings-article"}:
            errors.append(f"unapproved publication type {kind!r}")
        if re.search(r"SSRN|Research Report|arXiv|bioRxiv|medRxiv", venues, re.I):
            errors.append("repository/report deposit needs an explicit exception")
    if record.get("update-to"):
        for update in record["update-to"]:
            if update.get("type") in {"retraction", "withdrawal"}:
                errors.append("record is a retraction or withdrawal notice; review the source")
    return errors


def fetch_metadata(doi, cache_dir=None):
    path = None
    if cache_dir:
        path = cache_dir / (hashlib.sha256(doi.encode()).hexdigest() + ".json")
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    request = Request(
        "https://api.crossref.org/works/" + quote(doi, safe=""),
        headers={
            "User-Agent": "AwesomeMultipleHypothesisTesting/1.0 "
            "(https://github.com/OliverHennhoefer/awesome-multiple-hypothesis-testing)",
            "Accept": "application/json",
        },
    )
    for attempt in range(4):
        try:
            time.sleep(1)
            with urlopen(request, timeout=30) as response:
                record = json.load(response)["message"]
            if path:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
            return record
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
        except (URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("metadata request exhausted retries")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="also check Crossref metadata")
    parser.add_argument("--cache-dir", type=Path, help="optional temporary metadata cache for a local audit")
    args = parser.parse_args()
    references, errors = read_references((ROOT / "README.md").read_text(encoding="utf-8"))
    exceptions = json.loads((ROOT / "docs/publication-exceptions.json").read_text(encoding="utf-8"))
    errors.extend(check_catalog(references, exceptions))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Bibliography: {len(references)} unique references; format and exceptions valid.", flush=True)
    if args.online:
        doi_references = [ref for ref in references if ref.doi]
        markdown_files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
        markdown_files += list((ROOT / "docs").glob("*.md"))
        markdown_files += list((ROOT / ".github").glob("*.md"))
        all_dois = set().union(*(
            doi_links(path.read_text(encoding="utf-8")) for path in markdown_files
        ))
        all_dois.update(
            unquote(urlsplit(url).path.lstrip("/")).lower()
            for exception in exceptions.values() for url in exception["evidence"]
            if urlsplit(url).hostname == "doi.org"
        )
        extra_dois = sorted(all_dois - {ref.doi for ref in doi_references})

        def verify(ref):
            try:
                record = fetch_metadata(ref.doi, args.cache_dir)
                return [f"line {ref.line}: {error}" for error in check_metadata(
                    ref, record, exceptions.get(canonical_url(ref.url))
                )]
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as error:
                return [f"line {ref.line}: could not verify {ref.doi}: {error}"]

        with ThreadPoolExecutor(max_workers=2) as pool:
            for issues in pool.map(verify, doi_references):
                errors.extend(issues)
                for issue in issues:
                    print(issue, flush=True)
        for doi in extra_dois:
            try:
                record = fetch_metadata(doi, args.cache_dir)
                if record.get("DOI", "").lower() != doi:
                    errors.append(f"secondary citation {doi}: returned a different DOI")
                    print(errors[-1], flush=True)
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as error:
                errors.append(f"secondary citation {doi}: could not verify: {error}")
                print(errors[-1], flush=True)
        print(
            f"Crossref: checked {len(doi_references)} reference records and "
            f"{len(extra_dois)} additional DOI links; {len(errors)} issues."
        )
        corrections = sum(item.get("kind") == "metadata-correction" for item in exceptions.values())
        if corrections:
            print(f"Applied {corrections} documented publisher-metadata correction(s).")
        print("Non-DOI publications and peer-review status require manual source review.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
