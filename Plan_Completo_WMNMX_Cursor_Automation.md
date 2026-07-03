Plan completo WMNMX + Cursor Automation
1. Veredicto estratégico

Sí vamos a desarrollar la automatización en Cursor, pero con una arquitectura de trabajo seria:

Rules = política editorial persistente
Skills = manuales de operación / workflows
Subagents = investigadores especializados
MCP = conexión controlada a herramientas externas
Hooks = validación, logging y control de calidad
Automation = motor programado diario
Memories = contexto persistente mínimo
Human Review = última capa de criterio

La automatización se va a construir alrededor de Automations, no de Security Agents ni Approval Agents. Automations es la sección correcta porque permite correr Cloud Agents con triggers programados o por eventos; Rules, Skills, Hooks, MCP y Subagents son las capas que le dan criterio y control al sistema.

2. Qué NO vamos a usar como eje
Security Agents

No son para esta automatización editorial. Sirven para revisar código, bugs, vulnerabilidades, PRs y problemas de seguridad en repositorios.

Approval Agents

Tampoco son MVP para WMNMX. Sirven para aprobar pull requests o rutear revisiones humanas en flujos de desarrollo.

Facebook directo

No vamos a conectar Facebook ni publicar automáticamente en fase 1. Primero necesitamos probar calidad, consistencia y tono durante varios días.

Decisión: Cursor prepara. El equipo revisa. Luego se agenda manualmente en Facebook.

3. Arquitectura final del sistema
wmnmx-content-engine
↓
.cursor/rules/
  editorial voice
  source policy
  translation policy
↓
.cursor/skills/
  master automation skill
  digital safety skill
  AI productivity skill
  social commerce skill
↓
.cursor/agents/
  digital safety subagent
  AI productivity subagent
  social commerce subagent
↓
.cursor/hooks.json
  fase 2: validación automática
↓
MCP tools
  fase 1: web/search/fetch/context
  fase 2: Supabase / dashboard / analytics
↓
Cursor Automation
  scheduled trigger 6:00 am CDMX
↓
Daily output
  /content/daily/YYYY-MM-DD/
↓
Human review
↓
Manual Facebook scheduling
4. Repositorio base

Nombre recomendado:

wmnmx-content-engine

Estructura:

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
        SKILL.md
        references/
          source-allowlist.md
          safety-taxonomy.md
          output-schema.md

      wmnmx-ai-productivity-research/
        SKILL.md
        references/
          source-allowlist.md
          ai-use-cases.md
          prompt-patterns.md
          output-schema.md

      wmnmx-social-commerce-research/
        SKILL.md
        references/
          source-allowlist.md
          commerce-taxonomy.md
          output-schema.md

    agents/
      wmnmx-digital-safety.md
      wmnmx-ai-productivity.md
      wmnmx-social-commerce.md

    hooks.json

  sources/
    allowlist.yml
    rejected-sources.yml

  templates/
    senal-verificada.md
    explicamelo-facil.md
    reto-10-minutos.md
    visual-brief.md

  content/
    daily/
    approved/
    published/

  logs/
    automation-runs.md
5. Rules: política persistente del proyecto

Las Rules son clave porque le dicen a Cursor cómo comportarse siempre dentro de este proyecto. Según la documentación oficial, las Rules sirven para inyectar contexto reutilizable y pueden vivir como Project Rules dentro de .cursor/rules, normalmente en archivos .mdc.

Rule 1 — Voz editorial

Archivo:

.cursor/rules/wmnmx-editorial-voice.mdc

Función:

Mantener tono claro, cálido y útil.
Evitar condescendencia.
Evitar miedo barato.
Evitar lenguaje de gurú.
Escribir para mujeres +40 en México.
Cerrar con preguntas fáciles para activar conversación.

Ejemplo de dirección:

No decir:
"Esto es muy fácil, solo tienes que..."

Sí decir:
"Vamos paso a paso. Revisa esta configuración hoy y cuéntanos si la encontraste."
Rule 2 — Política de fuentes

Archivo:

.cursor/rules/wmnmx-source-policy.mdc

Función:

Definir qué fuentes sí se pueden usar.
Rechazar fuentes débiles.
Evitar scraping riesgoso.
Exigir URL, fecha, fuente y razón de confianza.

Fuentes permitidas:

- páginas públicas
- documentación oficial
- blogs oficiales
- instituciones gubernamentales
- universidades
- reportes serios
- medios confiables
- páginas públicas con fecha clara
- avisos públicos de seguridad

Fuentes prohibidas:

- grupos privados de Facebook
- páginas con login
- paywalls
- contenido sin fecha
- blogs SEO genéricos
- rumores
- posts virales sin fuente primaria
- extracción masiva
- copiar artículos completos
Rule 3 — Traducción y glosario digital

Archivo:

.cursor/rules/wmnx-translation-policy.mdc

Función:

Permitir investigación en inglés.
Producir output final en español.
Mantener términos digitales clave en inglés cuando sean necesarios para alfabetización digital.
Explicar esos términos en español simple.

Regla:

Término digital original + explicación sencilla en español.

Ejemplos:

Phishing: una estafa donde alguien se hace pasar por tu banco, Facebook o una tienda para robarte datos.

Prompt: la instrucción que le das a una IA para que te ayude a escribir, ordenar ideas o resolver una tarea.

DM: mensaje directo. Es donde muchas ventas empiezan antes de llegar al pago.

Deepfake: video, imagen o audio falso hecho con IA.
6. Skills: manuales operativos del sistema

Las Skills son el corazón del método. Cursor las usa como paquetes de instrucciones reutilizables que pueden incluir SKILL.md, referencias, scripts y assets. La documentación confirma que Cursor puede descubrir Skills desde rutas como .cursor/skills/ y que cada Skill vive en su propia carpeta con un SKILL.md.

Vamos a crear 4 Skills.

Skill madre

Nombre:

wmnmx-daily-content-automation

Archivo:

.cursor/skills/wmnmx-daily-content-automation/SKILL.md

Función:

Orquestar todo el sistema diario.

Qué hace:

- activa la rutina diaria
- lee Rules
- invoca los 3 Subagents
- recibe hallazgos
- filtra fuentes
- traduce hallazgos relevantes
- genera 3 posts diarios
- genera briefs visuales
- aplica Quality Gate
- escribe archivos en /content/daily/YYYY-MM-DD/
- prepara todo para revisión humana

Output obligatorio:

/content/daily/YYYY-MM-DD/
  01_research-summary.md
  02_posts-ready.md
  03_visual-briefs.md
  04_sources-used.json
  05_sources-rejected.md
  06_quality-score.md
  07_editorial-notes.md
Skill especialista 1

Nombre:

wmnmx-digital-safety-research

Función:

Investigar seguridad digital.

Temas:

- fraude
- phishing
- robo de identidad
- privacidad
- contraseñas
- 2FA
- passkeys
- deepfakes
- fake news
- WhatsApp security
- Facebook account protection
- pagos digitales

Fuentes prioritarias:

- CONDUSEF
- INAI
- Banco de México
- Policía Cibernética / fuentes oficiales
- Meta Safety
- Google Safety Center
- Microsoft Security
- CISA
- FTC

Este agente alimenta principalmente:

Señal verificada
Alerta Digital
Reto de protección
Skill especialista 2

Nombre:

wmnmx-ai-productivity-research

Función:

Investigar IA y productividad.

Temas:

- ChatGPT
- OpenAI
- Google AI
- Microsoft Copilot
- Meta AI
- Anthropic
- prompts
- workflows
- automatización ligera
- productividad
- organización
- escritura
- atención a clientes
- no-code
- low-code

Fuentes prioritarias:

- OpenAI
- Google
- Microsoft
- Meta
- Anthropic
- documentación oficial
- universidades
- reportes serios

Este agente alimenta principalmente:

IA en 10 minutos
Explícamelo fácil
Prompt práctico
Skill especialista 3

Nombre:

wmnmx-social-commerce-research

Función:

Investigar social commerce y reinvención profesional.

Temas:

- Facebook Groups
- Facebook Pages
- Meta Business Suite
- Instagram
- WhatsApp Business
- catálogos
- ventas por DM
- pagos digitales
- LinkedIn
- CV
- marca personal
- e-commerce
- emprendimiento

Fuentes prioritarias:

- Meta Business Help
- Facebook Help
- Instagram for Business
- WhatsApp Business Help
- LinkedIn
- AMVO
- INEGI
- Shopify
- Mercado Pago
- PayPal
- Stripe

Este agente alimenta principalmente:

Negocio y dinero
Reinvención profesional
Social commerce para principiantes
7. Subagents: investigadores especializados

Los Subagents sirven para dividir tareas complejas, mantener contexto aislado y trabajar en paralelo. La documentación de Cursor los plantea como agentes especializados con su propio prompt, frontmatter y configuración.

Vamos a crear 3 Subagents.

Subagent 1

Archivo:

.cursor/agents/wmnmx-digital-safety.md

Rol:

Investigar señales de seguridad digital.

Configuración:

name: wmnmx-digital-safety
description: Use proactively for daily verified research on digital safety, fraud, phishing, privacy, fake news, account protection, payment safety, and scam prevention for WMNMX.
model: inherit
readonly: true
Subagent 2

Archivo:

.cursor/agents/wmnmx-ai-productivity.md

Rol:

Investigar IA, productividad y herramientas útiles.

Configuración:

name: wmnmx-ai-productivity
description: Use proactively for daily verified research on AI, prompts, productivity, automation, writing, organization, learning workflows, and time-saving tools for WMNMX.
model: inherit
readonly: true
Subagent 3

Archivo:

.cursor/agents/wmnmx-social-commerce.md

Rol:

Investigar ventas digitales, Meta tools, WhatsApp Business, LinkedIn y reinvención profesional.

Configuración:

name: wmnmx-social-commerce
description: Use proactively for daily verified research on social commerce, Facebook, Instagram, WhatsApp Business, Meta tools, catalogs, payments, LinkedIn, employability, entrepreneurship, and digital business growth for WMNMX.
model: inherit
readonly: true
8. MCP: herramientas externas controladas

MCP permite conectar Cursor con herramientas y fuentes externas mediante servidores que exponen tools, prompts o recursos. En los screenshots vi que tienes varios MCPs activos: Chrome DevTools, context7, gsc-server, Mercado Pago, sequential-thinking, Supabase, entre otros. La documentación oficial define MCP como la capa para conectar Cursor con herramientas y fuentes externas.

Configuración recomendada fase 1

Usar:

- Web Search Tool: ON
- Web Fetch Tool: ON
- Chrome DevTools MCP: ON
- context7: ON
- sequential-thinking: ON

Mantener apagado o fuera del flujo:

- meta-mcp
- mercadopago-mcp-server
- supabase como dependencia crítica
- vercel
Por qué

No queremos sobrecargar el MVP. Necesitamos búsqueda, lectura, validación y razonamiento. No necesitamos conectar Facebook ni tocar operaciones reales.

Uso recomendado por herramienta
Chrome DevTools

Para verificar páginas públicas o revisar que una fuente cargue.

context7

Para documentación técnica actualizada.

sequential-thinking

Para evaluar calidad, contradicciones y selección de mejores fuentes.

Supabase

Fase 2 o 3. Puede guardar histórico, scores, fuentes, temas repetidos y métricas.

Meta MCP

Fase futura. No usar hasta tener permisos, política clara y riesgo controlado.

Mercado Pago MCP

Fase futura. Solo si vamos a crear contenidos sobre pagos digitales y seguridad financiera, sin tocar información sensible.

9. Hooks: validación y logging

Hooks permite correr scripts en puntos específicos de la ejecución del agente para modificar comportamiento, reforzar políticas o agregar logging. Según la documentación oficial, Hooks son una capa para ejecutar scripts custom durante la ejecución del agente.

Uso recomendado

No los metemos como pieza crítica en el día 1. Los dejamos como fase 2, cuando ya tengamos buenos outputs.

Hook principal

Archivo:

.cursor/hooks.json

Script:

.cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py

Qué valida:

- que existan los 7 archivos diarios
- que cada post tenga hook
- que cada post tenga explicación
- que cada post tenga acción práctica
- que cada post tenga pregunta de conversación
- que haya fuentes usadas
- que no haya fuentes prohibidas
- que cada score sea mínimo 24/30
- que el output final esté en español
- que los términos digitales clave estén explicados

Output del hook:

/content/daily/YYYY-MM-DD/08_hook-validation.md
Regla

El Hook no debe publicar ni editar creativamente. Solo valida y reporta.

10. Memories: contexto persistente mínimo

Ya que activaste memoria, lo importante es no meter todo ahí. Memories debe contener solo señales estables.

Memory 1 — Positioning
WMNMX is a private Facebook group for women 40+ in Mexico. It helps women adopt technology with confidence, safety, productivity, professional reinvention, AI literacy, and social commerce. The group is a school-community, not a news feed.
Memory 2 — Daily formula
Daily WMNMX content must follow this formula: 1 verified signal + 1 simple explanation + 1 ten-minute challenge. Never publish three links. Every post must inform, translate, or activate.
Memory 3 — Translation policy
Final outputs must be in Spanish. Keep key digital terms in English when the audience needs to recognize them online: phishing, ghosting, love bombing, DM, prompt, deepfake, 2FA, passkey, malware, scam, bot, chatbot, workflow, no-code, low-code, social commerce, e-commerce. Explain each term simply in Spanish.
Memory 4 — Source policy
Use verified public sources only. Do not use private Facebook groups, login-protected pages, paywalls, restricted pages, viral posts without sources, undated content, or generic SEO blogs. Do not copy full articles.
Memory 5 — Output standard
Every daily run must create /content/daily/YYYY-MM-DD/ with research summary, posts ready, visual briefs, sources used, sources rejected, quality score, and editorial notes.
11. Automation diaria

La Automation será el motor diario.

Configuración

En Cursor:

Automations → New Automation

Parámetros:

Active: sí, solo después del test
Repository: wmnmx-content-engine
Trigger: Scheduled
Horario: 6:00 am CDMX
Tools: Web Search, Web Fetch, MCP controlado
Memories: configurar después de guardar
Prompt maestro para Automation

Este prompt va en Agent Instructions:

Run the WMNMX Daily Content Automation.

Repository:
Use the selected repository as the persistent content engine.

Project context:
WMNMX is a private Facebook group for women 40+ in Mexico focused on technology adoption, digital safety, AI, productivity, professional reinvention, and social commerce.

Core goal:
Produce a daily editorial package that helps the community gain digital confidence, practical autonomy, and competitive advantage.

Important:
This automation must not publish to Facebook.
This automation must not connect to Facebook.
Prepare content for human review and manual scheduling only.

Use the project skills:
- wmnmx-daily-content-automation
- wmnmx-digital-safety-research
- wmnmx-ai-productivity-research
- wmnmx-social-commerce-research

Use the project subagents when useful:
- wmnmx-digital-safety
- wmnmx-ai-productivity
- wmnmx-social-commerce

Research mode:
Monitor verified public sources only.

Allowed:
- public pages
- RSS feeds
- official documentation
- official blogs
- government institutions
- universities
- public security advisories
- reputable media
- platform help centers
- public business and technology reports

Not allowed:
- private Facebook groups
- login-protected pages
- paywalled content
- restricted pages
- mass scraping
- copied full articles
- undated content
- rumor-based content
- viral posts without primary source
- generic SEO blogs

Language:
Use English for internal reasoning, research coordination, and source analysis when useful.
Final outputs must be in Spanish.
Use clear, simple, Mexican-context language.
Do not sound condescending.
Do not use fear as clickbait.
Do not use guru marketing language.

Translation rule:
Keep key digital terms in English when they are important for digital literacy, then explain them in simple Spanish.
Examples: phishing, ghosting, love bombing, DM, prompt, deepfake, 2FA, passkey, malware, scam, bot, chatbot, workflow, no-code, low-code, social commerce, e-commerce, marketplace, lead, checkout.

Daily content formula:
Create exactly 3 Facebook-ready posts:

1. Señal verificada
Purpose: inform.
Use one verified source or update.
Explain what happened, why it matters for women 40+, what risk or opportunity it opens, and what to do today.

2. Explícamelo fácil
Purpose: translate and simplify.
Turn a digital topic into a simple explanation, mini-guide, carousel idea, or visual brief.

3. Reto de 10 minutos
Purpose: activate.
Create one practical action the community can complete in 10 minutes or less.

Required output folder:
Create a folder under:

/content/daily/YYYY-MM-DD/

Required files:

1. 01_research-summary.md
2. 02_posts-ready.md
3. 03_visual-briefs.md
4. 04_sources-used.json
5. 05_sources-rejected.md
6. 06_quality-score.md
7. 07_editorial-notes.md

Each Facebook-ready post must include:
- title
- post type
- hook
- simple explanation
- why it matters for women 40+
- practical action
- easy question to activate comments
- source reference when applicable
- recommended publishing time
- visual brief

Quality gate:
Score each post from 0 to 5 on:
- source trust
- clear date
- clarity
- immediate usefulness
- relevance for women 40+
- conversation potential

Minimum score:
24/30.

If a post scores below 24, revise it or mark it as not ready.

Editorial note:
At the end, include what a human editor should check before scheduling.
12. Prompt de test

Antes de activar la Automation:

Test the WMNMX Daily Content Automation without scheduling.

Use the current repository and generate a sample daily package for tomorrow.

Do not publish.
Do not connect to Facebook.
Do not use private or restricted sources.

Use the project skills and subagents if available.

Create the output under:

/content/daily/test-run-YYYY-MM-DD/

Generate:
1. 01_research-summary.md
2. 02_posts-ready.md
3. 03_visual-briefs.md
4. 04_sources-used.json
5. 05_sources-rejected.md
6. 06_quality-score.md
7. 07_editorial-notes.md

Final output must be in Spanish.
Use simple Mexican-context language for women 40+.
Keep important digital terms in English and explain them in Spanish.
13. Quality Gate

Cada post se evalúa sobre 30 puntos.

Fuente confiable: 0-5
Fecha clara: 0-5
Claridad: 0-5
Utilidad inmediata: 0-5
Relevancia mujeres +40: 0-5
Potencial de conversación: 0-5

Criterio:

24/30 o más = listo para revisión humana
menos de 24 = reescribir o descartar
14. Output diario esperado

Cada día se crea:

/content/daily/YYYY-MM-DD/

Con:

01_research-summary.md

Resumen de lo investigado por los 3 agentes.

02_posts-ready.md

Los 3 posts listos para Facebook.

03_visual-briefs.md

Briefs para imagen, carrusel o post visual.

04_sources-used.json

Fuentes usadas, con URL, fecha, tipo y score.

05_sources-rejected.md

Fuentes descartadas y razón.

06_quality-score.md

Evaluación de cada post.

07_editorial-notes.md

Notas para la editora humana.

Fase 2:

08_hook-validation.md

Validación automática por Hook.

15. Flujo diario operativo
06:00 am
Automation corre por trigger programado.

06:01 am
Parent Agent lee Rules + Skill madre.

06:02 am
Parent Agent invoca Subagents.

06:02–06:20 am
Subagents investigan fuentes verificadas.

06:20 am
Parent Agent consolida hallazgos.

06:25 am
Traducción contextual a español.

06:30 am
Generación de 3 posts + visual briefs.

06:35 am
Quality Gate.

06:40 am
Creación de archivos diarios.

Fase 2:
Hook valida estructura, fuentes y score.

08:00 am
Humano revisa.

09:00 am
Se agenda manualmente en Facebook.
16. Fases de implementación
Fase 1 — MVP limpio

Construir:

- repo
- Rules
- Skills
- Subagents
- templates
- allowlist
- rejected sources
- prompt maestro
- prompt de test
- Memories

Objetivo:

Producir paquetes editoriales diarios sin Hooks ni integraciones complejas.

Fase 2 — Control de calidad automático

Agregar:

- hooks.json
- validate_daily_output.py
- hook validation report
- logs

Objetivo:

Que el sistema valide estructura, fuentes, español, glosario y quality score.

Fase 3 — Base editorial

Opcional:

- Supabase
- dashboard
- histórico de temas
- control de repetición
- métricas de performance

Objetivo:

Evitar repetir temas, medir qué funciona y construir inteligencia editorial.

Fase 4 — Integración de calendario

Opcional:

- Notion
- Airtable
- Google Sheets

Objetivo:

Pasar de output en Markdown a calendario editorial revisable por equipo.

Fase 5 — Integración Meta / Facebook

Solo después.

Condiciones:

- 7 a 14 días de output estable
- calidad consistente
- permisos claros
- revisión legal/política
- no riesgo de spam
17. Lo que voy a construir cuando me des luz verde

Te preparo un paquete completo con:

1. Guía final en .md
2. Repo skeleton
3. 4 Skills completas
4. 3 Subagents completos
5. 3 Rules .mdc
6. Prompt maestro de Automation
7. Prompt de test
8. Memories sugeridas
9. Source allowlist
10. Rejected sources base
11. Templates de posts
12. Translation glossary
13. Quality Gate
14. Hook de validación fase 2
15. Script validate_daily_output.py
16. README de instalación en Cursor
17. ZIP descargable listo para usar
18. Decisión final recomendada

La secuencia correcta es:

Primero:
Rules + Skills + Subagents + Automation

Después:
MCP controlado

Luego:
Hooks de validación

Más adelante:
Supabase / calendario / dashboard / integración Meta

Mi postura: no necesitamos una automatización que haga más ruido. Necesitamos una máquina editorial que produzca confianza diaria.

El valor real para WMNMX está aquí:

fuente verificada
→ traducción digital clara
→ utilidad para mujeres +40
→ acción de 10 minutos
→ revisión humana
→ publicación con intención

Ese es el sistema que sí puede hacer crecer el grupo sin volverlo un feed más.