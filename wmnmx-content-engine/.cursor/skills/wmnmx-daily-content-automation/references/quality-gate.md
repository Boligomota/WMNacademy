# Quality Gate

Every ready post is scored out of 40.

| Criterion | Score |
|---|---:|
| Source trust | 0-5 |
| Clear date | 0-5 |
| Clarity | 0-5 |
| Immediate usefulness | 0-5 |
| Relevance for women 40+ | 0-5 |
| Conversation potential | 0-5 |
| Novelty score | 0-5 |
| Audience fit | 0-5 |

## Status

- 32/40 or more: ready for human review.
- 24-31: revise or keep as backup.
- 23 or less: reject.

## Novelty score guidance

Score novelty by comparing the signal against:

- `content/database/published-posts.jsonl`
- `content/database/used-topics.jsonl`
- recent files in `content/daily/`
- recent audience notes in `content/audience-insights/`

Use this scale:

- 5: new topic or clearly new angle.
- 4: familiar topic with timely update or practical new use.
- 3: useful but similar to recent content.
- 2: repeated with weak new angle.
- 1: almost duplicate.
- 0: duplicate or unnecessary repetition.

## Audience fit guidance

Score audience fit by asking:

- Does this help women 40+ in Mexico act with more autonomy?
- Is it practical for beginners or intermediate users?
- Does it connect to safety, productivity, reinvention, AI literacy, or social commerce?
- Can the action be completed without an agency, developer, or paid tool?
- Does it respond to a real question, fear, goal, or friction from the group?

## Auto-reject

Reject if:

- source is not trustworthy
- source has no date and topic requires recency
- content is fear-based
- content is too technical with no beginner path
- content has no 10-minute action or practical next step
- content sounds like guru marketing
- topic was recently published without a meaningfully new angle
- the value is only a link, not a translation or action
