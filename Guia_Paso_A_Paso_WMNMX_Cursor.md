# Guía paso a paso — Desarrollo de la automatización WMNMX en Cursor

## 0. Qué estás montando

Vas a montar un sistema editorial automatizado para **WMNMX**, un grupo privado de Facebook para mujeres +40 en México enfocado en:

- adopción tecnológica;
- seguridad digital;
- IA;
- productividad;
- reinvención profesional;
- social commerce;
- autonomía digital.

La lógica del sistema es:

```txt
Fuente verificada
→ investigación controlada
→ traducción digital clara
→ utilidad para mujeres +40
→ acción de 10 minutos
→ revisión humana
→ publicación manual en Facebook
```

Cursor no va a publicar automáticamente en Facebook en fase 1.  
Cursor va a funcionar como una **redacción editorial automatizada con criterio**.

---

# 1. Archivos que ya tienes desarrollados

El paquete principal es:

```txt
wmnmx-content-engine.zip
```

Al descomprimirlo, debe aparecer esta carpeta:

```txt
wmnmx-content-engine/
```

Dentro de esa carpeta está todo el sistema:

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
    hooks.example.json
    mcp.recommendations.md

  sources/
    allowlist.yml
    rejected-sources.yml

  templates/
    senal-verificada.md
    explicamelo-facil.md
    reto-10-minutos.md
    visual-brief.md

  prompts/
    automation-master.md
    test-run.md
    memories.md

  content/
    daily/
    approved/
    published/

  docs/
    INSTALL_CURSOR_STEP_BY_STEP.md
    PLAN_COMPLETO_WMNMX_CURSOR_AUTOMATION.md

  logs/
    automation-runs.md

  README.md
```

---

# 2. Qué hace cada bloque

## 2.1 `.cursor/rules/`

Aquí viven las reglas persistentes del proyecto.

Estas reglas se aplican para mantener consistencia de tono, fuentes y traducción.

Archivos:

```txt
.cursor/rules/wmnmx-editorial-voice.mdc
.cursor/rules/wmnmx-source-policy.mdc
.cursor/rules/wmnmx-translation-policy.mdc
```

### `wmnmx-editorial-voice.mdc`

Controla:

- tono claro;
- tono cálido;
- cero condescendencia;
- cero miedo barato;
- cero lenguaje de gurú;
- español mexicano claro;
- preguntas fáciles para activar conversación.

### `wmnmx-source-policy.mdc`

Controla:

- qué fuentes sí se pueden usar;
- qué fuentes se deben rechazar;
- no scraping riesgoso;
- no paywalls;
- no grupos privados;
- no páginas con login;
- no contenido viral sin fuente primaria.

### `wmnmx-translation-policy.mdc`

Controla la traducción contextual.

Regla principal:

```txt
Término digital original + explicación sencilla en español.
```

Ejemplo:

```txt
Phishing: una estafa donde alguien se hace pasar por tu banco, Facebook o una tienda para robarte datos.
```

---

## 2.2 `.cursor/skills/`

Aquí viven las Skills.

Las Skills son manuales operativos para que Cursor sepa cómo trabajar.

Tenemos 4 Skills:

```txt
wmnmx-daily-content-automation
wmnmx-digital-safety-research
wmnmx-ai-productivity-research
wmnmx-social-commerce-research
```

### Skill madre

```txt
.cursor/skills/wmnmx-daily-content-automation/SKILL.md
```

Función:

- orquestar la automatización diaria;
- invocar subagents;
- consolidar investigación;
- traducir a español;
- generar 3 posts;
- generar briefs visuales;
- aplicar Quality Gate;
- crear archivos diarios.

### Skill especialista 1

```txt
.cursor/skills/wmnmx-digital-safety-research/SKILL.md
```

Función:

Investigar:

- fraudes;
- phishing;
- privacidad;
- fake news;
- 2FA;
- passkeys;
- deepfakes;
- seguridad en Facebook, WhatsApp, Instagram y pagos digitales.

### Skill especialista 2

```txt
.cursor/skills/wmnmx-ai-productivity-research/SKILL.md
```

Función:

Investigar:

- IA;
- prompts;
- herramientas de productividad;
- automatización ligera;
- no-code;
- low-code;
- organización;
- escritura;
- atención a clientes.

### Skill especialista 3

```txt
.cursor/skills/wmnmx-social-commerce-research/SKILL.md
```

Función:

Investigar:

- Facebook Groups;
- Meta Business Suite;
- Instagram;
- WhatsApp Business;
- ventas por DM;
- pagos digitales;
- LinkedIn;
- marca personal;
- e-commerce;
- emprendimiento.

---

## 2.3 `.cursor/agents/`

Aquí viven los Subagents.

Los Subagents son investigadores especializados que trabajan con contexto separado.

Archivos:

```txt
.cursor/agents/wmnmx-digital-safety.md
.cursor/agents/wmnmx-ai-productivity.md
.cursor/agents/wmnmx-social-commerce.md
```

Cada uno tiene:

- nombre;
- descripción;
- modelo heredado;
- modo `readonly: true`;
- misión;
- fuentes recomendadas;
- reglas de rechazo;
- formato de output.

---

## 2.4 `.cursor/hooks.json`

Aquí vive la configuración de Hooks.

En fase 1, los Hooks no son la pieza principal.  
En fase 2, servirán para validar que el output diario cumpla con estructura, fuentes, idioma y Quality Gate.

Archivos relacionados:

```txt
.cursor/hooks.json
.cursor/hooks.example.json
.cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py
```

El script principal de validación es:

```txt
.cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py
```

Valida:

- que existan los 7 archivos diarios;
- que los posts tengan hook;
- que tengan explicación;
- que tengan acción práctica;
- que tengan pregunta;
- que haya fuentes;
- que no haya fuentes prohibidas;
- que el score mínimo sea 24/30;
- que el output esté en español;
- que los términos digitales clave estén explicados.

---

## 2.5 `prompts/`

Aquí están los prompts listos para copiar y pegar en Cursor.

Archivos:

```txt
prompts/automation-master.md
prompts/test-run.md
prompts/memories.md
```

### `automation-master.md`

Es el prompt que va en **Agent Instructions** dentro de la Automation.

### `test-run.md`

Es el prompt para correr una prueba manual antes de activar la automatización diaria.

### `memories.md`

Contiene las Memories recomendadas para que la Automation conserve contexto estable.

---

## 2.6 `sources/`

Aquí vive la política de fuentes editable.

Archivos:

```txt
sources/allowlist.yml
sources/rejected-sources.yml
```

### `allowlist.yml`

Lista fuentes permitidas o preferidas.

Ejemplos:

- OpenAI;
- Google;
- Microsoft;
- Meta;
- CONDUSEF;
- INAI;
- Banco de México;
- LinkedIn;
- WhatsApp Business;
- AMVO;
- INEGI.

### `rejected-sources.yml`

Lista fuentes o tipos de fuentes que el sistema debe evitar.

Ejemplos:

- blogs SEO genéricos;
- contenido sin fecha;
- paywalls;
- páginas con login;
- grupos privados de Facebook;
- posts virales sin fuente primaria.

---

## 2.7 `templates/`

Aquí están las plantillas editoriales.

Archivos:

```txt
templates/senal-verificada.md
templates/explicamelo-facil.md
templates/reto-10-minutos.md
templates/visual-brief.md
```

La automatización debe generar tres piezas diarias con esta fórmula:

```txt
1 señal verificada + 1 explicación visual + 1 reto práctico diario
```

---

## 2.8 `content/`

Aquí se guardan los outputs diarios.

Estructura:

```txt
content/
  daily/
  approved/
  published/
```

Cada corrida diaria debe crear:

```txt
content/daily/YYYY-MM-DD/
  01_research-summary.md
  02_posts-ready.md
  03_visual-briefs.md
  04_sources-used.json
  05_sources-rejected.md
  06_quality-score.md
  07_editorial-notes.md
```

En fase 2, con Hooks:

```txt
content/daily/YYYY-MM-DD/08_hook-validation.md
```

---

# 3. Paso a paso para montar todo en Cursor

## Paso 1 — Descargar y descomprimir el ZIP

Descarga:

```txt
wmnmx-content-engine.zip
```

Descomprímelo en una ubicación fácil de encontrar.

Ejemplo:

```txt
Documents/Cursor Projects/wmnmx-content-engine/
```

La carpeta raíz debe llamarse:

```txt
wmnmx-content-engine
```

---

## Paso 2 — Abrir el repo en Cursor

En Cursor:

```txt
File → Open Folder
```

Selecciona la carpeta:

```txt
wmnmx-content-engine/
```

Importante: abre la carpeta raíz, no una subcarpeta.

Debes ver en el explorador:

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

---

## Paso 3 — Confirmar que Cursor detecta Rules, Skills y Subagents

En Cursor, ve a:

```txt
Settings → Rules, Skills, Subagents
```

Revisa tres secciones:

### Rules

Deben aparecer:

```txt
wmnmx-editorial-voice
wmnmx-source-policy
wmnmx-translation-policy
```

### Skills

Deben aparecer:

```txt
wmnmx-daily-content-automation
wmnmx-digital-safety-research
wmnmx-ai-productivity-research
wmnmx-social-commerce-research
```

### Subagents

Deben aparecer:

```txt
wmnmx-digital-safety
wmnmx-ai-productivity
wmnmx-social-commerce
```

Si no aparecen, revisa que los archivos estén exactamente aquí:

```txt
.cursor/rules/
.cursor/skills/
.cursor/agents/
```

---

# 4. Configuración recomendada de Cursor

## Paso 4 — Configurar Tools & MCPs

Ve a:

```txt
Settings → Tools & MCPs
```

Para fase 1, usa esta configuración:

```txt
Web Search Tool: ON
Web Fetch Tool: ON
Chrome DevTools MCP: ON
context7: ON
sequential-thinking: ON
```

Mantén fuera del flujo al inicio:

```txt
meta-mcp: OFF
mercadopago-mcp-server: OFF
supabase: OFF o sin dependencia crítica
vercel: OFF
```

### Por qué

No queremos sobrecargar la automatización desde el día 1.

Fase 1 necesita:

- búsqueda;
- lectura;
- verificación;
- razonamiento;
- generación editorial.

No necesita:

- conectar Facebook;
- tocar pagos;
- tocar datos sensibles;
- publicar directo;
- depender de una base externa.

---

## Paso 5 — Configurar Agents Settings

Ve a:

```txt
Settings → Agents
```

Recomendación para fase de prueba:

```txt
Web Search Tool: ON
Web Fetch Tool: ON
Browser Protection: ON si vas a navegar web
MCP Tools Protection: ON al inicio
Auto-accept web search: OFF hasta validar fuentes
```

Si tienes `Run Everything (Unsandboxed)`, úsalo con cuidado.

Para MVP estable, la recomendación es trabajar con:

- fuentes permitidas;
- revisión humana;
- no navegación libre sin criterio;
- no conexión directa a Facebook.

---

## Paso 6 — Configurar Cloud Agents

Ve al dashboard de Cursor:

```txt
Dashboard → Cloud Agents
```

Configura:

```txt
Default repository: wmnmx-content-engine
Default model: el modelo que prefieras usar
Branch prefix: wmnmx/daily-content/
```

Si aparece `No environments configured`, crea o configura un environment antes de depender de Automations en la nube.

Para fase 1:

```txt
Secrets: vacío
Network Access: controlado si Cursor te deja limitarlo
Slack Notifications: opcional
```

---

# 5. Crear la Automation diaria

## Paso 7 — Ir a Automations

En Cursor:

```txt
Automations → New Automation
```

Configura:

```txt
Active: OFF al inicio
Repository: wmnmx-content-engine
Trigger: Scheduled
Horario sugerido: 6:00 am CDMX
```

Importante: no dejes `No Repository`.

Para este sistema necesitas que Cursor escriba archivos en:

```txt
content/daily/YYYY-MM-DD/
```

Así que la Automation debe estar ligada al repo.

---

## Paso 8 — Pegar el prompt maestro

Abre este archivo:

```txt
prompts/automation-master.md
```

Copia todo el contenido.

Pégalo en:

```txt
Agent Instructions
```

Este prompt le dice a Cursor:

- qué es WMNMX;
- qué skills usar;
- qué subagents usar;
- qué fuentes permitir;
- qué fuentes prohibir;
- que el output final debe ir en español;
- que debe mantener términos digitales clave en inglés y explicarlos;
- que debe crear tres posts diarios;
- que debe crear los 7 archivos;
- que no debe publicar en Facebook.

---

## Paso 9 — Guardar la Automation

Guarda la Automation antes de configurar Memories.

En los screenshots se ve que Cursor pide guardar primero para habilitar y configurar memory notes.

---

## Paso 10 — Agregar Memories

Después de guardar la Automation, abre:

```txt
prompts/memories.md
```

Copia las Memories recomendadas y agrégalas en la sección de Memories de la Automation.

Memories recomendadas:

```txt
1. Positioning
2. Daily formula
3. Translation policy
4. Source policy
5. Output standard
```

No metas toda la estrategia en Memories.  
Para eso están Rules y Skills.

---

# 6. Correr test antes de activar

## Paso 11 — Ejecutar prueba manual

Antes de activar la Automation diaria, corre una prueba con:

```txt
prompts/test-run.md
```

Puedes hacerlo desde Agent en Cursor.

Este prompt debe crear:

```txt
content/daily/test-run-YYYY-MM-DD/
```

Con:

```txt
01_research-summary.md
02_posts-ready.md
03_visual-briefs.md
04_sources-used.json
05_sources-rejected.md
06_quality-score.md
07_editorial-notes.md
```

---

## Paso 12 — Revisar el output de prueba

Abre:

```txt
content/daily/test-run-YYYY-MM-DD/
```

Revisa estos puntos:

### Revisión editorial

- ¿El español suena claro?
- ¿No suena condescendiente?
- ¿No usa miedo barato?
- ¿No suena a gurú de ventas?
- ¿La explicación se entiende para mujeres +40?
- ¿El término digital se mantiene cuando conviene?
- ¿El término digital se explica en español?

### Revisión de fuentes

- ¿Hay fuentes verificadas?
- ¿Cada fuente tiene URL?
- ¿Cada fuente tiene fecha?
- ¿La fuente es oficial, institucional, seria o confiable?
- ¿Se descartaron fuentes débiles?

### Revisión de utilidad

- ¿Cada post tiene acción práctica?
- ¿El reto se puede hacer en 10 minutos?
- ¿La pregunta invita a comentar?
- ¿Hay valor real o solo información?

### Revisión de Quality Gate

Cada post debe tener mínimo:

```txt
24/30
```

Si algo baja de 24, no se publica. Se reescribe.

---

# 7. Activar la Automation

## Paso 13 — Activar solo después del test

Cuando el test produzca buen output:

```txt
Automations → WMNMX Daily Content Automation → Active ON
```

Horario recomendado:

```txt
6:00 am CDMX
```

Flujo diario ideal:

```txt
06:00 am — Automation corre
06:40 am — archivos diarios listos
08:00 am — humana revisa
09:00 am — se agenda manualmente en Facebook
```

---

# 8. Publicación manual en Facebook

## Paso 14 — Tomar contenido listo

Cada día abre:

```txt
content/daily/YYYY-MM-DD/02_posts-ready.md
```

Ahí estarán los tres posts:

```txt
1. Señal verificada
2. Explícamelo fácil
3. Reto de 10 minutos
```

También abre:

```txt
content/daily/YYYY-MM-DD/03_visual-briefs.md
```

Ese archivo sirve para diseño en Canva, carrusel, imagen o post visual.

---

## Paso 15 — Publicar o programar manualmente

No conectar Facebook todavía.

En fase 1:

```txt
Cursor prepara → equipo revisa → equipo agenda en Facebook
```

Esto evita:

- riesgo de spam;
- errores de publicación;
- problemas de permisos;
- tono incorrecto;
- contenido no revisado.

---

# 9. Fase 2: activar Hooks

## Paso 16 — Esperar 7 días de outputs estables

No actives hooks desde el día 1.

Primero valida que:

- el output sale diario;
- las fuentes son buenas;
- los posts son útiles;
- el tono es correcto;
- los scores tienen sentido;
- no hay repetición excesiva.

Después de 7 días, activar Hooks.

---

## Paso 17 — Revisar Hooks

Archivos:

```txt
.cursor/hooks.json
.cursor/hooks.example.json
.cursor/skills/wmnmx-daily-content-automation/scripts/validate_daily_output.py
```

Primero revisa:

```txt
.cursor/hooks.example.json
```

Luego valida si el schema exacto de tu versión de Cursor coincide.

Después activa:

```txt
.cursor/hooks.json
```

El Hook debe generar:

```txt
content/daily/YYYY-MM-DD/08_hook-validation.md
```

---

## Paso 18 — Qué debe revisar el Hook

El Hook debe validar:

```txt
- existen los 7 archivos diarios
- cada post tiene hook
- cada post tiene explicación
- cada post tiene acción práctica
- cada post tiene pregunta
- hay fuentes usadas
- no hay fuentes prohibidas
- cada score es mínimo 24/30
- el output final está en español
- los términos digitales clave están explicados
```

Regla:

```txt
El Hook no publica.
El Hook no reescribe creativamente.
El Hook valida y reporta.
```

---

# 10. Fase 3: mejorar la base editorial

Cuando el sistema esté funcionando, puedes evolucionarlo.

## Opción A — Supabase

Usarlo para guardar:

- histórico de posts;
- scores;
- fuentes usadas;
- temas repetidos;
- preguntas frecuentes;
- métricas de performance.

No hacerlo en fase 1.  
Primero Markdown en repo. Luego base de datos.

---

## Opción B — Google Sheets / Airtable / Notion

Usarlo para calendario editorial.

Flujo futuro:

```txt
Cursor genera posts
→ los manda a calendario
→ equipo aprueba
→ equipo publica
```

---

## Opción C — Meta MCP / Facebook

No usar en fase 1.

Solo considerar después de:

```txt
7 a 14 días de output estable
permisos claros
política clara
revisión de riesgos
cero riesgo de spam
```

---

# 11. Checklist de montaje

Antes de correr la Automation, confirma:

```txt
[ ] ZIP descomprimido
[ ] Carpeta wmnmx-content-engine abierta en Cursor
[ ] Rules detectadas
[ ] Skills detectadas
[ ] Subagents detectados
[ ] Web Search ON
[ ] Web Fetch ON
[ ] Chrome DevTools MCP ON
[ ] context7 ON
[ ] sequential-thinking ON
[ ] meta-mcp OFF
[ ] mercadopago-mcp-server OFF
[ ] Repository seleccionado en Automation
[ ] Trigger Scheduled configurado
[ ] Prompt maestro pegado
[ ] Memories agregadas
[ ] Test-run ejecutado
[ ] Output revisado
[ ] Quality Gate revisado
[ ] Automation activada
```

---

# 12. Checklist diario de operación

Cada mañana:

```txt
[ ] Revisar content/daily/YYYY-MM-DD/
[ ] Abrir 02_posts-ready.md
[ ] Abrir 03_visual-briefs.md
[ ] Revisar 04_sources-used.json
[ ] Revisar 06_quality-score.md
[ ] Revisar 07_editorial-notes.md
[ ] Editar si hace falta
[ ] Diseñar visual si aplica
[ ] Programar manualmente en Facebook
```

---

# 13. Checklist de seguridad editorial

Antes de publicar cualquier post:

```txt
[ ] No hay fuente dudosa
[ ] No hay miedo barato
[ ] No hay tono condescendiente
[ ] No hay promesas exageradas
[ ] No hay tecnicismos sin explicar
[ ] No hay claims financieros delicados sin fuente
[ ] No hay instrucciones peligrosas
[ ] No hay contenido de privacidad sensible
[ ] El post tiene acción clara
[ ] El post tiene pregunta fácil
```

---

# 14. Qué hacer si algo falla

## No aparecen las Rules

Revisa que estén aquí:

```txt
.cursor/rules/
```

Y que tengan extensión:

```txt
.mdc
```

---

## No aparecen las Skills

Revisa que cada Skill tenga su propio folder y archivo:

```txt
.cursor/skills/nombre-de-skill/SKILL.md
```

---

## No aparecen los Subagents

Revisa que estén aquí:

```txt
.cursor/agents/
```

Y que cada archivo tenga frontmatter YAML al inicio.

---

## La Automation no escribe archivos

Revisa:

```txt
Repository: wmnmx-content-engine
```

No debe estar en `No Repository`.

---

## El output sale en inglés

Revisa:

```txt
.cursor/rules/wmnmx-translation-policy.mdc
prompts/automation-master.md
prompts/test-run.md
```

Todos indican que el output final debe estar en español.

---

## Las fuentes son débiles

Revisa:

```txt
sources/allowlist.yml
sources/rejected-sources.yml
.cursor/rules/wmnmx-source-policy.mdc
```

Ajusta la allowlist.

---

## Los posts suenan genéricos

Revisa:

```txt
.cursor/rules/wmnmx-editorial-voice.mdc
templates/
```

Pide al agente que reescriba con más contexto mexicano y más acción práctica.

---

# 15. Recomendación final de implementación

No actives todo al mismo tiempo.

Secuencia recomendada:

```txt
Día 1:
Montar repo + revisar Rules, Skills y Subagents.

Día 2:
Correr test-run.

Día 3:
Ajustar tono, fuentes y plantillas.

Día 4:
Correr segundo test-run.

Día 5:
Crear Automation scheduled apagada.

Día 6:
Encender Automation y revisar output.

Día 7:
Publicar manualmente los primeros contenidos revisados.

Día 8 a 14:
Medir consistencia.

Después:
Activar Hooks.
```

La verdad cruda: si intentas conectar todo —Facebook, Meta MCP, Supabase, Hooks y publicación automática— desde el día uno, el sistema se puede volver frágil.

El MVP correcto es:

```txt
Rules + Skills + Subagents + Automation + revisión humana
```

Cuando eso funcione, metemos Hooks.  
Cuando Hooks funcione, metemos base editorial.  
Cuando la base editorial funcione, evaluamos Meta.

---

# 16. Resultado esperado

Si lo montas bien, cada día tendrás un paquete editorial con:

```txt
1 post de señal verificada
1 post de explicación simple
1 reto de 10 minutos
3 briefs visuales
fuentes usadas
fuentes rechazadas
score de calidad
notas editoriales
```

Eso convierte Cursor en una máquina editorial de confianza para WMNMX.

No es solo automatización.  
Es una infraestructura de crecimiento comunitario.

**Love Academy**  
*Siente Más*
