# Instalación paso a paso en Cursor

## 1. Abrir el repo

Abre `wmnmx-content-engine` como workspace en Cursor.

## 2. Confirmar Rules, Skills y Subagents

Ve a:

```txt
Settings → Rules, Skills, Subagents
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

- `wmnmx-digital-safety`
- `wmnmx-ai-productivity`
- `wmnmx-social-commerce`

## 3. Ajustar Tools & MCPs

Recomendado fase 1:

- Web Search Tool: ON
- Web Fetch Tool: ON
- Chrome DevTools MCP: ON
- context7: ON
- sequential-thinking: ON

Mantener fuera del flujo:

- meta-mcp
- mercadopago-mcp-server
- supabase como dependencia crítica
- vercel

## 4. Crear Automation

Ve a:

```txt
Automations → New Automation
```

Configura:

- Repository: `wmnmx-content-engine`
- Trigger: Scheduled
- Time: 6:00 am CDMX
- Agent Instructions: pega el contenido de `prompts/automation-master.md`

No conectar Facebook.
No activar publicación directa.

## 5. Agregar Memories

Después de guardar la Automation, agrega las Memories de:

```txt
prompts/memories.md
```

## 6. Test manual

Antes de activar, corre el prompt de:

```txt
prompts/test-run.md
```

Revisa:

```txt
/content/daily/test-run-YYYY-MM-DD/
```

## 7. Activar Automation

Solo activar cuando el output sea consistente y útil.

## 8. Hooks fase 2

El archivo `.cursor/hooks.json` está como placeholder seguro.

Cuando la automatización produzca outputs confiables durante 7 días, revisa `.cursor/hooks.example.json`, valida el schema exacto de tu versión de Cursor y activa el hook de validación.
