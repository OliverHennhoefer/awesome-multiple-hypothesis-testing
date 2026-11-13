import unittest

from scripts.check_references import (
    Reference, canonical_url, check_catalog, check_metadata, normalize,
    doi_links, publication_years, read_references,
)


def reference(**changes):
    fields = dict(
        line=3, section="Seminal Papers",
        title="Controlling the False Discovery Rate",
        url="https://doi.org/10.1234/example", authors="Benjamini and Hochberg",
        year=1995, venue="Journal of Statistics", note="Introduces an FDR procedure.",
    )
    fields.update(changes)
    return Reference(**fields)


def record(**changes):
    fields = dict(
        DOI="10.1234/example", title=["Controlling the False Discovery Rate"],
        author=[{"family": "Benjamini"}], type="journal-article",
        **{"published-print": {"date-parts": [[1995]]},
           "container-title": ["Journal of Statistics"]},
    )
    fields.update(changes)
    return fields


class ReferenceTests(unittest.TestCase):
    def test_parses_doi_with_parentheses_and_secondary_link(self):
        text = (
            "## Reviews\n"
            "- [Paper](https://doi.org/10.1016/S0123(00)001-2) - Smith "
            "(2000, *Journal*). See the [correction](https://doi.org/10.1234/correction).\n"
        )
        refs, errors = read_references(text)
        self.assertEqual(errors, [])
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].doi, "10.1016/s0123(00)001-2")

    def test_ignores_contents_and_software(self):
        text = (
            "## Contents\n- [Reviews](#reviews)\n## Reviews\n"
            "- [Paper](https://doi.org/10.1234/a) - Smith (2000, *Journal*). Useful.\n"
            "## Software\n### Python\n- [Tool](https://example.org) - Implementation.\n"
        )
        refs, errors = read_references(text)
        self.assertEqual(len(refs), 1)
        self.assertEqual(errors, [])

    def test_missing_metadata_and_empty_catalog_fail(self):
        _, errors = read_references("## Reviews\n- [Paper](https://example.org) - Useful.")
        self.assertTrue(any("authors, year" in error for error in errors))
        self.assertTrue(any("no research" in error for error in errors))

    def test_duplicate_case_and_encoded_dois_fail(self):
        refs = [reference(), reference(line=4, title="Another title", url="https://doi.org/10.1234%2FEXAMPLE")]
        self.assertTrue(any("duplicate reference URL" in e for e in check_catalog(refs, {})))

    def test_duplicate_titles_fail_even_with_different_identifiers(self):
        refs = [reference(), reference(line=4, url="https://doi.org/10.1234/another")]
        self.assertTrue(any("duplicate title" in e for e in check_catalog(refs, {})))

    def test_future_year_fails(self):
        errors = check_catalog([reference(year=2030)], {}, current_year=2026)
        self.assertTrue(any("future" in e for e in errors))

    def test_unlabelled_monograph_fails(self):
        ref = reference(section="Authoritative Monographs")
        errors = check_catalog([ref], {})
        self.assertTrue(any("explicit exception" in e for e in errors))
        self.assertTrue(any("visibly labelled" in e for e in errors))

    def test_preprint_needs_evidence_and_visible_label(self):
        ref = reference(url="https://arxiv.org/abs/1234.5678", venue="Preprint")
        self.assertTrue(any("expert exception" in e for e in check_catalog([ref], {})))
        exceptions = {ref.url: {"kind": "expert-preprint", "reason": "Foundational author", "evidence": ["https://example.org/publication"]}}
        self.assertTrue(any("visibly labelled" in e for e in check_catalog([ref], exceptions)))
        ref = reference(url=ref.url, venue="Preprint", note="**Not peer reviewed.** Contribution.")
        self.assertEqual(check_catalog([ref], exceptions), [])

    def test_stale_exceptions_fail(self):
        errors = check_catalog([reference()], {"https://example.org/unused": {}})
        self.assertTrue(any("unused" in e for e in errors))

    def test_exception_evidence_must_be_https_urls(self):
        ref = reference()
        for evidence in ([], "https://example.org", ["not a URL"], ["http://example.org"], [None]):
            with self.subTest(evidence=evidence):
                errors = check_catalog([ref], {
                    ref.url: {"kind": "metadata-correction", "year": ref.year,
                              "reason": "Publisher-confirmed year", "evidence": evidence},
                })
                self.assertTrue(any("evidence must" in e for e in errors))

    def test_metadata_matches(self):
        self.assertEqual(check_metadata(reference(), record()), [])

    def test_wrong_paper_at_live_doi_fails(self):
        errors = check_metadata(reference(), record(title=["A different paper about another subject"]))
        self.assertTrue(any("title does not match" in e for e in errors))

    def test_preprint_metadata_is_not_journal_evidence(self):
        self.assertTrue(any("publication type" in e for e in check_metadata(reference(), record(type="posted-content"))))
        errors = check_metadata(reference(), record(**{"container-title": ["SSRN Electronic Journal"]}))
        self.assertTrue(any("report deposit" in e for e in errors))

    def test_wrong_year_or_author_fails(self):
        errors = check_metadata(reference(year=1996, authors="Someone Else"), record())
        self.assertTrue(any("year" in e for e in errors))
        self.assertTrue(any("author" in e for e in errors))

    def test_online_and_issue_years_are_accepted(self):
        metadata = record(**{
            "published-online": {"date-parts": [[1994]]},
            "journal-issue": {"published-print": {"date-parts": [[1996]]}},
        })
        self.assertEqual(publication_years(metadata), {1994, 1995, 1996})

    def test_normalizes_publisher_math_and_unicode(self):
        self.assertEqual(normalize("<i>α</i>-Investing"), normalize("Alpha-Investing"))
        self.assertEqual(normalize("Šidák"), normalize("Sidak"))

    def test_book_review_is_not_book_exception(self):
        errors = check_metadata(reference(), record(), {"kind": "monograph"})
        self.assertTrue(any("expected a book" in e for e in errors))

    def test_other_url_paths_remain_case_sensitive(self):
        self.assertNotEqual(canonical_url("https://example.org/A"), canonical_url("https://example.org/a"))

    def test_extracts_secondary_doi_links_and_parentheses(self):
        text = "[Paper](https://doi.org/10.1016/A(00)001) and [correction](https://doi.org/10.1234/B)."
        self.assertEqual(doi_links(text), {"10.1016/a(00)001", "10.1234/b"})

    def test_documented_year_correction_is_narrow(self):
        exception = {"kind": "metadata-correction", "year": 1996}
        self.assertEqual(check_metadata(reference(year=1996), record(), exception), [])
        errors = check_metadata(reference(year=1997), record(), exception)
        self.assertTrue(any("year" in e for e in errors))

    def test_metadata_correction_does_not_bypass_publication_type(self):
        errors = check_metadata(reference(year=1996), record(type="posted-content"),
                                {"kind": "metadata-correction", "year": 1996})
        self.assertTrue(any("publication type" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
