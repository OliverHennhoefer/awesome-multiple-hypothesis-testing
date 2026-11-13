# Contributing

Recommend resources you have read or used and can explain. Breadth should come from covering distinct ideas, not accumulating near-duplicate papers.

## Selection Policy

Research entries normally require a published article in a refereed journal or a full paper in reviewed conference proceedings. An arXiv upload, DOI, institutional affiliation, workshop presentation, or acceptance claim alone does not establish peer review. Prefer the version of record once it exists; a repository-hosted accepted manuscript can be an additional access link.

Include foundational contributions, strong surveys, useful methodological advances, and reproducible comparisons that directly concern multiplicity. Consider both the contribution and its limitations. A famous author or prestigious venue is not sufficient by itself. Exclude generic single-hypothesis tutorials, routine applications of BH, marketing, unexplained link dumps, and papers whose central relevant result has been retracted.

The philosophy section may include scholarly perspectives and debate in the cited journals. Describe positions as arguments, not universal recommendations, and check the article's actual publication category and review policy when adding one.

Two exceptions are possible:

1. **Authoritative monographs.** Established specialist books by foundational contributors belong in the monograph section. Mark each with **Monograph.**, identify its publisher and year, and document the authors' relevant contributions in the exception register. Do not call a book a peer-reviewed journal article.
2. **Exceptional preprints or reports.** Include only a substantial, otherwise missing contribution by a demonstrably established authority in the relevant area. Give specific evidence of that author's foundational peer-reviewed work and a primary institutional or professional source supporting their standing. Institutional prestige, social-media popularity, citation counts alone, and coauthorship with a famous researcher are insufficient. State why a published alternative cannot fill the gap. Label the annotation **Not peer reviewed.**, identify the server and version date, and add a reason and evidence to the exception register. Replace it when a reviewed version appears.

The current register is [publication-exceptions.json](docs/publication-exceptions.json). Its keys are canonical publication URLs; DOI keys use lowercase identifiers. Unused exceptions fail validation. No expert-preprint exceptions are currently listed.

The register can also contain a `metadata-correction` for a publication year omitted or incorrectly deposited in Crossref. It requires the exact corrected year, a reason, and evidence from the publisher or an authoritative archive of the published article. This only resolves the recorded metadata discrepancy; all publication-status checks still apply.

## Verify the Publication

Before adding a reference:

- Open the publisher or proceedings record and check the title, authors, publication year, and venue. A reference list or search snippet is only a discovery aid.
- Check that the link is the intended paper, rather than a book review, correction notice, similarly titled article, or earlier preprint. Crossref sometimes has several such records.
- Check for corrections, expressions of concern, and retractions on the publisher page. Link relevant corrections and describe material limitations.
- Read the abstract and enough of the paper to support the annotation. Identify the error criterion, testing setting, assumptions, and whether the guarantee is finite-sample, asymptotic, or empirical.
- Use the issue year when available; use the online-publication year for an article that has not yet been assigned to an issue. Do not use the preprint year for the published paper.
- Prefer a clean HTTPS DOI link. For papers without an appropriate DOI, use the official journal or proceedings landing page, not a search result or an unstable PDF mirror.

DOI registration and a Crossref journal-article type are useful checks, but neither proves that a work was peer reviewed. The contributor and reviewer must establish that separately.

## Format and Placement

Edit the README directly. It is an annotated, manually maintained list rather than generated search results or a generated bibliography.

```markdown
- [Published Paper Title](https://example.org/article) - Author and Author (2024, *Journal Name*). Contribution, setting, and the important limitation or assumption.
```

Use surnames, preserving accents where possible. List up to four authors; use the first surname followed by “et al.” for longer author lists. Use a consistent short journal name where the full historical name is cumbersome. Preserve the paper's title apart from capitalization and readable mathematical typography.

Place a paper once, in the section that best explains its main contribution. Add method names such as BH, SAFFRON, or DAGGER to the annotation so they remain searchable. Keep the seminal section short; subsequent important papers belong in their methodological sections. Prefer chronological order within sections.

Descriptions start with a capital letter and end with a period. Explain why the resource is useful. Avoid unsupported claims such as “best,” “most powerful,” or “valid under any dependence” when the theorem has additional conditions. Distinguish FDR, marginal FDR, local FDR, FDX, FCR, and false sign rates.

Use the Contents list for section navigation and avoid redundant internal links elsewhere. Do not add CI, star-count, download-count, or coverage badges. Keep the official Awesome badge beside the title.

## Software and Research Code

Software entries link to official documentation or an official package registry, explain the implemented methods, and point to published methodological support. Documentation itself is not an exception to the research-paper rule: it is clearly categorized as an implementation resource.

Check that a package is available, documented, and maintained. Keep historical, archived, or inactive author code in [Research Code](docs/RESEARCH_CODE.md), with its associated published paper and a clear statement of its role. An old commit date alone does not prove that a mature package is unusable.

## Run the Checks

Use Node.js 22 or newer and Python 3.10 or newer.

```sh
npm ci --ignore-scripts
npm run check
npm run check:references
```

Install [Lychee](https://github.com/lycheeverse/lychee) 0.24.2 to run link checks locally:

```sh
npm run check:links:offline
npm run check:links
```

The first command checks local files and fragments without network access. The second checks non-DOI external links as well. The separate reference audit checks DOI registration and bibliographic metadata; publisher bot protection is not silently counted as success. See [Maintenance](docs/MAINTENANCE.md) for interpreting failures.

## Review Checklist

- The contribution fills a clear gap or improves an existing entry.
- Publication status and the version of record were checked at a primary source.
- The annotation accurately states the contribution and relevant assumptions.
- The entry is placed once and has consistent metadata.
- Any exception is labelled and supported by specific evidence.
- Documentation and software links were opened and checked.
- Applicable local, publication-metadata, and network checks pass, or a reproducible external failure is explained.

Contributions to this repository are made under its [CC0 dedication](LICENSE). Linked papers, books, and software retain their own rights and licenses.
