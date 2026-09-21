# WIP Bolivia — Instrucciones para Gemini / Antigravity

## Memoria del Proyecto y Base de Conocimiento
- Consultar siempre [`PROJECT_KNOWLEDGE_BASE.md`](PROJECT_KNOWLEDGE_BASE.md) y [`CONTINUIDAD-DEL-PROYECTO.md`](CONTINUIDAD-DEL-PROYECTO.md) para conocer el mapa, el estado y el procedimiento de continuidad.
- Activar el skill [`wip-bolivia`](.agents/skills/wip-bolivia/SKILL.md) para tareas de ingeniería, web, audiovisual o comercial.
- La carpeta raíz puede cambiar de nombre o ubicación. Usar rutas relativas y no guardar dependencias de la ruta local.

## Mapa del Proyecto
- **`sitio-web-actual/`**: Contiene el sitio web desplegable en producción (`wip-new/` con sus 5 divisiones) y archivos de redirección (`redirect-root/`).
- **`lineamientos-y-recursos-corporativos/`**: Identidad visual corporativa, documentos comerciales, manuales de marca y plantillas de propuestas B2B.
- **`produccion-audiovisual-y-ferias/`**: Biblioteca de proyectos audiovisuales y materiales de feria. El proyecto histórico de Google Flow está en `video-feria-google-flow-2026/`.
- **`documentacion-tecnica-y-propuestas/`**: Manifiestos de arquitectura, fichas técnicas de Arauterm/WebServi e insumos técnicos de ingeniería.
- **`historico-web-fuentes-2022/`**: Archivos y fotografías históricas originales de productos y obras de WIP (2022) y respaldo de la versión previa.
- **`respaldos-versiones-web/`**: Versiones completas, fechadas e inmutables de la web.
- **`.cpanel.yml`**: Configuración de despliegue automático de cPanel Git Version Control.
- **`README.md`**: Guía maestra para humanos e IA sobre cómo está organizado todo el espacio.

## Reglas de Marca y Comerciales
- **Identidad:** Paleta `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería). Mantener estética técnica y sobria.
- **Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (evitar *"exclusivo"*).
- **WebServi:** Plataforma tecnológica aliada para telemetría; los canales de contacto comercial primarios son de WIP (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).

## Convenciones Técnicas y Despliegue
- **Arquitectura:** HTML/CSS/JS nativo sin dependencias ni procesos de compilación (npm/Node).
- **Respaldo previo obligatorio:** Antes de editar cualquier archivo dentro de `sitio-web-actual/`, ejecutar `scripts/crear-respaldo-web.ps1 -Motivo "descripcion-breve"` y comprobar el ZIP, `.sha256` y `.txt`. No sobrescribir ni borrar respaldos; las tareas de solo lectura no requieren uno.
- **Git:** Repositorio en GitHub `https://github.com/L0quillo/wip-web.git`, rama `main`.
- **Servidor (cPanel / WHM):** Permisos `755` en carpetas, `644` en archivos, usuario `wipbolivia:wipbolivia`.
- **Comando de despliegue en servidor:**
  ```bash
  cd /home/wipbolivia/repositories/wip-web && git pull origin main && cp -R -f sitio-web-actual/wip-new/. /home/wipbolivia/public_html/wip-new/ && cp -R -f sitio-web-actual/wip-new/. /home/wipbolivia/public_html/
  ```
