# WIP Bolivia — instrucciones compartidas para agentes

## Memoria del Proyecto y Base de Conocimiento
- Consultar siempre [`PROJECT_KNOWLEDGE_BASE.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/PROJECT_KNOWLEDGE_BASE.md) para conocer el mapa exhaustivo de directorios, especificaciones técnicas de las divisiones y el historial de cambios (Changelog).

## Compatibilidad
- Este proyecto se trabaja con Antigravity y Codex. Mantener compatibles ambos entornos.
- `.agents/skills/` es la fuente existente de habilidades del proyecto. No moverla, renombrarla ni reescribirla.
- Conservar `skills-lock.json`, `.claude/skills/` y `agent/skills/`.

## Mapa del Proyecto
- **`wip-new/`**: Sitio web desplegable en producción con 5 divisiones (Tratamiento de Agua, Filtros Metálicos, Calderas & Vapor Arauterm, Automatización & IoT WebServi, Servicios & Montajes). HTML5 nativo, CSS3, JS vainilla y PHP.
- **`PROPUESTA-AMPLIACION-WEB-ANTIGRAVITY/`**: Manifiestos de arquitectura, fichas técnicas y propuestas de contenido.
- **`corporativo/`**: Identidad visual corporativa, documentos comerciales y plantillas de propuestas B2B.
- **`2. TRATAMIENTO DE AGUA/`, `3. FILTROS METALICOS/`, `13. SERVICIOS/`**: Archivos y fotografías históricas originales de productos y obras de WIP.
- **`FLOW-FERIA-WIP/`**: Material gráfico para ferias industriales y eventos.
- **`datos adicionales a reacomodar e interpretar/`**: Banco de insumos técnicos y diagramas aportados por ingeniería.
- **`redirect-root/`**: Archivos de redirección para la raíz del hosting hacia `/wip-new/index.html`.
- **`.cpanel.yml`**: Configuración de despliegue automático de cPanel Git Version Control.

## Reglas de Marca y Comerciales
- **Identidad:** Paleta `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería). Mantener estética técnica y sobria.
- **Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (evitar *"exclusivo"*).
- **WebServi:** Plataforma tecnológica aliada para telemetría; los canales de contacto comercial primarios son de WIP (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).

## Convenciones Técnicas y Despliegue
- **Arquitectura:** HTML/CSS/JS nativo sin dependencias ni procesos de compilación (npm/Node).
- **Git:** Repositorio en GitHub `https://github.com/L0quillo/wip-web.git`, rama `main`.
- **Servidor (cPanel / WHM):** Permisos `755` en carpetas, `644` en archivos, usuario `wipbolivia:wipbolivia`.
- **Comando de despliegue en servidor:**
  ```bash
  cd /home/wipbolivia/repositories/wip-web && git pull origin main && cp -R -f wip-new/. /home/wipbolivia/public_html/wip-new/ && cp -R -f wip-new/. /home/wipbolivia/public_html/
  ```
