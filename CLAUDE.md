# WIP Bolivia — Instrucciones para Claude Code / Anthropic

## Guía Rápida y Base de Conocimiento
- Antes de realizar cualquier tarea, consulta [`PROJECT_KNOWLEDGE_BASE.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/PROJECT_KNOWLEDGE_BASE.md) y [`README.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/README.md).
- Usa la skill dedicada [`wip-bolivia`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/.claude/skills/wip-bolivia/SKILL.md).

## Estructura del Proyecto
- **`sitio-web-actual/wip-new/`**: Sitio web en producción (HTML5 nativo, CSS3, JS vainilla y PHP mailer). No introducir Node.js, npm ni frameworks pesados.
- **`FLOW-FERIA-WIP/`**: Producción audiovisual, videos MP4, renders 3D de stands industriales y banners de feria.
- **`lineamientos-y-recursos-corporativos/`**: Manuales de marca, paleta de colores y plantillas comerciales B2B en `ai-skills/`.
- **`documentacion-tecnica-y-propuestas/`**: Especificaciones de calderas Arauterm y telemetría WebServi.
- **`historico-web-fuentes-2022/`**: Fuentes y fotos originales de 2022 (SOLO LECTURA).

## Reglas de Marca
- Colores: `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería).
- **Arauterm:** *"Representantes de Arauterm en Bolivia"* (nunca usar *"exclusivo"*).
- **WebServi:** Plataforma tecnológica aliada de telemetría; los contactos de cotización siempre van a `comercial@wipbolivia.com` y WhatsApp `+591 70057895`.

## Despliegue en Servidor
- Repositorio Git: `https://github.com/L0quillo/wip-web.git`, rama `main`.
- Despliegue automático en cPanel mediante `.cpanel.yml` hacia `/public_html/` y `/public_html/wip-new/`.
