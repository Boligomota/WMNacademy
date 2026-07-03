# Guia paso a paso - Desarrollo de la automatizacion WMNMX en Cursor

## 0. Que estas montando

Vas a montar un sistema editorial automatizado para **WMNMX**, un grupo privado de Facebook para mujeres +40 en Mexico enfocado en:

- adopcion tecnologica;
- seguridad digital;
- IA;
- productividad;
- reinvencion profesional;
- social commerce;
- autonomia digital.

La version actualizada no funciona como autoposter ni como scraper. Funciona como una **redaccion editorial automatizada con criterio**.

La logica del sistema es:

```txt
fuentes permitidas
-> bandeja de senales
-> verificacion
-> deduplicacion
-> novelty score
-> feedback real del grupo
-> traduccion digital clara
-> contenido util
-> revision humana
-> publicacion manual en Facebook
```

Cursor no va a publicar automaticamente en Facebook en fase 1.
Cursor va a preparar contenido para revision humana.

## 1. Estructura actualizada del paquete

Carpeta principal:

```txt
wmnmx-content-engine/
```

Estructura esperada:

```txt
wmnmx-content-engine/

  .cursor/
    rules/
      wmnmx-editorial-voice.mdc
      wmnmx-source-policy.mdc
      wmnmx-translation-policy.mdc

    skills/
      wmnmx-daily-content-automation/
        SKILL.md
        references/
          editorial-system.md
          source-policy.md
          output-schemas.md
          translation-glossary.md
          quality-gate.md
        scripts/
          validate_daily_output.py

      wmnmx-digital-safety-research/
      wmnmx-ai-productivity-research/
      wmnmx-social-commerce-research/

    agents/
      wmnmx-source-discovery.md
      wmnmx-digital-safety.md
      wmnmx-ai-productivity.md
      wmnmx-social-commerce.md
      wmnmx-editorial-critic.md

    hooks.json
    hooks.example.json
    mcp.recommendations.md

  sources/
    allowlist.yml
    rejected-sources.yml
    rss-feeds.yml
    api-sources.yml
    manual-intake.yml

  templates/
    senal-verificada.md
    explicamelo-facil.md
    reto-10-minutos.md
    visual-brief.md
    content-modes.md

  prompts/
    automation-master.md
    test-run.md
    memories.md

  content/
    inbox/
    daily/
    approved/
    published/
    database/
    audience-insights/

  docs/
    INSTALL_CURSOR_STEP_BY_STEP.md
    PLAN_COMPLETO_WMNMX_CURSOR_AUTOMATION.md

  logs/
    automation-runs.md

  README.md
```

## 2. Que hace cada bloque

### `.cursor/rules/`

Controla comportamiento persistente:

- voz editorial;
- politica de fuentes;
- traduccion y glosario digital.

La rule mas importante para esta version es `wmnmx-source-policy.mdc`, porque ahora define el orden correcto:

```txt
RSS/API primero
manual intake permitido
web search solo para verificar o completar
scraping puntual solo en paginas publicas
nunca grupos privados, login, paywalls o contenido restringido
```

### `.cursor/skills/`

Contiene los workflows reutilizables.

La skill madre `wmnmx-daily-content-automation` ahora debe:

- leer fuentes configuradas;
- revisar `content/inbox/`;
- revisar feedback del grupo;
- revisar historial local;
- rankear senales;
- calcular novelty score y audience fit;
- seleccionar una recomendacion principal;
- generar backups solo si valen la pena;
- preparar contenido para revision humana.

### `.cursor/agents/`

Hay dos tipos de agentes:

Agentes por etapa:

- `wmnmx-source-discovery`: descubre y rankea senales antes de redactar.
- `wmnmx-editorial-critic`: revisa si el contenido realmente merece publicarse.

Agentes por tema:

- `wmnmx-digital-safety`
- `wmnmx-ai-productivity`
- `wmnmx-social-commerce`

### `sources/`

Define de donde puede venir la informacion.

Archivos clave:

- `allowlist.yml`: fuentes confiables por categoria.
- `rejected-sources.yml`: patrones prohibidos.
- `rss-feeds.yml`: feeds RSS recomendados.
- `api-sources.yml`: APIs publicas para descubrimiento.
- `manual-intake.yml`: reglas para aportes manuales del equipo.

### `content/inbox/`

Bandeja de senales antes de redactar.

Ejemplo futuro:

```txt
content/inbox/YYYY-MM-DD/
  rss-signals.json
  api-signals.json
  manual-signals.md
```

### `content/database/`

Base editorial local antes de usar Supabase.

Sirve para guardar:

- senales consideradas;
- temas usados;
- posts publicados;
- senales rechazadas;
- preguntas frecuentes.

Esto evita repeticion.

### `content/audience-insights/`

Aqui se guarda feedback real del grupo sin scrapear Facebook.

Usa `weekly-notes-template.md` para resumir:

- preguntas frecuentes;
- miedos;
- dudas;
- temas que generaron conversacion;
- temas que conviene pausar.

No copies comentarios privados. Resume patrones.

## 3. Paso 1 - Abrir el repo en Cursor

En Cursor:

```txt
File -> Open Folder
```

Selecciona:

```txt
wmnmx-content-engine/
```

Importante: abre la carpeta raiz, no una subcarpeta.

## 4. Paso 2 - Confirmar Rules, Skills y Subagents

Ve a:

```txt
Settings -> Rules, Skills, Subagents
```

Deben aparecer:

Rules:

```txt
wmnmx-editorial-voice
wmnmx-source-policy
wmnmx-translation-policy
```

Skills:

```txt
wmnmx-daily-content-automation
wmnmx-digital-safety-research
wmnmx-ai-productivity-research
wmnmx-social-commerce-research
```

Subagents:

```txt
wmnmx-source-discovery
wmnmx-digital-safety
wmnmx-ai-productivity
wmnmx-social-commerce
wmnmx-editorial-critic
```

Si no aparecen, revisa que esten en:

```txt
.cursor/rules/
.cursor/skills/
.cursor/agents/
```

## 5. Paso 3 - Revisar fuentes antes de activar

Abre:

```txt
sources/allowlist.yml
sources/rejected-sources.yml
sources/rss-feeds.yml
sources/api-sources.yml
sources/manual-intake.yml
```

Ajusta las fuentes segun lo que realmente quieres monitorear.

Regla practica:

```txt
70% RSS/APIs
20% busqueda web controlada
10% scraping puntual de paginas publicas
0% scraping de grupos privados
```

## 6. Paso 4 - Preparar feedback del grupo

Antes del primer test, llena una copia de:

```txt
content/audience-insights/weekly-notes-template.md
```

Puedes crear, por ejemplo:

```txt
content/audience-insights/2026-07-week-1.md
```

Incluye solo resumenes seguros:

- que preguntan mucho;
- que les da miedo;
- que no entienden;
- que tema genero comentarios;
- que quieren aprender.

No incluyas nombres, capturas, mensajes privados ni datos personales.

## 7. Paso 5 - Preparar bandeja de senales opcional

Para el primer test puedes dejar `content/inbox/` vacio.

Pero la mejor practica es crear:

```txt
content/inbox/test-run/manual-signals.md
```

Con 3 a 5 enlaces o senales candidatas.

Formato recomendado:

```txt
- Fecha:
- Fuente:
- URL publica:
- Resumen de la senal:
- Por que podria importar a WMNMX:
- Categoria:
- Privacy check:
```

## 8. Paso 6 - Configurar Tools & MCPs

Ve a:

```txt
Settings -> Tools & MCPs
```

Fase 1:

```txt
Web Search Tool: ON
Web Fetch Tool: ON
Chrome DevTools MCP: ON, solo verificacion puntual
context7: ON
sequential-thinking: ON
```

Mantener fuera al inicio:

```txt
meta-mcp: OFF
mercadopago-mcp-server: OFF
supabase: OFF o sin dependencia critica
vercel: OFF
```

## 9. Paso 7 - Crear Automation diaria

En Cursor:

```txt
Automations -> New Automation
```

Configura:

```txt
Active: OFF al inicio
Repository: wmnmx-content-engine
Trigger: Scheduled
Horario sugerido: 6:00 am CDMX
```

No dejes `No Repository`, porque Cursor necesita escribir en `content/daily/`.

## 10. Paso 8 - Pegar prompt maestro

Abre:

```txt
prompts/automation-master.md
```

Copia todo y pegalo en:

```txt
Agent Instructions
```

Este prompt ya le pide a Cursor:

- leer fuentes RSS/API/manuales;
- revisar inbox;
- revisar feedback del grupo;
- revisar base editorial;
- rankear senales;
- usar novelty score;
- generar una recomendacion principal;
- crear backups solo si valen la pena;
- no conectar Facebook;
- no usar contenido privado.

## 11. Paso 9 - Agregar Memories

Despues de guardar la Automation, abre:

```txt
prompts/memories.md
```

Copia las Memories recomendadas.

Memories clave:

- posicionamiento de WMNMX;
- modelo editorial;
- politica de fuentes;
- traduccion;
- output esperado;
- novelty y audience fit;
- frontera con Facebook.

## 12. Paso 10 - Correr test manual

Antes de activar la Automation diaria, corre:

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

## 13. Paso 11 - Revisar el test

Revisa estos puntos:

### Senales

```txt
[ ] Hay al menos 3 senales candidatas
[ ] Cada senal tiene fuente, resumen y decision
[ ] Hay una recomendacion principal
[ ] Hay backups solo si valen la pena
[ ] Hay senales rechazadas con razon
```

### Fuentes

```txt
[ ] Cada fuente tiene URL o nota de manual intake
[ ] Cada fuente tiene fecha o access date
[ ] La fuente es confiable
[ ] No hay grupos privados, login, paywalls ni contenido restringido
[ ] No hay articulos copiados completos
```

### Calidad editorial

```txt
[ ] El post esta en espanol claro
[ ] No suena condescendiente
[ ] No usa miedo barato
[ ] No suena a guru
[ ] Tiene accion practica
[ ] Tiene pregunta facil
[ ] Explica terminos digitales
```

### Quality Gate

Cada post se evalua sobre 40 puntos:

```txt
Source trust: 0-5
Clear date: 0-5
Clarity: 0-5
Immediate usefulness: 0-5
Relevance women 40+: 0-5
Conversation potential: 0-5
Novelty score: 0-5
Audience fit: 0-5
```

Criterio:

```txt
32/40 o mas = listo para revision humana
24-31 = backup o revision
23 o menos = rechazar
```

## 14. Paso 12 - Activar Automation

Solo cuando el test sea bueno:

```txt
Automations -> WMNMX Daily Content Automation -> Active ON
```

Flujo diario ideal:

```txt
06:00 am - Automation corre
06:45 am - paquete diario listo
08:00 am - humana revisa
09:00 am - equipo agenda manualmente en Facebook
```

## 15. Paso 13 - Operacion diaria

Cada manana abre:

```txt
content/daily/YYYY-MM-DD/
```

Revisa:

```txt
00_signals-ranked.json
02_posts-ready.md
03_visual-briefs.md
04_sources-used.json
06_quality-score.md
07_editorial-notes.md
```

Si publicas manualmente, actualiza cuando puedas:

```txt
content/database/published-posts.jsonl
content/database/used-topics.jsonl
```

Esto ayuda a que Cursor detecte repeticion.

## 16. Paso 14 - Fase 2 con n8n

Cuando el flujo funcione manualmente, usa n8n para poblar:

```txt
content/inbox/YYYY-MM-DD/rss-signals.json
content/inbox/YYYY-MM-DD/api-signals.json
```

n8n debe:

- leer RSS;
- consultar APIs publicas;
- guardar senales;
- no redactar;
- no publicar;
- no conectar Facebook.

Cursor sigue siendo la capa editorial.

## 17. Paso 15 - Fase 3 con Hooks

Despues de 7 a 14 dias de outputs estables, activa Hooks.

El validador revisa:

```txt
[ ] existen los 8 archivos diarios
[ ] 00_signals-ranked.json es valido
[ ] hay novelty score
[ ] hay audience fit
[ ] quality score usa escala 40
[ ] fuentes cumplen politica
[ ] terminos digitales estan explicados
[ ] output esta listo para revision humana
```

## 18. Paso 16 - Fase 4 con Supabase o dashboard

Solo despues de validar el flujo editorial.

Usar Supabase, Airtable o Notion para:

- historial de posts;
- fuentes;
- temas repetidos;
- metricas de engagement;
- calendario editorial.

No hacerlo dependencia critica desde el dia 1.

## 19. Checklist final antes de publicar

```txt
[ ] El tema no esta repetido sin nuevo angulo
[ ] La fuente es confiable
[ ] La accion es segura y realista
[ ] El texto esta claro
[ ] El tono respeta a mujeres +40
[ ] No hay datos privados
[ ] No hay promesas exageradas
[ ] La pregunta invita a conversar
[ ] El equipo humano lo aprueba
```

## 20. Recomendacion final de implementacion

Secuencia recomendada:

```txt
Dia 1: Abrir repo y revisar Rules, Skills, Subagents.
Dia 2: Ajustar fuentes RSS/API/manual intake.
Dia 3: Llenar primer audience insight semanal.
Dia 4: Correr test-run.
Dia 5: Ajustar fuentes, tono y templates.
Dia 6: Crear Automation apagada.
Dia 7: Activar Automation y revisar output.
Dias 8-14: Operar manualmente y medir consistencia.
Despues: agregar n8n, Hooks y base editorial externa si hace falta.
```

La verdad practica: no necesitas que la automatizacion haga mas cosas desde el dia uno. Necesitas que haga mejores decisiones.

El MVP correcto es:

```txt
mejores senales
-> menos repeticion
-> mas contexto del grupo
-> contenido accionable
-> revision humana
-> publicacion con intencion
```

**Love Academy**  
*Siente Mas*
