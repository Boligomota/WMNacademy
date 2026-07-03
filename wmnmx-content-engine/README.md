# WMNMX Content Engine

Sistema editorial automatizado para **WMNMX**, un grupo privado de Facebook para mujeres +40 en México enfocado en adopción tecnológica, seguridad digital, IA, productividad, reinvención profesional y social commerce.

Este repositorio está diseñado para funcionar en Cursor con:

- **Rules**: política editorial persistente.
- **Skills**: manuales operativos y workflows reutilizables.
- **Subagents**: investigadores especializados.
- **MCP**: conexión controlada a herramientas externas.
- **Hooks**: validación y logging, fase 2.
- **Automation**: motor programado diario.
- **Memories**: contexto persistente mínimo.
- **Human Review**: última capa de criterio.

## Principio estratégico

Cursor no debe operar como autoposter. Debe operar como una **redacción editorial automatizada con criterio**.

El flujo correcto:

```txt
fuente verificada
→ traducción digital clara
→ utilidad para mujeres +40
→ acción de 10 minutos
→ revisión humana
→ publicación con intención
```

## Instalación en Cursor

1. Abre este folder como workspace en Cursor.
2. Revisa que Cursor detecte:
   - `.cursor/rules/`
   - `.cursor/skills/`
   - `.cursor/agents/`
3. En Cursor, ve a **Rules, Skills, Subagents** y confirma que aparecen las Rules, Skills y Subagents del proyecto.
4. En **Automations**, crea una nueva Automation.
5. Selecciona este repo como repository: `wmnmx-content-engine`.
6. Agrega un trigger **Scheduled** a las 6:00 am CDMX.
7. Pega el prompt de `prompts/automation-master.md` en **Agent Instructions**.
8. Guarda la Automation.
9. Configura Memories usando `prompts/memories.md`.
10. Corre primero el prompt de prueba en `prompts/test-run.md`.
11. Revisa el output en `/content/daily/test-run-YYYY-MM-DD/`.
12. Activa la Automation diaria solo cuando el output pase revisión.

## Herramientas recomendadas en Cursor

Fase 1:

- Web Search Tool: ON
- Web Fetch Tool: ON
- Chrome DevTools MCP: ON, solo para verificación puntual
- context7: ON, para documentación técnica actualizada
- sequential-thinking: ON, para scoring y razonamiento de calidad

Mantener fuera del flujo en fase 1:

- meta-mcp
- mercadopago-mcp-server
- supabase como dependencia crítica
- vercel

## Output diario esperado

Cada corrida debe generar:

```txt
/content/daily/YYYY-MM-DD/
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

## Importante

- No publicar directamente en Facebook.
- No conectar Facebook en fase 1.
- No scrapear grupos privados, paywalls, páginas con login ni fuentes restringidas.
- El output final debe estar en español claro, sencillo y contextual para mujeres +40 en México.
- Mantener términos digitales clave en inglés cuando sean necesarios para alfabetización digital, explicándolos de inmediato en español.

**Love Academy**  
*Siente Más*
