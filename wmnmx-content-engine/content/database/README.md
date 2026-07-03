# Local Editorial Database

This folder stores lightweight editorial memory before moving to Supabase, Airtable, or another database.

It helps the automation avoid repetition and make better recommendations over time.

Recommended files:

```txt
content/database/
  signals.jsonl
  used-topics.jsonl
  rejected-signals.jsonl
  published-posts.jsonl
  audience-questions.jsonl
```

## signals.jsonl

One JSON object per candidate signal considered by the system.

Recommended fields:

```json
{
  "date": "YYYY-MM-DD",
  "signal_id": "",
  "topic": "",
  "source_url": "",
  "decision": "used / backup / rejected",
  "decision_reason": "",
  "novelty_score": 0,
  "audience_fit": 0
}
```

## used-topics.jsonl

Track topic repetition.

```json
{
  "date": "YYYY-MM-DD",
  "topic": "",
  "angle": "",
  "content_mode": "",
  "post_title": ""
}
```

## published-posts.jsonl

Update this manually after publishing.

```json
{
  "published_date": "YYYY-MM-DD",
  "post_title": "",
  "content_mode": "",
  "topic": "",
  "source_url": "",
  "facebook_post_url": "",
  "performance_notes": "",
  "comments_summary": ""
}
```

## audience-questions.jsonl

Store repeated questions or needs from the group without personal information.

```json
{
  "date": "YYYY-MM-DD",
  "question_summary": "",
  "topic": "",
  "frequency": "low / medium / high",
  "privacy_check": "no personal data"
}
```

## Rule

This folder is operational memory, not private data storage. Do not store member names, screenshots, private comments, phone numbers, emails, or personal details.
