Test the WMNMX Daily Content Automation without scheduling.

Use the current repository and generate a sample daily package for tomorrow.

Do not publish.
Do not connect to Facebook.
Do not use private or restricted sources.
Do not scrape private Facebook groups, login-protected pages, paywalls, or restricted pages.

Before researching freely, read:

- `sources/allowlist.yml`
- `sources/rss-feeds.yml`
- `sources/api-sources.yml`
- `sources/manual-intake.yml`
- `sources/rejected-sources.yml`
- `content/inbox/` if it contains sample signals
- `content/audience-insights/` if it contains audience notes
- `content/database/` if it contains previous topics or posts

Use the project skills and subagents if available.

Create the output under:

`/content/daily/test-run-YYYY-MM-DD/`

Generate:

1. `00_signals-ranked.json`
2. `01_research-summary.md`
3. `02_posts-ready.md`
4. `03_visual-briefs.md`
5. `04_sources-used.json`
6. `05_sources-rejected.md`
7. `06_quality-score.md`
8. `07_editorial-notes.md`

The test should show:

- at least 3 candidate signals ranked before writing
- one primary editorial recommendation
- one or two backup ideas only if they are strong enough
- novelty score and audience fit for each ready post
- rejected sources or rejected signals when applicable
- final output in Spanish
- simple Mexican-context language for women 40+
- important digital terms in English when useful, explained immediately in Spanish

Quality threshold:

- 32/40 or more: ready for human review
- 24-31: backup or revise
- 23 or less: reject
