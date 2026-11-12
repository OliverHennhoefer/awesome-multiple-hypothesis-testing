# Maintenance

The README is the authoritative reading map. The automation checks its formatting and references; it does not select papers or regenerate the list.

## Validation Layers

| Check | Command | Purpose |
| --- | --- | --- |
| Official Awesome lint and Markdown lint | `npm run lint` | Badge placement, title, Contents, list style, contribution file, license, and Markdown structure. |
| Bibliography integrity and checker regression tests | `npm test` | Required author/year/venue annotations, duplicate titles and identifiers, valid exception records, and tests of failure cases. |
| Publisher-deposited DOI metadata | `npm run check:references` | Crossref registration, title, first author, publication year, and publication type for research references; registration of additional supporting DOI links. |
| Local links and anchors | `npm run check:links:offline` | Missing files and broken section links without accessing the network. |
| External links | `npm run check:links` | Reachability of non-DOI documentation, journals, proceedings, repositories, and exception evidence, including URLs in the JSON register. |

The quality workflow runs on pushes to main, pull requests, and manual dispatch. The network workflow also runs every Monday. Action revisions and npm dependencies are pinned; Dependabot proposes monthly updates. Workflow permissions are read-only, checkout does not persist credentials, and no workflow opens issues or posts comments.

Use the unmodified [official Awesome badge](https://github.com/sindresorhus/awesome/blob/main/awesome.md#awesome-badge). The [upstream guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) explicitly prohibit CI badges, so CI exists without adding one to the README.

## Interpreting Link Failures

DOI links are excluded only from Lychee because academic publishers commonly challenge automated requests after DOI redirection. They are checked separately through Crossref. This verifies the identifier and deposited citation, not browser access to the publisher's full text. Open DOI destinations manually when adding or reviewing a paper.

Do not globally accept 403, 429, timeouts, or server errors as successful checks. A 403 can be bot protection; a 429 can be rate limiting. Retry later, inspect the page in a browser, and use a stable official landing page if needed. A permanent exclusion needs a specific URL, a reason, and an alternative verification path. Avoid domain-wide exclusions.

A successful HTTP response can still be a soft 404, a login page, an unrelated article, or a package removal notice. Read the returned page when assessing a failed or suspicious reference. Conversely, a publisher blocking automation is not evidence that its paper has disappeared.

The optional local cache is for iterating within one audit:

```sh
python3 scripts/check_references.py --online --cache-dir /tmp/mht-doi-audit
```

CI does not use a persistent metadata cache. Run without the cache for a fresh audit. Crossref failures remain failures; the checker does not silently fall back to unverified metadata.

A published issue year can differ from Crossref's online-only date. Record a narrowly scoped `metadata-correction` in [publication-exceptions.json](publication-exceptions.json), with the exact year and evidence from the publisher or an authoritative archive of the published article. The checker reports applied corrections and still validates the title, author, and publication type. Never use a year correction to exempt a preprint from the selection policy.

## Manual Scientific Review

Check these items when adding a paper and during periodic maintenance:

- Verify the venue's review process and the actual publication category. A DOI or bibliographic database record is not a peer-review certificate.
- Follow corrections and retractions at the publisher. Automated metadata checks are not a complete retraction-monitoring service.
- Confirm that each annotation matches the theorem's assumptions and the error criterion it actually controls.
- Check whether an expert preprint has a published replacement.
- Reassess whether software is available and maintained, moving historical implementations to the separate research-code file when appropriate.
- Review coverage by methodological topic, including recent work. Avoid adding many small variations merely to increase the item count.
- Check book editions and issue years against the publisher when database metadata are inconsistent.

The original list's duplicated Benjamini–Yekutieli citation, mismatched onlineFDR bibliography, incorrect batching year, misspellings, and SAFFRON repository link were corrected during the expansion. Unverified lecture slides, standalone talks, and the unverified HAL/workshop references were replaced with published sources. Long formula transcriptions were removed in favor of concise annotations pointing to the original definitions and proofs.

## Awesome Compatibility and Editorial Responsibility

Follow the [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md), [creation guide](https://github.com/sindresorhus/awesome/blob/main/create-list.md), and current list requirements. Their standard is curation of resources a contributor can personally recommend, not exhaustive inclusion of everything published.

Formatting compliance does not establish eligibility for the upstream index. The upstream guidelines also require human curation and disallow AI-generated lists. An AI-assisted expansion therefore requires substantive human editorial review; passing the linters cannot certify compliance with that requirement or guarantee upstream acceptance.

Repository topics and any upstream submission are separate repository-management steps. Recommended topics include `awesome`, `awesome-list`, `multiple-testing`, `multiple-hypothesis-testing`, `false-discovery-rate`, and `statistics`.
