# WIP Bolivia — Instrucciones para Claude Code / Anthropic

## Guía Rápida y Base de Conocimiento
- Antes de realizar cualquier tarea, consulta [`PROJECT_KNOWLEDGE_BASE.md`](PROJECT_KNOWLEDGE_BASE.md), [`CONTINUIDAD-DEL-PROYECTO.md`](CONTINUIDAD-DEL-PROYECTO.md) y [`README.md`](README.md).
- Usa la skill dedicada [`wip-bolivia`](.claude/skills/wip-bolivia/SKILL.md).
- La carpeta raíz puede cambiar de nombre o ubicación. Usar rutas relativas y no guardar dependencias de la ruta local.

## Estructura del Proyecto
- **`sitio-web-actual/wip-new/`**: Sitio web en producción (HTML5 nativo, CSS3, JS vainilla y PHP mailer). No introducir Node.js, npm ni frameworks pesados.
- **`produccion-audiovisual-y-ferias/`**: Biblioteca de proyectos audiovisuales y materiales de feria. El video creado con Google Flow está en `video-feria-google-flow-2026/`.
- **`lineamientos-y-recursos-corporativos/`**: Manuales de marca, paleta de colores y plantillas comerciales B2B en `ai-skills/`.
- **`documentacion-tecnica-y-propuestas/`**: Especificaciones de calderas Arauterm y telemetría WebServi.
- **`historico-web-fuentes-2022/`**: Fuentes y fotos originales de 2022 (SOLO LECTURA).
- **`respaldos-versiones-web/`**: Versiones completas, fechadas e inmutables de la web.

## Respaldo obligatorio antes de modificar la web
- Antes de editar cualquier archivo dentro de `sitio-web-actual/`, ejecutar `scripts/crear-respaldo-web.ps1 -Motivo "descripcion-breve"` y confirmar la creación del ZIP, `.sha256` y `.txt`.
- No sobrescribir ni borrar respaldos. Las tareas de solo lectura no requieren crear uno.

## Reglas de Marca
- Colores: `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería).
- **Arauterm:** *"Representantes de Arauterm en Bolivia"* (nunca usar *"exclusivo"*).
- **WebServi:** Plataforma tecnológica aliada de telemetría; los contactos de cotización siempre van a `comercial@wipbolivia.com` y WhatsApp `+591 70057895`.

## Despliegue en Servidor
- Repositorio Git: `https://github.com/L0quillo/wip-web.git`, rama `main`.
- Despliegue automático en cPanel mediante `.cpanel.yml` hacia `/public_html/` y `/public_html/wip-new/`.
