# Instalacion paso a paso en Cursor

Esta guia monta la version mejorada de WMNMX Content Engine: una redaccion editorial automatizada basada en fuentes permitidas, bandeja de senales, novelty score, feedback del grupo y revision humana.

## 1. Abrir el repo

Abre `wmnmx-content-engine` como workspace en Cursor.

No abras una subcarpeta. La raiz debe mostrar:

```txt
.cursor/
content/
docs/
logs/
prompts/
sources/
templates/
README.md
```

## 2. Confirmar Rules, Skills y Subagents

Ve a:

```txt
Settings -> Rules, Skills, Subagents
```

Confirma que existan:

### Rules

- `wmnmx-editorial-voice`
- `wmnmx-source-policy`
- `wmnmx-translation-policy`

### Skills

- `wmnmx-daily-content-automation`
- `wmnmx-digital-safety-research`
- `wmnmx-ai-productivity-research`
- `wmnmx-social-commerce-research`

### Subagents

- `wmnmx-source-discovery`
- `wmnmx-digital-safety`
- `wmnmx-ai-productivity`
- `wmnmx-social-commerce`
- `wmnmx-editorial-critic`

## 3. Revisar fuentes antes de automatizar

Antes de crear la Automation, abre y ajusta:

```txt
sources/allowlist.yml
sources/rejected-sources.yml
sources/rss-feeds.yml
sources/api-sources.yml
sources/manual-intake.yml
```

Regla practica:

```txt
RSS/API primero.
Busqueda web solo para verificar o completar.
Scraping puntual solo si la pagina es publica y no hay mejor alternativa.
Nada de grupos privados, login, paywalls o contenido restringido.
```

## 4. Preparar contexto del grupo sin scraping

Abre:

```txt
content/audience-insights/weekly-notes-template.md
```

Cada semana, llena una copia con:

- preguntas frecuentes del grupo;
- dudas repetidas;
- temas que generaron conversacion;
- miedos o fricciones;
- temas que conviene pausar.

No copies comentarios privados. Resume patrones.

## 5. Preparar la bandeja de senales

La Automation puede buscar por si sola, pero es mejor si existe una bandeja previa:

```txt
content/inbox/YYYY-MM-DD/
  rss-signals.json
  api-signals.json
  manual-signals.md
```

En fase 1 puedes llenar esto manualmente.
En fase 2 puedes usar n8n para poblarlo desde RSS/APIs.

## 6. Ajustar Tools & MCPs

Recomendado fase 1:

- Web Search Tool: ON
- Web Fetch Tool: ON
- Chrome DevTools MCP: ON solo para verificacion puntual
- context7: ON
- sequential-thinking: ON

Mantener fuera del flujo inicial:

- meta-mcp: OFF
- mercadopago-mcp-server: OFF
- supabase: OFF o sin dependencia critica
- vercel: OFF

## 7. Crear Automation

Ve a:

```txt
Automations -> New Automation
```

Configura:

```txt
Active: OFF al inicio
Repository: wmnmx-content-engine
Trigger: Scheduled
Time: 6:00 am CDMX
Agent Instructions: pegar prompts/automation-master.md
```

No conectar Facebook.
No activar publicacion directa.

## 8. Agregar Memories

Despues de guardar la Automation, agrega las Memories de:

```txt
prompts/memories.md
```

No metas toda la estrategia en Memories. Las Memories son solo contexto estable.

## 9. Test manual

Antes de activar, corre:

```txt
prompts/test-run.md
```

Debe crear:

```txt
content/daily/test-run-YYYY-MM-DD/
  00_signals-ranked.json
  01_research-summary.md
  02_posts-ready.md
  03_visual-briefs.md
  04_sources-used.json
  05_sources-rejected.md
  06_quality-score.md
  07_editorial-notes.md
```

## 10. Revisar el test

Revisa:

- hay al menos 3 senales candidatas rankeadas;
- hay una recomendacion editorial principal;
- no se forzaron 3 posts si no habia calidad suficiente;
- cada fuente tiene URL, fecha o access date, tipo y razon de confianza;
- el post principal tiene novelty score y audience fit;
- el contenido esta en espanol claro para mujeres +40 en Mexico;
- no hay miedo barato, tono condescendiente ni lenguaje de guru;
- no se uso contenido privado.

## 11. Activar Automation

Solo activar cuando el test sea util y consistente:

```txt
Automations -> WMNMX Daily Content Automation -> Active ON
```

Flujo recomendado:

```txt
06:00 Automation corre
06:45 paquete diario listo
08:00 humana revisa
09:00 equipo agenda manualmente en Facebook
```

## 12. Operacion diaria

Cada manana abre:

```txt
content/daily/YYYY-MM-DD/
```

Revisa especialmente:

- `00_signals-ranked.json`
- `02_posts-ready.md`
- `04_sources-used.json`
- `06_quality-score.md`
- `07_editorial-notes.md`

Despues de publicar manualmente, actualiza si puedes:

```txt
content/database/published-posts.jsonl
content/database/used-topics.jsonl
```

## 13. Fase 2: n8n para ingestion

Cuando el proceso manual funcione, usa n8n para:

- leer RSS feeds;
- consultar APIs publicas;
- guardar senales en `content/inbox/`;
- enviar notificaciones internas;
- no redactar ni publicar.

## 14. Fase 3: Hooks

Despues de 7 a 14 dias de outputs estables, activa hooks.

El validador debe revisar:

- existen los 8 archivos diarios;
- `00_signals-ranked.json` es valido;
- hay novelty score;
- hay audience fit;
- las fuentes cumplen politica;
- los scores usan escala 40;
- los terminos digitales estan explicados;
- el contenido esta listo para revision humana.

## 15. Fase 4: Base externa

Solo cuando ya tengas historial suficiente, considera:

- Supabase;
- Airtable;
- Notion;
- dashboard editorial.

No lo vuelvas dependencia critica antes de validar el flujo editorial.

## 16. Regla final

El MVP correcto no es publicar mas rapido.

El MVP correcto es:

```txt
mejores senales
-> menos repeticion
-> mas contexto real del grupo
-> contenido mas util
-> revision humana
-> publicacion con intencion
```
