# Plan completo WMNMX + Cursor Automation

Esta es la version interna del plan para `wmnmx-content-engine`. La version principal tambien esta documentada en la raiz del repositorio como `Plan_Completo_WMNMX_Cursor_Automation.md`.

## Veredicto estrategico

La automatizacion debe construirse en Cursor, pero no como scraper ni autoposter. Debe operar como una redaccion editorial automatizada con criterio.

Arquitectura recomendada:

```txt
RSS / APIs / aportes manuales / busqueda controlada
-> content/inbox/
-> verificacion de fuentes
-> deduplicacion y novelty score
-> ajuste con feedback real del grupo
-> produccion editorial en Cursor
-> revision humana
-> publicacion manual en Facebook
```

## Componentes principales

- Rules: tono, fuentes y traduccion.
- Skills: workflows reutilizables.
- Subagents por etapa: source discovery y editorial critic.
- Subagents por tema: seguridad digital, IA/productividad y social commerce.
- Signal Inbox: senales previas a redaccion.
- Local Editorial Database: historial ligero antes de Supabase.
- Audience Insights: resumenes seguros del grupo, sin scraping privado.
- Quality Gate: 40 puntos, incluyendo novelty score y audience fit.
- Human Review: ultima decision antes de publicar.

## Estructura recomendada

```txt
wmnmx-content-engine/
  .cursor/
    rules/
    skills/
    agents/
    hooks.json
  sources/
    allowlist.yml
    rejected-sources.yml
    rss-feeds.yml
    api-sources.yml
    manual-intake.yml
  prompts/
    automation-master.md
    test-run.md
    memories.md
  templates/
    senal-verificada.md
    explicamelo-facil.md
    reto-10-minutos.md
    visual-brief.md
    content-modes.md
  content/
    inbox/
    daily/
    approved/
    published/
    database/
    audience-insights/
  logs/
    automation-runs.md
```

## Flujo diario

```txt
06:00  Automation inicia
06:01  Lee Rules, Skills, Memories y audience-insights
06:03  Lee content/inbox/ y sources/
06:08  Completa investigacion con web search/fetch si hace falta
06:15  Verifica fuentes y rechaza senales debiles
06:20  Deduplica contra content/database/
06:25  Calcula novelty score y audience fit
06:30  Selecciona 1 senal principal y hasta 2 backups
06:35  Produce post(s), visual brief y notas editoriales
06:40  Aplica Quality Gate
06:45  Escribe archivos diarios
08:00  Humano revisa
09:00  Equipo agenda manualmente en Facebook
```

## Output diario

```txt
content/daily/YYYY-MM-DD/
  00_signals-ranked.json
  01_research-summary.md
  02_posts-ready.md
  03_visual-briefs.md
  04_sources-used.json
  05_sources-rejected.md
  06_quality-score.md
  07_editorial-notes.md
```

Fase 2:

```txt
content/daily/YYYY-MM-DD/08_hook-validation.md
```

## Quality Gate

Cada pieza se evalua sobre 40 puntos:

- Source trust: 0-5
- Clear date: 0-5
- Clarity: 0-5
- Immediate usefulness: 0-5
- Relevance women 40+: 0-5
- Conversation potential: 0-5
- Novelty score: 0-5
- Audience fit: 0-5

Criterio:

- 32/40 o mas: listo para revision humana.
- 24-31: revisar o convertir en backup.
- 23 o menos: descartar.

## Fases

### Fase 1 - Cursor mejorado

- Ajustar fuentes.
- Usar inbox manual si hace falta.
- Registrar audience insights semanales.
- Generar paquetes con senales rankeadas.

### Fase 2 - n8n para ingestion

- Leer RSS.
- Consultar APIs publicas.
- Guardar senales en `content/inbox/`.
- No redactar ni publicar.

### Fase 3 - Hooks

- Validar estructura.
- Validar score de 40 puntos.
- Validar novelty y audience fit.
- Generar `08_hook-validation.md`.

### Fase 4 - Base externa

- Supabase, Airtable, Notion o dashboard solo cuando haya datos suficientes.

### Fase 5 - Meta/Facebook

Solo despues de output estable, permisos claros, politica anti-spam y revision de riesgos. No usar scraping privado.

## Decision final

La mejor ruta es:

```txt
n8n/RSS/API para ingestion
+
Cursor para criterio editorial
+
revision humana antes de publicar
```

El objetivo no es hacer mas ruido. El objetivo es detectar mejores senales, traducirlas con criterio y aprender de la comunidad.
