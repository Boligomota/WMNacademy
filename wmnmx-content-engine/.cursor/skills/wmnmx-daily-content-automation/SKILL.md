---
name: wmnmx-daily-content-automation
description: orchestrate the daily content automation for WMNMX, a private Facebook group for women 40+ in Mexico. Use this skill when generating daily verified-source research, Spanish editorial translation, Facebook-ready posts, visual briefs, quality scoring, and human-review packages for technology adoption, digital safety, AI, productivity, professional reinvention, and social commerce.
---

# WMNMX Daily Content Automation

## Mission

Operate as the editorial orchestration layer for WMNMX.

WMNMX is a private Facebook group for women 40+ in Mexico focused on technology adoption, digital confidence, AI literacy, productivity, professional reinvention, and social commerce.

The goal is not to publish more content. The goal is to build trust, autonomy, and practical digital advantage.

## Core operating principle

Use English for internal instructions, research prompts, and agent coordination.

Produce all final outputs in Spanish, using simple, clear, Mexican-context language. Keep key digital terms in English when they are part of real digital literacy, then explain them in Spanish.

Example:

- Keep: phishing, ghosting, prompt, deepfake, DM, scam, malware, bot, passkey.
- Explain in Spanish immediately after the term.

## Daily content formula

Generate exactly three daily content pieces:

1. Señal verificada
2. Explícamelo fácil
3. Reto de 10 minutos

Each piece must serve a different job:

- Inform
- Translate / explain
- Activate

Never produce three link posts.
Never publish directly to Facebook.
Always prepare for human review.

## Required workflow

1. Start daily run.
2. Use or invoke the three research agents:
   - wmnmx-digital-safety
   - wmnmx-ai-productivity
   - wmnmx-social-commerce
3. Collect findings from verified public sources only.
4. Reject weak, undated, paywalled, private, login-protected, or SEO-spam sources.
5. Translate and simplify useful findings into Spanish.
6. Create three Facebook-ready posts.
7. Create one visual brief per post.
8. Create sources used and sources rejected files.
9. Apply quality scoring.
10. Write editorial notes for human review.

## Required daily output

Create a dated folder:

`/content/daily/YYYY-MM-DD/`

Inside it, create:

1. `01_research-summary.md`
2. `02_posts-ready.md`
3. `03_visual-briefs.md`
4. `04_sources-used.json`
5. `05_sources-rejected.md`
6. `06_quality-score.md`
7. `07_editorial-notes.md`

## Source policy

Allowed:

- public pages
- RSS feeds
- official documentation
- official blogs
- government institutions
- universities
- reputable media
- platform help centers
- public security advisories
- public business and technology reports

Not allowed:

- private Facebook groups
- login-protected pages
- paywalls
- restricted sites
- mass scraping
- copied full articles
- undated content
- viral posts without primary source
- generic SEO blogs
- rumor-based content

## Editorial standard

Every post must include:

- clear hook
- simple explanation
- relevance for women 40+
- practical action
- easy question to activate comments
- verified source reference when applicable
- recommended publishing time
- visual brief

## Quality Gate

Score each post from 0 to 5 on:

- source trust
- clear date
- clarity
- immediate usefulness
- relevance for women 40+
- conversation potential

Minimum score to mark ready: 24/30.

If a post fails, rewrite it or mark it as not ready.

## Final rule

Automation saves time. It does not replace editorial judgment.

The final package must be ready for human review, not direct publishing.
