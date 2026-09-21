# 🏭 WIP Soluciones Integrales — Hub Corporativo, Web y Sistema de Agentes

Bienvenido al repositorio central de **WIP Soluciones Integrales** (Santa Cruz, Bolivia).  
Este espacio unifica el sitio web en producción, la identidad corporativa B2B, los activos audiovisuales y de ferias, los insumos históricos de ingeniería y el sistema de agentes de inteligencia artificial.

Si esta carpeta fue compartida, copiada, movida o renombrada, comenzar por [`INICIO-AQUI.md`](INICIO-AQUI.md).

---

## 🧭 1. Guía Rápida de Navegación (Para Humanos)

Si buscas un recurso específico, consulta esta tabla:

| ¿Qué necesitas encontrar o hacer? | Carpeta o Archivo de Destino |
| :--- | :--- |
| 🌐 **Editar o revisar el sitio web en producción** | [`sitio-web-actual/wip-new/`](sitio-web-actual/wip-new/) (HTML5, CSS, JS, PHP - 5 Divisiones) |
| 🚀 **Subir la web al hosting (cPanel)** | Usar **Git Version Control** y `.cpanel.yml`; generar un ZIP de despliegue solo cuando sea necesario |
| 🕘 **Restaurar una versión anterior de la web** | [`respaldos-versiones-web/`](respaldos-versiones-web/) |
| 🎨 **Logos oficiales y Manual de Marca** | [`lineamientos-y-recursos-corporativos/logos/`](lineamientos-y-recursos-corporativos/logos/) y [`lineamientos-y-recursos-corporativos/documentos/`](lineamientos-y-recursos-corporativos/documentos/) |
| 💼 **Plantillas de Propuestas Comerciales B2B** | [`lineamientos-y-recursos-corporativos/ai-skills/Plantillas_Propuestas_Comerciales_B2B.md`](lineamientos-y-recursos-corporativos/ai-skills/Plantillas_Propuestas_Comerciales_B2B.md) |
| 🎬 **Videos corporativos y materiales de feria** | [`produccion-audiovisual-y-ferias/`](produccion-audiovisual-y-ferias/) |
| 📐 **Especificaciones técnicas (Arauterm / WebServi)** | [`documentacion-tecnica-y-propuestas/`](documentacion-tecnica-y-propuestas/) |
| 📷 **Fotos históricas de obras y planos originales 2022** | [`historico-web-fuentes-2022/`](historico-web-fuentes-2022/) |
| 🤖 **Consultar reglas técnicas de agentes de IA** | [`AGENTS.md`](AGENTS.md) y [`PROJECT_KNOWLEDGE_BASE.md`](PROJECT_KNOWLEDGE_BASE.md) |
| 🔄 **Retomar después de mover o renombrar la carpeta** | [`CONTINUIDAD-DEL-PROYECTO.md`](CONTINUIDAD-DEL-PROYECTO.md) |
| 📋 **Dar contexto a un agente nuevo** | [`INICIO-AQUI.md`](INICIO-AQUI.md), con una instrucción lista para copiar y pegar |
| 🗃️ **Saber dónde guardar material nuevo** | [`GOBERNANZA-DE-ARCHIVOS.md`](GOBERNANZA-DE-ARCHIVOS.md) |
| 📋 **Consultar el estado y pendientes** | [`ESTADO-DE-PROYECTOS.md`](ESTADO-DE-PROYECTOS.md) |

---

## 🤖 2. Directrices para Agentes de Inteligencia Artificial (AI Guidelines)

Cualquier agente (Antigravity, Codex, Claude, GPT) que opere en este espacio **debe cumplir obligatoriamente** las siguientes normas:

1. **Lectura obligatoria:** Antes de modificar cualquier archivo, consultar [`PROJECT_KNOWLEDGE_BASE.md`](PROJECT_KNOWLEDGE_BASE.md) y [`CONTINUIDAD-DEL-PROYECTO.md`](CONTINUIDAD-DEL-PROYECTO.md) para conocer el estado actual y el mapa de dependencias.
2. **Filosofía Web Ultraligera:** La web en `sitio-web-actual/wip-new/` es **100% nativa** (Vanilla HTML5, CSS3, JavaScript puro y PHP). Está terminantemente prohibido instalar Node.js, frameworks JS pesados o herramientas de compilación que rompan la compatibilidad con cPanel.
3. **Identidad de Marca:**
   - Paleta cromática oficial: `#C1303A` (Rojo Industrial) y `#244088` (Azul Ingeniería).
   - **Regla Arauterm:** La denominación debe ser estrictamente *"Representantes de Arauterm en Bolivia"* (no usar *"exclusivo"* ni *"servicio oficial único"*).
   - **Regla WebServi:** Plataforma de telemetría y socio tecnológico; los canales de contacto y cotización siempre pertenecen a WIP Bolivia (`comercial@wipbolivia.com` y WhatsApp `+591 70057895`).
4. **Protección de Fuentes Históricas:** La carpeta `historico-web-fuentes-2022/` es de **solo lectura**. No borrar ni sobreescribir planos ni fotos originales.
5. **Entorno de Skills:** Conservar `.agents/skills/`, `skills-lock.json`, `.claude/` y `agent/`.
6. **Respaldo web previo:** Antes de editar `sitio-web-actual/`, ejecutar `scripts/crear-respaldo-web.ps1 -Motivo "descripcion-breve"`. No comenzar la edición hasta comprobar el ZIP, `.sha256` y `.txt` resultantes.

---

## 🏗️ 3. Estructura del Árbol de Carpetas

```text
├── sitio-web-actual/                    # 🌐 SITIO WEB EN PRODUCCIÓN (5 Divisiones)
│   ├── wip-new/                         # Código fuente en producción
│   │   ├── index.html                   # Home con catálogo y cotizador
│   │   ├── tratamiento-agua.html        # División 1: Plantas PPA/PTAR, Ósmosis, Ablandadores
│   │   ├── filtros-metalicos.html       # División 2: Filtros Serie P, Combustibles, Gases
│   │   ├── calderas-vapor.html          # División 3: Arauterm (Vapor, Biomasa, Térmico)
│   │   ├── automatizacion-iot.html      # División 4: WebServi IoT (Telemetría y Control)
│   │   ├── servicios.html               # División 5: Montajes de Vapor, Gas y Refractarios
│   │   ├── nosotros.html                # Historia, visión y presencia en Bolivia
│   │   ├── contacto.html                # Formulario dinámico B2B
│   │   ├── send-contact.php             # Receptor de correos a comercial@wipbolivia.com
│   │   └── assets/                      # CSS, JS e imágenes optimizadas
│   └── redirect-root/                   # Archivos de redirección para la raíz
│
├── lineamientos-y-recursos-corporativos/# 🏢 IDENTIDAD, MARCA Y ESTRATEGIA B2B
│   ├── ai-skills/                       # Plantillas y prompts para propuestas comerciales B2B
│   ├── documentos/                      # Manual de identidad y estrategia en PDF/Word/MD
│   ├── logos/                           # Vectoriales y variantes oficiales de WIP
│   └── scripts/                         # Utilidades Python (build_corporate_docs.py)
│
├── produccion-audiovisual-y-ferias/     # 🎬 BIBLIOTECA AUDIOVISUAL Y DE FERIAS
│   └── video-feria-google-flow-2026/    # Proyecto Flow: prompts, clips, entregables y QA
│
├── documentacion-tecnica-y-propuestas/  # 📚 ARQUITECTURA Y ESPECIFICACIONES TÉCNICAS
│   ├── documentacion-ampliacion-web-2026 # Memoria de Calderas, IoT y Centro de Recursos
│   └── insumos-tecnicos-ingenieria      # Diagramas de flujo y brochures PDF de ingeniería
│
├── historico-web-fuentes-2022/          # 📦 FUENTES HISTÓRICAS Y BANCO DE FOTOS ORIGINALES
│   ├── 2. TRATAMIENTO DE AGUA/          # Fichas y fotos originales de plantas
│   ├── 3. FILTROS METALICOS/            # Planos y fotos originales de carcasas
│   ├── 13. SERVICIOS/                   # Fotos de cabezales y montajes de vapor
│   ├── imagenes-historicas/             # Renders y logos preliminares de 2022
│   └── wip-backup-pre-divisiones.zip    # Respaldo ZIP de la web previa
│
├── respaldos-versiones-web/             # 🕘 VERSIONES COMPLETAS PREVIAS A CADA CAMBIO WEB
├── scripts/                              # 🔧 Utilidades repetibles, incluido el respaldo web
├── .cpanel.yml                          # ⚙️ Script de despliegue automatizado cPanel CI/CD
├── INICIO-AQUI.md                        # 📋 Entrada portable y prompt para cualquier agente
├── CONTINUIDAD-DEL-PROYECTO.md          # 🔄 Memoria portable para futuros agentes y ubicaciones
├── GOBERNANZA-DE-ARCHIVOS.md            # 🗃️ Dónde guardar cada tipo de material nuevo
└── PROJECT_KNOWLEDGE_BASE.md            # 📜 Base de conocimiento completa y Changelog
```

---

## ⚡ 4. Despliegue en Servidor de Producción (cPanel / Git)

### Forma 1: Desde cPanel con Git Version Control (Recomendado para cualquier usuario)
1. Entra a tu **cPanel** > **Git Version Control**.
2. En la pestaña **Pull or Deploy**, haz clic en **Update from Remote**.
3. Haz clic en **Deploy HEAD Commit**. *(cPanel ejecutará `.cpanel.yml` y actualizará los archivos sin necesidad de acceso root)*.

### Forma 2: Con un ZIP de despliegue generado expresamente
1. Comprime el contenido vigente de `sitio-web-actual/wip-new/` como `wip-new.zip`.
2. Sube el paquete a `public_html/wip-new/` (o `public_html/`) y extráelo.

Los archivos de `respaldos-versiones-web/` son copias de restauración y no deben confundirse con paquetes preparados para despliegue.

---
*Mantenido por el equipo de Ingeniería y Tecnología de WIP Soluciones Integrales.*
