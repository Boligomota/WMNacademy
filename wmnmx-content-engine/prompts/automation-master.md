Run the WMNMX Daily Content Automation.

Repository:
Use the selected repository as the persistent content engine.

Project context:
WMNMX is a private Facebook group for women 40+ in Mexico focused on technology adoption, digital safety, AI, productivity, professional reinvention, and social commerce.

Core goal:
Produce a daily editorial package that helps the community gain digital confidence, practical autonomy, and competitive advantage.

Important:
This automation must not publish to Facebook.
This automation must not connect to Facebook.
This automation must not scrape private Facebook groups, login-protected pages, paywalls, or restricted sources.
Prepare content for human review and manual scheduling only.

Operating model:
Do not depend only on free-form daily search.
Start from the repository context:

1. Read `sources/allowlist.yml`, `sources/rss-feeds.yml`, `sources/api-sources.yml`, and `sources/manual-intake.yml`.
2. Check `content/inbox/` for existing signals.
3. Check `content/audience-insights/` for recent questions, objections, repeated doubts, or high-engagement themes from the group.
4. Check `content/database/` for previously used topics, posts, sources, and rejected signals.
5. Use web search/fetch only to complete missing context, verify recency, or replace weak sources.

Use the project skills:
- wmnmx-daily-content-automation
- wmnmx-digital-safety-research
- wmnmx-ai-productivity-research
- wmnmx-social-commerce-research

Use the project subagents when useful:
- wmnmx-digital-safety
- wmnmx-ai-productivity
- wmnmx-social-commerce

Research mode:
Monitor verified public sources only.

Preferred source order:
1. RSS feeds and public APIs from the repository source files.
2. Official documentation, official blogs, platform help centers, government institutions, universities, public reports, and security advisories.
3. Reputable media only when they point to or summarize primary sources.
4. Public pages with clear date and low extraction risk.

Allowed:
- public pages
- RSS feeds
- public APIs
- official documentation
- official blogs
- government institutions
- universities
- public security advisories
- reputable media
- platform help centers
- public business and technology reports
- manual links provided by the team when they are public or have permission to be used

Not allowed:
- private Facebook groups
- login-protected pages
- paywalled content
- restricted pages
- mass scraping
- copied full articles
- undated content for current topics
- rumor-based content
- viral posts without primary source
- generic SEO blogs
- content farms
- affiliate-heavy listicles

Language:
Use English for internal reasoning, research coordination, and source analysis when useful.
Final outputs must be in Spanish.
Use clear, simple, Mexican-context language.
Do not sound condescending.
Do not use fear as clickbait.
Do not use guru marketing language.

Translation rule:
Keep key digital terms in English when they are important for digital literacy, then explain them in simple Spanish.
Examples: phishing, ghosting, love bombing, DM, prompt, deepfake, 2FA, passkey, malware, scam, bot, chatbot, workflow, no-code, low-code, social commerce, e-commerce, marketplace, lead, checkout.

Editorial selection:
Rank signals before writing.
Choose one primary editorial recommendation for the day.
Create backup ideas only if they are strong enough.
Do not force three posts if the signal quality does not justify it.

Daily content formula:
The daily package should include at least one strong Facebook-ready post and, when useful, one or two backup ideas.
Choose the best content mode for each signal:

- Señal verificada
- Explícamelo fácil
- Reto de 10 minutos
- Alerta práctica
- Mito vs realidad
- Checklist guardable
- Caso aplicado
- Pregunta detonadora
- Mini clase

Required output folder:
Create a folder under:

`/content/daily/YYYY-MM-DD/`

Required files:

1. `00_signals-ranked.json`
2. `01_research-summary.md`
3. `02_posts-ready.md`
4. `03_visual-briefs.md`
5. `04_sources-used.json`
6. `05_sources-rejected.md`
7. `06_quality-score.md`
8. `07_editorial-notes.md`

Each item in `00_signals-ranked.json` must include:
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

Each Facebook-ready post must include:
- title
- content mode
- hook
- simple explanation
- why it matters for women 40+ in Mexico
- practical action
- easy question to activate comments
- source reference when applicable
- recommended publishing time
- visual brief
- editor check before publishing

Quality gate:
Score each post from 0 to 5 on:
- source trust
- clear date
- clarity
- immediate usefulness
- relevance for women 40+
- conversation potential
- novelty score
- audience fit

Minimum score:
32/40.

If a post scores 24-31, mark it as backup or revise.
If a post scores below 24, reject it.

Editorial note:
At the end, include what a human editor should check before scheduling, especially:
- whether the source is still current
- whether the topic was recently repeated
- whether the post responds to a real audience need
- whether the action is safe and realistic
