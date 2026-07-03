# WMNMX Content Engine

Sistema editorial automatizado para **WMNMX**, un grupo privado de Facebook para mujeres +40 en Mexico enfocado en adopcion tecnologica, seguridad digital, IA, productividad, reinvencion profesional y social commerce.

Este repositorio esta disenado para funcionar en Cursor como una **redaccion editorial automatizada con criterio**, no como autoposter ni como scraper agresivo.

## Principio estrategico actualizado

La automatizacion no debe empezar todos los dias con una busqueda libre. Debe operar sobre una bandeja de senales confiables.

Flujo recomendado:

```txt
fuentes permitidas
-> bandeja de senales
-> verificacion y deduplicacion
-> novelty score
-> ajuste con feedback real del grupo
-> traduccion digital clara
-> utilidad para mujeres +40
-> accion practica
-> revision humana
-> publicacion manual con intencion
```

## Arquitectura del sistema

El proyecto combina:

- **Rules**: politica editorial, fuentes y traduccion persistente.
- **Skills**: workflows reutilizables para investigacion, seleccion y produccion.
- **Subagents**: investigadores especializados por tema y por etapa.
- **Signal Inbox**: bandeja diaria de senales provenientes de RSS, APIs, busqueda controlada y aportes manuales.
- **Editorial Memory**: historial local de temas, fuentes, publicaciones y rechazos para evitar repeticion.
- **Audience Feedback**: notas semanales de preguntas, dudas y conversaciones reales del grupo.
- **Quality Gate**: evaluacion de fuente, claridad, utilidad, relevancia, conversacion y novedad.
- **Human Review**: ultima capa de criterio antes de publicar.

## Que si debe hacer

- Monitorear fuentes publicas verificadas.
- Usar RSS y APIs como primera opcion.
- Usar web search/fetch de forma controlada.
- Usar scraping solo en paginas publicas cuando no exista RSS/API.
- Rechazar grupos privados, paywalls, paginas con login y contenido sin fuente primaria.
- Generar contenido en espanol claro, contextualizado para mujeres +40 en Mexico.
- Mantener terminos digitales en ingles cuando ayudan a la alfabetizacion digital, explicandolos en espanol.
- Producir contenido listo para revision humana, no para publicacion automatica.

## Que no debe hacer

- No publicar directamente en Facebook.
- No conectar Facebook en fase 1.
- No scrapear grupos privados.
- No depender de una sola fuente o de busquedas libres cada dia.
- No generar tres posts por obligacion si solo hay una senal realmente fuerte.
- No repetir temas sin novelty score.
- No usar miedo, tono condescendiente ni lenguaje de guru.

## Herramientas recomendadas

Fase 1:

- Web Search Tool: ON
- Web Fetch Tool: ON
- RSS/API intake mediante archivos en `sources/`
- Chrome DevTools MCP: ON solo para verificacion puntual
- context7: ON para documentacion tecnica actualizada
- sequential-thinking: ON para scoring y razonamiento editorial

Mantener fuera del flujo inicial:

- meta-mcp
- mercadopago-mcp-server
- supabase como dependencia critica
- vercel

Fase 2:

- n8n para poblar `content/inbox/` desde RSS/APIs.
- Hooks para validacion estructural.
- Base editorial local en `content/database/`.

Fase 3:

- Supabase o Airtable si el volumen y el historial editorial ya justifican una base externa.

## Output diario esperado

Cada corrida debe generar, como minimo:

```txt
/content/daily/YYYY-MM-DD/
  00_signals-ranked.json
  01_research-summary.md
  02_posts-ready.md
  03_visual-briefs.md
  04_sources-used.json
  05_sources-rejected.md
  06_quality-score.md
  07_editorial-notes.md
```

Fase 2, con hooks:

```txt
/content/daily/YYYY-MM-DD/08_hook-validation.md
```

## Carpetas nuevas clave

```txt
content/inbox/              # senales capturadas antes de redactar
content/database/           # historial local de temas, fuentes y publicaciones
content/audience-insights/  # feedback semanal del grupo
sources/rss-feeds.yml       # feeds RSS permitidos
sources/api-sources.yml     # APIs publicas permitidas
sources/manual-intake.yml   # reglas para aportes manuales
```

## Modos editoriales

Ademas de la formula base, el sistema puede producir distintos modos segun la senal:

- Senal verificada
- Explicamelo facil
- Reto de 10 minutos
- Alerta practica
- Mito vs realidad
- Checklist guardable
- Caso aplicado
- Pregunta detonadora
- Mini clase

## Instalacion en Cursor

1. Abre este folder como workspace en Cursor.
2. Revisa que Cursor detecte `.cursor/rules/`, `.cursor/skills/` y `.cursor/agents/`.
3. Configura Tools y MCPs segun la fase.
4. Revisa y ajusta `sources/rss-feeds.yml`, `sources/api-sources.yml` y `sources/manual-intake.yml`.
5. Pega `prompts/automation-master.md` en Agent Instructions.
6. Configura Memories usando `prompts/memories.md`.
7. Corre primero `prompts/test-run.md`.
8. Revisa el paquete en `content/daily/test-run-YYYY-MM-DD/`.
9. Activa la Automation diaria solo cuando el output pase revision.

**Love Academy**  
*Siente Mas*
