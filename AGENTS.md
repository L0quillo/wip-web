# WIP Bolivia — instrucciones compartidas para agentes

## Memoria del Proyecto y Base de Conocimiento
- Empezar por [`INICIO-AQUI.md`](INICIO-AQUI.md) cuando el proyecto provenga de una carpeta compartida, una copia completa o una nueva ubicación.
- Consultar siempre [`PROJECT_KNOWLEDGE_BASE.md`](PROJECT_KNOWLEDGE_BASE.md) para conocer el mapa exhaustivo de directorios, especificaciones técnicas de las divisiones y el historial de cambios.
- Si la carpeta fue movida, renombrada o abierta como un proyecto nuevo, leer también [`CONTINUIDAD-DEL-PROYECTO.md`](CONTINUIDAD-DEL-PROYECTO.md). Usar siempre rutas relativas y no asumir una ubicación fija en el equipo.

## Carpeta compartida y portabilidad
- El proyecto debe poder utilizarse directamente desde una carpeta sincronizada de Drive/OneDrive o mediante copia completa.
- No crear dependencias en rutas absolutas, accesos directos, enlaces simbólicos ni archivos ubicados fuera de la raíz.
- Los archivos excluidos de Git —videos, ZIP, documentos corporativos e históricos— siguen siendo parte del proyecto compartido y deben conservarse en Drive.
- Antes y después de operaciones grandes, comprobar que la sincronización haya terminado. Evitar ediciones simultáneas del mismo archivo por varios agentes.

## Compatibilidad
- Este proyecto se trabaja con Antigravity y Codex. Mantener compatibles ambos entornos.
- `.agents/skills/` es la fuente existente de habilidades del proyecto. No moverla, renombrarla ni reescribirla.
- Conservar `skills-lock.json`, `.claude/skills/` y `agent/skills/`.

## Mapa del Proyecto
- **`sitio-web-actual/`**: Contiene el sitio web desplegable en producción (`wip-new/` con sus 5 divisiones) y archivos de redirección (`redirect-root/`).
- **`lineamientos-y-recursos-corporativos/`**: Identidad visual corporativa, documentos comerciales, manuales de marca y plantillas de propuestas B2B.
- **`produccion-audiovisual-y-ferias/`**: Biblioteca neutral de proyectos audiovisuales, videos corporativos y materiales para ferias. Cada campaña vive en una subcarpeta propia.
- **`documentacion-tecnica-y-propuestas/`**: Manifiestos de arquitectura, fichas técnicas de Arauterm/WebServi e insumos técnicos de ingeniería.
- **`historico-web-fuentes-2022/`**: Archivos y fotografías históricas originales de productos y obras de WIP (2022) y respaldo de la versión previa.
- **`respaldos-versiones-web/`**: Copias completas, fechadas e inmutables del sitio antes de cada modificación.
- **`.cpanel.yml`**: Configuración de despliegue automático de cPanel Git Version Control.
- **`README.md`**: Guía maestra para humanos e IA sobre cómo está organizado todo el espacio.

## Reglas de Marca y Comerciales
- **Identidad:** Paleta `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería). Mantener estética técnica y sobria.
- **Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (evitar *"exclusivo"*).
- **WebServi:** Plataforma tecnológica aliada para telemetría; los canales de contacto comercial primarios son de WIP (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).

## Convenciones Técnicas y Despliegue
- **Arquitectura:** HTML/CSS/JS nativo sin dependencias ni procesos de compilación (npm/Node).
- **Respaldo previo obligatorio:** Antes de modificar cualquier archivo dentro de `sitio-web-actual/`, ejecutar `scripts/crear-respaldo-web.ps1 -Motivo "descripcion-breve"` y comprobar que existan el ZIP, `.sha256` y `.txt` en `respaldos-versiones-web/`. El respaldo debe crearse antes de la primera edición, incluir toda la carpeta `sitio-web-actual/` y nunca sobrescribirse ni eliminarse automáticamente. Si la tarea es solo lectura o análisis, no crear respaldo.
- **Git:** Repositorio en GitHub `https://github.com/L0quillo/wip-web.git`, rama `main`.
- **Servidor (cPanel / WHM):** Permisos `755` en carpetas, `644` en archivos, usuario `wipbolivia:wipbolivia`.
- **Comando de despliegue en servidor:**
  ```bash
  cd /home/wipbolivia/repositories/wip-web && git pull origin main && cp -R -f sitio-web-actual/wip-new/. /home/wipbolivia/public_html/wip-new/ && cp -R -f sitio-web-actual/wip-new/. /home/wipbolivia/public_html/
  ```
