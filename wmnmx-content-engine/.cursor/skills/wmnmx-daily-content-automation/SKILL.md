---
name: wmnmx-daily-content-automation
description: orchestrate the daily content automation for WMNMX, a private Facebook group for women 40+ in Mexico. Use this skill when generating verified-source research, ranked content signals, novelty scoring, Spanish editorial translation, Facebook-ready posts, visual briefs, quality scoring, and human-review packages.
---

# WMNMX Daily Content Automation

## Mission

Operate as the editorial orchestration layer for WMNMX.

WMNMX is a private Facebook group for women 40+ in Mexico focused on technology adoption, digital confidence, AI literacy, productivity, professional reinvention, and social commerce.

The goal is not to publish more content. The goal is to build trust, autonomy, and practical digital advantage.

## Core operating principle

Cursor should not behave like a daily free-form search bot.

Cursor should behave like an editorial desk:

```txt
source intake
-> signal ranking
-> verification
-> deduplication
-> novelty scoring
-> audience fit
-> editorial production
-> human review
```

Use English for internal instructions, research prompts, and agent coordination when useful.

Produce all final outputs in Spanish, using simple, clear, Mexican-context language. Keep key digital terms in English when they are part of real digital literacy, then explain them in Spanish.

## Required workflow

1. Start daily run.
2. Read repository source files:
   - `sources/allowlist.yml`
   - `sources/rss-feeds.yml`
   - `sources/api-sources.yml`
   - `sources/manual-intake.yml`
   - `sources/rejected-sources.yml`
3. Check `content/inbox/` for existing signals.
4. Check `content/audience-insights/` for recent audience questions and repeated needs.
5. Check `content/database/` for previously used topics, sources, rejections, and published posts.
6. Invoke or use the three topic research agents when useful:
   - wmnmx-digital-safety
   - wmnmx-ai-productivity
   - wmnmx-social-commerce
7. Use web search/fetch only to verify, complete, or replace signals.
8. Reject weak, undated, paywalled, private, login-protected, or SEO-spam sources.
9. Rank all candidate signals before writing.
10. Calculate novelty score and audience fit.
11. Select one primary recommendation and up to two backup ideas.
12. Create Facebook-ready content only for signals that pass the quality threshold.
13. Create visual briefs.
14. Create sources used and sources rejected files.
15. Apply quality scoring.
16. Write editorial notes for human review.

## Source policy

Allowed:

- public pages
- RSS feeds
- public APIs
- official documentation
- official blogs
- government institutions
- universities
- reputable media
- platform help centers
- public security advisories
- public business and technology reports
- manual links provided by the team when public or permitted

Not allowed:

- private Facebook groups
- login-protected pages
- paywalls
- restricted sites
- mass scraping
- copied full articles
- undated content for current topics
- viral posts without primary source
- generic SEO blogs
- rumor-based content
- content farms
- affiliate-heavy listicles

## Content modes

Choose the mode that best fits the signal:

1. Señal verificada
2. Explícamelo fácil
3. Reto de 10 minutos
4. Alerta práctica
5. Mito vs realidad
6. Checklist guardable
7. Caso aplicado
8. Pregunta detonadora
9. Mini clase

Do not force three posts every day. One excellent post is better than three generic posts.

## Required daily output

Create a dated folder:

`/content/daily/YYYY-MM-DD/`

Inside it, create:

1. `00_signals-ranked.json`
2. `01_research-summary.md`
3. `02_posts-ready.md`
4. `03_visual-briefs.md`
5. `04_sources-used.json`
6. `05_sources-rejected.md`
7. `06_quality-score.md`
8. `07_editorial-notes.md`

## Signal ranking standard

Every signal in `00_signals-ranked.json` must include:

- signal_id
- topic
- source_name
- source_url
- source_type
- publication_date or access_date
- summary
- audience_fit
- novelty_score
- urgency
- recommended_content_mode
- decision: use / backup / reject
- decision_reason

## Editorial standard

Every ready post must include:

- clear hook
- simple explanation
- relevance for women 40+ in Mexico
- practical action
- easy question to activate comments
- verified source reference when applicable
- recommended publishing time
- visual brief
- editor check before publishing

## Quality Gate

Score each post from 0 to 5 on:

- source trust
- clear date
- clarity
- immediate usefulness
- relevance for women 40+
- conversation potential
- novelty score
- audience fit

Minimum score to mark ready: 32/40.

Status rules:

- 32/40 or more: ready for human review.
- 24-31: revise or keep as backup.
- 23 or less: reject.

Auto-reject if:

- source is not trustworthy
- source has no date and topic requires recency
- content is fear-based
- content is too technical without a beginner path
- content has no practical action
- content sounds like guru marketing
- topic was recently used without a new angle

## Final rule

Automation saves time. It does not replace editorial judgment.

The final package must be ready for human review, not direct publishing.
