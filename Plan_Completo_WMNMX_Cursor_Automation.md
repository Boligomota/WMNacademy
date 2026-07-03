# Plan completo WMNMX + Cursor Automation

## 1. Veredicto estrategico actualizado

Si conviene desarrollar la automatizacion en Cursor, pero no como un scraper ni como una busqueda diaria libre. La mejor version debe funcionar como una **maquina editorial de inteligencia de contenido tech**.

La arquitectura recomendada es hibrida:

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

Cursor debe ser la capa de criterio editorial. La captura recurrente de senales puede vivir en Cursor al inicio, pero debe estar preparada para moverse a n8n, cron, Supabase o una API cuando el volumen crezca.

## 2. Que ya esta bien planteado

La base actual es solida en estos puntos:

- No publicar automaticamente en Facebook.
- No conectar Facebook en fase 1.
- No scrapear grupos privados, paywalls ni paginas con login.
- Usar Rules para tono, fuentes y traduccion.
- Usar Skills para workflows reutilizables.
- Usar Subagents para dividir investigacion por tema.
- Usar Quality Gate y revision humana.
- Producir en espanol claro para mujeres +40 en Mexico.

Eso se mantiene.

## 3. Lo que cambia con la mejora

El sistema no debe depender solo de que el agente investigue bien cada dia. Debe tener una capa previa de **discovery sistematico**.

Cambios clave:

1. Agregar bandeja de senales en `content/inbox/`.
2. Agregar fuentes RSS y APIs en `sources/`.
3. Agregar intake manual para enlaces del equipo o moderadoras.
4. Agregar base editorial local en `content/database/`.
5. Agregar feedback semanal del grupo en `content/audience-insights/`.
6. Agregar novelty score para evitar repeticion.
7. Agregar modos editoriales mas variados.
8. Permitir que el output diario recomiende 1 post fuerte y backups, no siempre 3 posts por obligacion.

## 4. Arquitectura final recomendada

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
      README.md
    daily/
    approved/
    published/
    database/
      README.md
    audience-insights/
      weekly-notes-template.md

  logs/
    automation-runs.md

  README.md
```

## 5. Roles del sistema

### Cursor

Cursor debe:

- leer reglas y skills;
- consultar la bandeja de senales;
- investigar solo cuando falte contexto;
- verificar fuentes;
- comparar contra historial editorial;
- generar recomendacion editorial;
- producir posts y visual briefs;
- aplicar Quality Gate;
- preparar todo para revision humana.

### n8n o automatizador externo, fase 2

n8n puede:

- leer RSS;
- consultar APIs publicas;
- guardar senales crudas en `content/inbox/` o Supabase;
- enviar notificaciones si hay senales urgentes;
- no redactar ni publicar.

### Humano editor

La editora o equipo debe:

- revisar el paquete diario;
- aprobar, editar o descartar;
- registrar feedback del grupo;
- programar manualmente en Facebook.

## 6. Fuentes recomendadas

Prioridad 1: fuentes estructuradas y permitidas.

- RSS oficiales.
- Blogs oficiales.
- Documentacion oficial.
- APIs publicas.
- Newsletters reenviadas manualmente.
- Reportes institucionales.
- Aportes manuales del equipo.

Prioridad 2: busqueda web controlada.

- Usar web search para complementar, no como unica base.
- Exigir fuente primaria cuando sea posible.
- Rechazar contenido SEO generico.

Prioridad 3: scraping puntual.

- Solo paginas publicas.
- Solo si no hay RSS/API.
- Respetando robots.txt, terminos de uso, frecuencia baja y sin login.

No usar:

- grupos privados de Facebook;
- paginas con login;
- paywalls;
- scraping masivo;
- contenido viral sin fuente primaria;
- publicaciones privadas o restringidas.

## 7. Nuevo flujo diario operativo

```txt
06:00  Automation inicia
06:01  Lee Rules, Skills, Memories y audience-insights recientes
06:03  Lee content/inbox/ y sources/
06:08  Completa investigacion con web search/fetch solo si hace falta
06:15  Verifica fuentes y rechaza senales debiles
06:20  Deduplica contra content/database/
06:25  Calcula novelty score y audience fit
06:30  Selecciona 1 senal principal y 2 backups
06:35  Produce post(s), visual brief y notas editoriales
06:40  Aplica Quality Gate
06:45  Escribe archivos diarios
08:00  Humano revisa
09:00  Equipo agenda manualmente en Facebook
```

## 8. Output diario esperado

Cada corrida debe crear:

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

`02_posts-ready.md` puede incluir:

- 1 post principal listo para revision;
- 1 o 2 posts backup si las senales lo justifican;
- ideas descartadas si no alcanzan calidad.

No debe forzar tres posts si solo hay una senal realmente buena.

## 9. Quality Gate actualizado

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

Auto-rechazo:

- fuente no confiable;
- no hay fecha en un tema sensible a recencia;
- repite un tema publicado recientemente sin nuevo angulo;
- suena generico;
- no tiene accion practica;
- depende de miedo, promesa exagerada o lenguaje de guru.

## 10. Modos editoriales recomendados

Ademas de la formula base, el sistema debe elegir el modo que mejor sirva a la senal:

- Senal verificada: informar una novedad importante.
- Explicamelo facil: traducir un concepto.
- Reto de 10 minutos: activar una accion concreta.
- Alerta practica: prevenir un riesgo sin miedo.
- Mito vs realidad: corregir confusion comun.
- Checklist guardable: crear un recurso evergreen.
- Caso aplicado: aterrizar a negocio, empleo o vida diaria.
- Pregunta detonadora: activar conversacion.
- Mini clase: explicar un paso a paso breve.

## 11. Fases de implementacion

### Fase 1 - Cursor mejorado

Construir y probar:

- Rules
- Skills
- Subagents actuales
- prompts
- templates
- `sources/rss-feeds.yml`
- `sources/api-sources.yml`
- `sources/manual-intake.yml`
- `content/inbox/README.md`
- `content/database/README.md`
- `content/audience-insights/weekly-notes-template.md`

Objetivo: producir paquetes editoriales con senales rankeadas, novelty score y revision humana.

### Fase 2 - Ingestion con n8n

Agregar n8n para capturar:

- RSS;
- APIs publicas;
- newsletters reenviadas;
- formularios manuales.

Objetivo: que Cursor no tenga que descubrir todo desde cero cada dia.

### Fase 3 - Validacion automatica

Agregar:

- hooks;
- `validate_daily_output.py` actualizado;
- reportes de validacion;
- logs.

Objetivo: validar estructura, fuentes, idioma, novelty y quality score.

### Fase 4 - Base editorial externa

Solo cuando haya volumen suficiente:

- Supabase;
- Airtable;
- Notion;
- dashboard editorial.

Objetivo: medir repeticion, rendimiento, temas y aprendizaje editorial.

### Fase 5 - Integracion Meta/Facebook

Solo considerar despues de:

- 14 a 30 dias de output estable;
- permisos claros;
- revision de riesgos;
- cero dependencia de grupos privados;
- politica clara anti-spam;
- decision humana final.

## 12. Decision final recomendada

La mejor ruta es:

```txt
Ruta 2 primero: n8n/RSS/API para ingestion + Cursor para criterio editorial.
Ruta 3 despues: Supabase o dashboard cuando haya datos reales.
```

No necesitamos una automatizacion que publique mas. Necesitamos una infraestructura editorial que detecte buenas senales, las traduzca con criterio y aprenda de la comunidad.

El valor real para WMNMX esta aqui:

```txt
senal confiable
-> contexto real del grupo
-> explicacion simple
-> accion practica
-> revision humana
-> publicacion con intencion
```
