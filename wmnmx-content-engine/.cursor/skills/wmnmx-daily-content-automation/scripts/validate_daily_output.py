#!/usr/bin/env python3
"""Validate WMNMX daily automation output.

Usage:
  python3 .cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py --latest
  python3 .cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py --folder content/daily/2026-06-30

This script is intentionally conservative. It validates structure and produces a human-readable report.
It does not publish, edit creatively, or connect to Facebook.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from datetime import datetime

REQUIRED_FILES = [
    "00_signals-ranked.json",
    "01_research-summary.md",
    "02_posts-ready.md",
    "03_visual-briefs.md",
    "04_sources-used.json",
    "05_sources-rejected.md",
    "06_quality-score.md",
    "07_editorial-notes.md",
]

CONTENT_MODES = [
    "señal verificada", "senal verificada", "explícamelo fácil", "explicamelo facil",
    "reto de 10 minutos", "alerta práctica", "alerta practica", "mito vs realidad",
    "checklist guardable", "caso aplicado", "pregunta detonadora", "mini clase",
]
REQUIRED_POST_FIELDS = ["hook", "explicación", "explicacion", "por qué", "por que", "acción", "accion", "pregunta"]
SPANISH_MARKERS = ["para", "mujeres", "acción", "pregunta", "fuente", "explicación", "esto", "hoy"]
DIGITAL_TERMS = [
    "phishing", "ghosting", "love bombing", "DM", "prompt", "deepfake", "2FA", "passkey",
    "malware", "scam", "bot", "chatbot", "workflow", "no-code", "low-code",
    "social commerce", "e-commerce", "marketplace", "lead", "checkout", "link-in-bio"
]
PROHIBITED_SOURCE_HINTS = [
    "paywall", "login", "private facebook", "grupo privado", "seo blog", "rumor",
    "content farm", "contenido privado", "sin fuente"
]


def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "content" / "daily").exists() or (candidate / ".cursor").exists():
            return candidate
    return current


def latest_daily_folder(root: Path) -> Path | None:
    daily = root / "content" / "daily"
    if not daily.exists():
        return None
    folders = [p for p in daily.iterdir() if p.is_dir()]
    if not folders:
        return None
    folders.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return folders[0]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def load_json_array(path: Path, label: str) -> tuple[list[dict], list[str]]:
    if not path.exists():
        return [], [f"{label} missing"]
    try:
        data = json.loads(read(path))
    except Exception as e:
        return [], [f"{label} is not valid JSON: {e}"]
    if not isinstance(data, list):
        return [], [f"{label} must be a JSON array"]
    return data, []


def validate_ranked_signals(path: Path) -> list[str]:
    data, issues = load_json_array(path, "00_signals-ranked.json")
    if issues:
        return issues
    if not data:
        issues.append("00_signals-ranked.json is empty")
    required = ["topic", "source_name", "summary", "audience_fit", "novelty_score", "decision", "decision_reason"]
    use_or_backup = 0
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            issues.append(f"Signal item {idx} is not an object")
            continue
        for key in required:
            if item.get(key) in (None, ""):
                issues.append(f"Signal item {idx} missing {key}")
        if item.get("decision") in {"use", "backup"}:
            use_or_backup += 1
        for score_key in ["audience_fit", "novelty_score"]:
            try:
                score = int(item.get(score_key, -1))
            except Exception:
                issues.append(f"Signal item {idx} has invalid {score_key}")
                continue
            if score < 0 or score > 5:
                issues.append(f"Signal item {idx} {score_key} must be 0-5")
    if use_or_backup == 0:
        issues.append("No usable or backup signals were selected")
    return issues


def validate_sources_json(path: Path) -> list[str]:
    data, issues = load_json_array(path, "04_sources-used.json")
    if issues:
        return issues
    if not data:
        issues.append("04_sources-used.json is empty")
    required = ["source_name", "source_type", "claim_used", "trust_reason"]
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            issues.append(f"Source item {idx} is not an object")
            continue
        for key in required:
            if not item.get(key):
                issues.append(f"Source item {idx} missing {key}")
        if not item.get("source_url") and item.get("source_type") != "manual-intake":
            issues.append(f"Source item {idx} missing source_url")
        joined = " ".join(str(v).lower() for v in item.values())
        if any(hint in joined for hint in PROHIBITED_SOURCE_HINTS):
            issues.append(f"Source item {idx} may violate source policy")
    return issues


def validate_posts(text: str) -> list[str]:
    issues = []
    lower = text.lower()
    if not any(mode in lower for mode in CONTENT_MODES):
        issues.append("No recognized content mode detected in posts-ready")
    for field in REQUIRED_POST_FIELDS:
        if field.lower() not in lower:
            issues.append(f"Posts may be missing required field: {field}")
    spanish_hits = sum(1 for marker in SPANISH_MARKERS if marker.lower() in lower)
    if spanish_hits < 4:
        issues.append("Output may not be sufficiently Spanish or community-facing")
    for term in DIGITAL_TERMS:
        if term.lower() in lower:
            pattern = re.compile(rf"{re.escape(term)}[^\n]{{0,160}}(:|significa|es |sirve|se refiere|una |un )", re.I)
            if not pattern.search(text):
                issues.append(f"Digital term appears without simple explanation: {term}")
    return issues


def score_quality_text(text: str) -> list[str]:
    issues = []
    totals = [int(x) for x in re.findall(r"(?:total|score|puntaje)[^0-9]{0,20}(\d{1,2})\s*/\s*40", text, flags=re.I)]
    if not totals:
        totals = [int(x) for x in re.findall(r"(\d{1,2})\s*/\s*40", text)]
    low = [x for x in totals if x < 32]
    if low:
        issues.append(f"Quality scores below 32/40 found: {low}")
    if not totals:
        issues.append("No quality totals were detected. Add scores in 0-40 format.")
    lower = text.lower()
    if "novelty" not in lower and "novedad" not in lower:
        issues.append("Quality score should include novelty score")
    if "audience" not in lower and "audiencia" not in lower:
        issues.append("Quality score should include audience fit")
    return issues


def validate_editorial_notes(text: str) -> list[str]:
    issues = []
    lower = text.lower()
    expected = ["repet", "audiencia", "editor", "fuente"]
    for marker in expected:
        if marker not in lower:
            issues.append(f"Editorial notes may be missing marker: {marker}")
    return issues


def write_report(folder: Path, issues: list[str]) -> None:
    status = "PASS" if not issues else "REVIEW NEEDED"
    now = datetime.now().isoformat(timespec="seconds")
    lines = [
        "# WMNMX Hook Validation",
        "",
        f"**Status:** {status}",
        f"**Validated at:** {now}",
        f"**Folder:** `{folder}`",
        "",
    ]
    if issues:
        lines.append("## Issues")
        lines.append("")
        for issue in issues:
            lines.append(f"- {issue}")
    else:
        lines.append("No structural issues detected. Ready for human review.")
    lines.append("")
    lines.append("## Reminder")
    lines.append("")
    lines.append("This validation does not replace editorial judgment. A human editor must review before scheduling on Facebook.")
    (folder / "08_hook-validation.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true", help="Validate latest folder under content/daily")
    parser.add_argument("--folder", type=str, help="Specific daily output folder")
    args = parser.parse_args()

    root = find_project_root(Path.cwd())
    if args.folder:
        folder = (root / args.folder).resolve() if not Path(args.folder).is_absolute() else Path(args.folder).resolve()
    elif args.latest:
        folder = latest_daily_folder(root)
        if folder is None:
            print("No daily output folder found.")
            return 1
    else:
        parser.error("Use --latest or --folder")

    issues: list[str] = []
    for filename in REQUIRED_FILES:
        if not (folder / filename).exists():
            issues.append(f"Missing required file: {filename}")

    issues.extend(validate_ranked_signals(folder / "00_signals-ranked.json"))

    posts_text = read(folder / "02_posts-ready.md")
    if posts_text:
        issues.extend(validate_posts(posts_text))

    quality_text = read(folder / "06_quality-score.md")
    if quality_text:
        issues.extend(score_quality_text(quality_text))

    notes_text = read(folder / "07_editorial-notes.md")
    if notes_text:
        issues.extend(validate_editorial_notes(notes_text))

    issues.extend(validate_sources_json(folder / "04_sources-used.json"))

    write_report(folder, issues)

    if issues:
        print(f"Validation completed with {len(issues)} issue(s). See {folder / '08_hook-validation.md'}")
        return 1
    print(f"Validation passed. See {folder / '08_hook-validation.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
