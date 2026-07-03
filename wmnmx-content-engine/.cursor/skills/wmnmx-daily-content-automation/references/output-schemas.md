# Output Schemas

## 00_signals-ranked.json

```json
[
  {
    "signal_id": "YYYY-MM-DD-001",
    "topic": "",
    "source_name": "",
    "source_url": "",
    "source_type": "rss / api / official / institutional / university / media / platform-doc / public-report / manual-intake",
    "publication_date": "",
    "access_date": "",
    "summary": "",
    "why_it_matters_for_wmnmx": "",
    "audience_fit": 0,
    "novelty_score": 0,
    "urgency": "low / medium / high",
    "recommended_content_mode": "senal-verificada / explicamelo-facil / reto-10-minutos / alerta-practica / mito-vs-realidad / checklist-guardable / caso-aplicado / pregunta-detonadora / mini-clase",
    "decision": "use / backup / reject",
    "decision_reason": ""
  }
]
```

## 04_sources-used.json

```json
[
  {
    "source_name": "",
    "source_url": "",
    "source_type": "rss / api / official / institutional / university / media / platform-doc / public-report / manual-intake",
    "publication_date": "",
    "access_date": "",
    "claim_used": "",
    "trust_reason": "",
    "used_for_post": "primary / backup / visual-brief / research-context",
    "source_quality_score": 0
  }
]
```

## 06_quality-score.md item

```json
{
  "post_title": "",
  "content_mode": "",
  "source_trust": 0,
  "clear_date": 0,
  "clarity": 0,
  "immediate_usefulness": 0,
  "relevance_women_40": 0,
  "conversation_potential": 0,
  "novelty_score": 0,
  "audience_fit": 0,
  "total": 0,
  "status": "ready / backup / revise / reject",
  "reason": ""
}
```

## 07_editorial-notes.md required checks

Include:

- primary recommendation for the day
- backup ideas and why they were not primary
- repeated topic risk
- audience insight used, if any
- source concerns
- what the human editor must verify before scheduling
- suggested manual update to `content/database/` after publishing
