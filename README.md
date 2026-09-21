# 🏭 WIP Soluciones Integrales — Hub Corporativo, Web y Sistema de Agentes

Bienvenido al repositorio central de **WIP Soluciones Integrales** (Santa Cruz, Bolivia).  
Este espacio unifica el sitio web en producción, la identidad corporativa B2B, los activos de marketing para ferias, los insumos históricos de ingeniería y el sistema de agentes de inteligencia artificial.

---

## 🧭 1. Guía Rápida de Navegación (Para Humanos)

Si buscas un recurso específico, consulta esta tabla:

| ¿Qué necesitas encontrar o hacer? | Carpeta o Archivo de Destino |
| :--- | :--- |
| 🌐 **Editar o revisar el sitio web en producción** | [`wip-new/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/) (HTML5, CSS, JS, PHP) |
| 🚀 **Subir la web al hosting (cPanel)** | [`wip-new/README-DEPLOY.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new/README-DEPLOY.md) o usar [`wip-new.zip`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/wip-new.zip) |
| 🎨 **Logos oficiales y Manual de Marca** | [`corporativo/logos/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/corporativo/logos/) y [`corporativo/documentos/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/corporativo/documentos/) |
| 💼 **Plantillas de Propuestas Comerciales B2B** | [`corporativo/ai-skills/Plantillas_Propuestas_Comerciales_B2B.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/corporativo/ai-skills/Plantillas_Propuestas_Comerciales_B2B.md) |
| 🎪 **Gráficas, banners y presentaciones para ferias** | [`FLOW-FERIA-WIP/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/FLOW-FERIA-WIP/) |
| 📐 **Especificaciones técnicas (Arauterm / WebServi)** | [`documentacion-y-propuestas/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/documentacion-y-propuestas/) |
| 📷 **Fotos históricas de obras y planos originales 2022** | [`historico-web-fuentes-2022/`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/historico-web-fuentes-2022/) |
| 🤖 **Consultar reglas técnicas de agentes de IA** | [`AGENTS.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/AGENTS.md) y [`PROJECT_KNOWLEDGE_BASE.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/PROJECT_KNOWLEDGE_BASE.md) |

---

## 🤖 2. Directrices para Agentes de Inteligencia Artificial (AI Guidelines)

Cualquier agente (Antigravity, Codex, Claude, GPT) que opere en este espacio **debe cumplir obligatoriamente** las siguientes normas:

1. **Lectura obligatoria:** Antes de modificar cualquier archivo, consultar [`PROJECT_KNOWLEDGE_BASE.md`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/PROJECT_KNOWLEDGE_BASE.md) para conocer el estado actual y el mapa de dependencias.
2. **Filosofía Web Ultraligera:** La web en `wip-new/` es **100% nativa** (Vanilla HTML5, CSS3, JavaScript puro y PHP). Está terminantemente prohibido instalar Node.js, frameworks JS pesados o herramientas de compilación que rompan la compatibilidad con cPanel.
3. **Identidad de Marca:**
   - Paleta cromática oficial: `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería).
   - **Regla Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (no usar *"exclusivo"* ni *"servicio oficial único"*).
   - **Regla WebServi:** Plataforma de telemetría y socio tecnológico; los canales de contacto y cotización siempre pertenecen a WIP Bolivia (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).
4. **Protección de Fuentes Históricas:** La carpeta `historico-web-fuentes-2022/` es de **solo lectura**. No borrar ni sobreescribir planos ni fotos originales.
5. **Entorno de Skills:** Conservar `.agents/skills/`, `skills-lock.json`, `.claude/` y `agent/`.

---

## 🏗️ 3. Estructura del Árbol de Carpetas

```text
├── wip-new/                             # 🌐 SITIO WEB EN PRODUCCIÓN (5 Divisiones de Ingeniería)
│   ├── index.html                       # Home principal con catálogo y formulario
│   ├── tratamiento-agua.html            # División 1: Plantas PPA/PTAR, Ósmosis, Ablandadores
│   ├── filtros-metalicos.html           # División 2: Filtros Serie P, Combustibles, Gases
│   ├── calderas-vapor.html              # División 3: Arauterm (Vapor, Biomasa, Fluido Térmico)
│   ├── automatizacion-iot.html          # División 4: WebServi IoT (Telemetría y Control)
│   ├── servicios.html                   # División 5: Montajes de Vapor, Gas y Refractarios
│   ├── nosotros.html                    # Historia, visión y presencia en Bolivia
│   ├── contacto.html                    # Formulario de cotización con autoselección
│   ├── send-contact.php                 # Procesador de correo para comercial@wipbolivia.com
│   └── assets/                          # CSS, JS, imágenes optimizadas y branding
│
├── corporativo/                         # 🏢 IDENTIDAD, MARCA Y ESTRATEGIA B2B
│   ├── ai-skills/                       # Plantillas y prompts para propuestas comerciales
│   ├── documentos/                      # Manual de identidad y estrategia en PDF/Word/MD
│   ├── logos/                           # Vectoriales y variantes de logos de WIP
│   └── scripts/                         # Utilidades Python (build_corporate_docs.py)
│
├── FLOW-FERIA-WIP/                      # 🎪 MARKETING, FERIAS INDUSTRIALES Y EVENTOS
│   ├── assets/, renders/                # Modelados 3D de stands y gigantografías
│   └── lineamientos y prompts           # Instrucciones para ferias y stands B2B
│
├── documentacion-y-propuestas/          # 📚 ARQUITECTURA Y ESPECIFICACIONES TÉCNICAS
│   ├── propuesta-ampliacion-antigravity # Manifiestos y fichas técnicas Arauterm/WebServi
│   └── insumos-tecnicos-ingenieria      # Diagramas de flujo y brochures PDF de ingeniería
│
├── historico-web-fuentes-2022/          # 📦 FUENTES HISTÓRICAS Y BANCO DE FOTOS ORIGINALES
│   ├── 2. TRATAMIENTO DE AGUA/          # Fichas y fotos originales de plantas
│   ├── 3. FILTROS METALICOS/            # Planos y fotos originales de carcasas
│   ├── 13. SERVICIOS/                   # Fotos de cabezales y montajes de vapor
│   ├── imagenes-historicas/             # Renders y logos preliminares de 2022
│   └── wip-backup-pre-divisiones.zip    # Respaldo ZIP de la web antes de la fase de calderas
│
├── redirect-root/                       # 🔀 Redirección para la raíz del hosting cPanel
├── .cpanel.yml                          # ⚙️ Script de despliegue automatizado cPanel CI/CD
└── PROJECT_KNOWLEDGE_BASE.md            # 📜 Base de conocimiento completa y Changelog
```

---

## ⚡ 4. Despliegue en Servidor de Producción (cPanel / WHM)

Para actualizar el sitio web en el servidor en vivo:

### Vía Terminal (WHM / SSH):
```bash
cd /home/wipbolivia/repositories/wip-web && git pull origin main && cp -R -f wip-new/. /home/wipbolivia/public_html/wip-new/ && cp -R -f wip-new/. /home/wipbolivia/public_html/
```

### Vía cPanel Git Version Control:
1. En cPanel > **Git Version Control** > **Pull or Deploy**.
2. Haz clic en **Update from Remote**.
3. Haz clic en **Deploy HEAD Commit**.

---
*Mantenido por el equipo de Ingeniería y Tecnología de WIP Soluciones Integrales.*
