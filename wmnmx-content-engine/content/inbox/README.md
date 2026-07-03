# Content Inbox

This folder stores candidate signals before Cursor turns them into editorial content.

Use this folder to avoid starting every daily run from a blank web search.

Recommended structure:

```txt
content/inbox/YYYY-MM-DD/
  rss-signals.json
  api-signals.json
  manual-signals.md
```

## Signal fields

Each signal should include:

```json
{
  "signal_id": "YYYY-MM-DD-001",
  "source_channel": "rss / api / manual / web-search",
  "topic": "",
  "source_name": "",
  "source_url": "",
  "publication_date": "",
  "captured_at": "",
  "summary": "",
  "why_it_might_matter": "",
  "initial_category": "digital-safety / ai-productivity / social-commerce / reinvention / other",
  "privacy_check": "public / permitted / needs-review",
  "notes": ""
}
```

## Rules

- Inbox signals are candidates, not approved sources.
- Cursor must still verify source quality before using them.
- Manual notes from the private Facebook group must be summaries only.
- Do not store names, screenshots, private messages, or personal data.
- Prefer RSS/API ingestion in phase 2 through n8n or another scheduler.
