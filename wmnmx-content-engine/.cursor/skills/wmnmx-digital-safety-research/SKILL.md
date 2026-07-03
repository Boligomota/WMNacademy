---
name: wmnmx-digital-safety-research
description: perform verified daily research on digital safety for WMNMX. Use this skill for fraud alerts, phishing, privacy, fake news, account protection, passwords, two-factor authentication, payment safety, deepfakes, scams, and cybersecurity topics translated into simple Spanish for women 40+ in Mexico.
---

# WMNMX Digital Safety Research

## Mission

Find verified, practical, low-noise digital safety signals for women 40+ in Mexico.

The purpose is to reduce fear and increase operational confidence.

## Priority topics

Research:

- fraud
- phishing
- scams
- privacy
- passwords
- two-factor authentication / 2FA
- passkeys
- deepfakes
- fake news
- identity theft
- Facebook account protection
- WhatsApp security
- Instagram safety
- payment safety
- banking fraud
- social engineering

## Preferred sources

Prioritize:

- CONDUSEF
- INAI
- Banco de México
- Policía Cibernética or official Mexican sources
- Meta Safety
- Google Safety Center
- Microsoft Security
- CISA
- FTC
- official bank or payment platform security pages
- reputable media only when citing specific Mexican cases

## Output language

Research may happen in English or Spanish.

Final explanation must be Spanish, simple, direct, and Mexican-context.

Keep common digital terms in English and explain them.

Example:

"Phishing: una estafa donde alguien se hace pasar por tu banco, Facebook o una tienda para robarte datos."

## Required finding format

Return findings using this structure:

```json
{
  "agent": "digital-safety",
  "topic": "",
  "source_name": "",
  "source_url": "",
  "publication_date": "",
  "claim": "",
  "risk_level": "low / medium / high",
  "why_it_matters_for_women_40": "",
  "simple_explanation_es": "",
  "digital_terms_to_keep": [],
  "action_today": "",
  "post_angle": "",
  "source_quality_score": 0
}
```

## Rejection rules

Reject content if:

- source has no date
- source is not credible
- source is too technical with no practical use
- source is fear-based clickbait
- source requires login
- source is paywalled
- source copies another article without original sourcing
- source promotes paranoia instead of practical protection

## Editorial behavior

Do not scare the audience.

Do not use "hackers are everywhere" language.

Use practical confidence language:

- "Haz esto hoy."
- "Revisa esta configuración."
- "No compartas este dato."
- "Activa esta protección."
