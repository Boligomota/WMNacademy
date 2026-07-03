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
Prepare content for human review and manual scheduling only.

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

Allowed:
- public pages
- RSS feeds
- official documentation
- official blogs
- government institutions
- universities
- public security advisories
- reputable media
- platform help centers
- public business and technology reports

Not allowed:
- private Facebook groups
- login-protected pages
- paywalled content
- restricted pages
- mass scraping
- copied full articles
- undated content
- rumor-based content
- viral posts without primary source
- generic SEO blogs

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

Daily content formula:
Create exactly 3 Facebook-ready posts:

1. Señal verificada
Purpose: inform.
Use one verified source or update.
Explain what happened, why it matters for women 40+, what risk or opportunity it opens, and what to do today.

2. Explícamelo fácil
Purpose: translate and simplify.
Turn a digital topic into a simple explanation, mini-guide, carousel idea, or visual brief.

3. Reto de 10 minutos
Purpose: activate.
Create one practical action the community can complete in 10 minutes or less.

Required output folder:
Create a folder under:

/content/daily/YYYY-MM-DD/

Required files:

1. 01_research-summary.md
2. 02_posts-ready.md
3. 03_visual-briefs.md
4. 04_sources-used.json
5. 05_sources-rejected.md
6. 06_quality-score.md
7. 07_editorial-notes.md

Each Facebook-ready post must include:
- title
- post type
- hook
- simple explanation
- why it matters for women 40+
- practical action
- easy question to activate comments
- source reference when applicable
- recommended publishing time
- visual brief

Quality gate:
Score each post from 0 to 5 on:
- source trust
- clear date
- clarity
- immediate usefulness
- relevance for women 40+
- conversation potential

Minimum score:
24/30.

If a post scores below 24, revise it or mark it as not ready.

Editorial note:
At the end, include what a human editor should check before scheduling.
