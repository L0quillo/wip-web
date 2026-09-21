# WIP Bolivia — Base de Conocimiento y Mapa Maestro del Proyecto

> **Propósito del documento:** Este archivo sirve como memoria técnica, mapa de arquitectura y registro histórico (Changelog) para desarrolladores y agentes de inteligencia artificial (Antigravity, Codex, Claude, etc.). Contiene la descripción de todas las carpetas, el estado de la web, las convenciones de despliegue en cPanel/WHM y el flujo de trabajo en Git.

---

## 🗺️ 1. Mapa Completo de Directorios del Workspace

| Carpeta / Archivo | Tipo | Descripción y Propósito | Estado / Reglas |
| :--- | :--- | :--- | :--- |
| **`sitio-web-actual/`** | **Sitio Web Desplegable** | Contiene el código fuente en producción (`wip-new/`) y archivos de redirección (`redirect-root/`). | **Producción.** Se despliega directamente en cPanel (`public_html/` y `public_html/wip-new/`). |
| **`lineamientos-y-recursos-corporativos/`** | **Identidad & Negocio B2B** | Identidad visual corporativa, paletas de color, manuales de marca, plantillas de propuestas comerciales B2B y modelos de cotización técnica. | **Material protegido.** Consultar para mantener tono de voz y estilo. |
| **`FLOW-FERIA-WIP/`** | **Marketing & Audiovisual** | Videos corporativos, renders 3D de stands, banners y presentaciones para ferias industriales. | **Material audiovisual.** |
| **`documentacion-tecnica-y-propuestas/`** | **Documentación & Insumos** | Manifiestos de arquitectura, fichas técnicas de Arauterm/WebServi, diagramas de ingeniería y brochures de telemetría. | **Referencia técnica.** |
| **`historico-web-fuentes-2022/`** | **Fuentes Históricas** | Fichas técnicas, planos, fotografías originales de obras de WIP (plantas PPA/PTAR, filtros serie P, montajes de vapor) y respaldo de la web 2022. | **Solo lectura.** Fuente original de imágenes y datos. |
| **`.cpanel.yml`** | **Automatización CI/CD** | Script de despliegue automático de cPanel Git Version Control que copia los archivos a `public_html/`. | **Crítico para despliegue.** |
| **`.agents/`, `.claude/`, `agent/`** | **Configuración de IA** | Skills, prompts y herramientas del sistema de agentes (Antigravity/Codex). | **Configuración de agentes.** Conservar. |
| **`README.md`** | **Guía Maestra** | Explicación general para humanos y agentes de IA sobre cómo está organizado todo el proyecto. | **Documentación central.** |

---

## 🌐 2. Arquitectura de la Web (`wip-new/`)

El sitio web está compuesto por **5 Divisiones Maestras de Ingeniería** estructuradas en páginas estáticas ultraligeras:

1. **[`index.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/index.html)**: Home con Hero, barra de homologaciones (NB 512, Ley 1333, ASME), las 5 divisiones industriales, productos destacados, banner de continuidad operativa, formulario de contacto y footer de 4 columnas.
2. **[`tratamiento-agua.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/tratamiento-agua.html)**: Plantas Potabilizadoras PPA, Efluentes PTAR/PDA-I, Ósmosis Inversa Industrial, Ablandadores y Desinfección UV/Ozono.
3. **[`filtros-metalicos.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/filtros-metalicos.html)**: Filtros Serie P para aceite térmico (hasta 15 bar), combustibles Explosion Proof y filtros para polvo/gases.
4. **[`calderas-vapor.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/calderas-vapor.html)** *(Nueva)*:
   - Badge oficial: *"Representantes de Arauterm en Bolivia"*.
   - 4 Familias de Equipos Arauterm: Calderas de Vapor Pirotubulares, Calderas a Biomasa, Calentadores de Fluido Térmico y Generadores de Agua Caliente.
   - Modales interactivos con especificaciones de capacidad, presión y combustible.
   - Galería de montajes reales de WIP (cabezales de vapor a 10 bar / 3 ton/h, manifolds y trampeo).
5. **[`automatizacion-iot.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/automatizacion-iot.html)** *(Nueva)*:
   - 3 Pilares: Telemetría Cloud WebServi, Tableros Eléctricos y Eficiencia Energética.
   - Diagrama de Arquitectura de Datos en 5 Fases (Sensores -> Edge Gateways -> Conectividad Industrial -> Dashboards Cloud -> Alertas WhatsApp/Telegram).
   - Matriz de 6 Variables Críticas Monitoreadas.
   - Protocolo de seguridad industrial (monitoreo en la nube / actuación crítica en hardware local).
6. **[`servicios.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/servicios.html)**: Ingeniería de montajes mecánicos, líneas de vapor/condensado, gas natural y aislamiento refractario.
7. **[`nosotros.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/nosotros.html)**: Identidad, valores, experiencia y cobertura en Bolivia.
8. **[`contacto.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/contacto.html)**: Formulario dinámico B2B con preselección inteligente por URL (`?servicio=`), canales de WhatsApp directo y QR.

---

## 🎨 3. Identidad de Marca y Reglas Comerciales

- **Colores Corporativos:**
  - Primario / Acento: `#C1303A` (Rojo Industrial WIP)
  - Secundario / Corporativo: `#244088` (Azul Ingeniería WIP)
  - Fondo oscuro / Contraste: `#0f172a` / `#1e293b`
  - Fondo claro: `#f8fafc` / `#ffffff`
- **Regla Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (evitar *"exclusivo"* o *"servicio técnico oficial único"*).
- **Regla WebServi:** Presentar la plataforma como socio tecnológico y plataforma de telemetría, manteniendo siempre el canal de contacto comercial de WIP Bolivia (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).

---

## ⚙️ 4. Flujo Git y Despliegue en Servidor (cPanel / WHM)

### Repositorio Central
- **GitHub:** `https://github.com/L0quillo/wip-web.git`
- **Rama principal de producción:** `main`
- **Tag de respaldo histórico:** `v1.0-backup-pre-expansion` (en commit `37b2dbd`).

### Configuración del Servidor en cPanel / WHM
- **Ruta del repositorio en el servidor:** `/home/wipbolivia/repositories/wip-web`
- **Ruta web pública:** `/home/wipbolivia/public_html/` y `/home/wipbolivia/public_html/wip-new/`
- **Permisos requeridos en Linux:** Carpetas `755`, Archivos `644`, Usuario propietario `wipbolivia:wipbolivia`.
- **Despliegue automático (`.cpanel.yml`):**
  ```yaml
  ---
  deployment:
    tasks:
      - export DEPLOYPATH=/home/wipbolivia/public_html
      - /bin/mkdir -p $DEPLOYPATH/wip-new
      - /bin/cp -R -f wip-new/. $DEPLOYPATH/wip-new/
      - /bin/cp -R -f wip-new/. $DEPLOYPATH/
  ```

### Comando rápido para actualizar producción desde la Terminal de WHM:
```bash
cd /home/wipbolivia/repositories/wip-web && git pull origin main && cp -R -f wip-new/. /home/wipbolivia/public_html/wip-new/ && cp -R -f wip-new/. /home/wipbolivia/public_html/
```

---

## 📜 5. Registro Histórico de Cambios (Changelog)

### [Fase 2] — Septiembre 2026: Ampliación con Calderas Arauterm y Automatización IoT
- **Nuevas Páginas:** Creación de `calderas-vapor.html` y `automatizacion-iot.html` con modales interactivos y esquemas de arquitectura de datos.
- **Navegación:** Menú superior ampliado con soporte de submenús dropdown en Tratamiento de Agua y Calderas & Vapor; breakpoint de menú móvil ajustado a 1080px.
- **Interacción y Formularios:** `main.js` actualizado para capturar parámetros GET (`?servicio=`) y preseleccionar la opción de cotización.
- **Optimización de Assets:** Inclusión de imágenes oficiales Arauterm y nuevo Dashboard WebServi en alta resolución (`WEBSERVI-DASHBOARD-IOT.jpeg`).
- **Seguridad & Despliegue:** Creación de ramas y tags de respaldo en Git, sincronización con GitHub y optimización de `.cpanel.yml` para despliegue simultáneo en raíz y subcarpeta.

### [Fase 1] — Versión Base: Tratamiento de Agua, Filtros y Montajes
- Estructuración inicial de `wip-new/` con páginas de Tratamiento de Agua, Filtros Metálicos, Servicios de Montaje, Nosotros y Contacto con PHP mailer.
