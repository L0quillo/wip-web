# Continuidad del proyecto WIP

Este documento permite retomar el proyecto después de mover o renombrar la carpeta, cambiar de equipo, compartirla mediante Drive/OneDrive o abrir una tarea nueva con otro agente. Toda la información usa rutas relativas al directorio raíz.

## Cómo retomar el trabajo

1. Abrir como proyecto la carpeta raíz que contiene este archivo, `AGENTS.md` y `.git/`.
2. Pedir al agente que lea, en este orden: `AGENTS.md`, `PROJECT_KNOWLEDGE_BASE.md`, `ESTADO-DE-PROYECTOS.md`, `GOBERNANZA-DE-ARCHIVOS.md` y el `README.md` del área que se trabajará.
3. Para tareas WIP, aplicar `.agents/skills/wip-bolivia/SKILL.md` sin mover las copias compatibles de `.claude/skills/` y `agent/skills/`.
4. Revisar `git status` antes de editar. La reorganización documentada en septiembre de 2026 puede aparecer como archivos movidos mientras no se haya confirmado mediante un commit.
5. Si se modificará `sitio-web-actual/`, crear primero el respaldo obligatorio indicado en `respaldos-versiones-web/README.md`.

No es necesario reconstruir el proyecto ni crear otra estructura. Si cambia la ruta o el nombre, se debe trasladar la carpeta raíz completa, incluidos `.git/`, `.agents/`, `.claude/`, `agent/`, los ZIP ignorados por Git y los archivos ocultos. Después basta con abrir la nueva ubicación como proyecto en Codex, Antigravity u otro agente. La instrucción inicial reutilizable está en `INICIO-AQUI.md`.

## Funcionamiento como carpeta compartida

- La carpeta compartida es la biblioteca completa; Git protege el historial del código y la documentación, pero no reemplaza los archivos grandes que se conservan en Drive.
- Antes de una copia completa, marcar la carpeta como disponible sin conexión o confirmar que todos los archivos estén descargados.
- No trasladar archivos mientras OneDrive/Drive esté sincronizando ni mientras un video o documento esté abierto.
- Si dos personas o agentes trabajan al mismo tiempo, asignar carpetas o archivos distintos. No aceptar automáticamente copias de conflicto como versión canónica.
- Los nombres internos deben ser estables y descriptivos; el nombre de la carpeta raíz puede cambiar libremente.
- No depender de rutas absolutas del tipo `C:\Users\...`; cualquier referencia interna nueva debe ser relativa a la raíz.

## Memoria consolidada de los trabajos

### Organización general

- La fuente vigente de la web está en `sitio-web-actual/wip-new/` y las redirecciones en `sitio-web-actual/redirect-root/`.
- La identidad, logos y plantillas comerciales están en `lineamientos-y-recursos-corporativos/`.
- Las propuestas y referencias técnicas están en `documentacion-tecnica-y-propuestas/`.
- Los originales históricos permanecen en `historico-web-fuentes-2022/` y son de solo lectura.
- Los proyectos de video y feria se guardan en `produccion-audiovisual-y-ferias/`, independientemente del agente o herramienta.

### Video corporativo de feria

- Proyecto canónico: `produccion-audiovisual-y-ferias/video-feria-google-flow-2026/`.
- Secuencia verificada: 34 clips numerados del 00 al 33, sin faltantes ni números repetidos.
- Todos los clips comprobados duran 8 segundos, tienen resolución 1280 × 720, 24 fps y pista de audio.
- Hay dos versiones finales en `entregables/`: Master y Liviano.
- Los prompts, referencias, reglas de marca, estado de renders y control de duplicados permanecen dentro del proyecto.
- `FLOW-FERIA-WIP/` es una copia heredada pendiente de retiro por bloqueos previos de OneDrive/Explorador. No debe recibir material nuevo; antes de eliminarla se debe cerrar cualquier archivo abierto y comparar nuevamente con la carpeta canónica.

### Web y propuestas

- La documentación de la ampliación con Calderas & Vapor y Automatización & IoT está en `documentacion-tecnica-y-propuestas/documentacion-ampliacion-web-2026/`.
- La propuesta del Centro de Recursos para ingenieros permanece pendiente de selección e implementación.
- No modificar la web cuando la tarea sea únicamente de análisis, inventario u organización.

### Respaldos web

- El antiguo `wip-new.zip` fue verificado: contenía los mismos 69 archivos que `sitio-web-actual/wip-new/` en la auditoría del 20 de septiembre de 2026.
- Se conserva como `respaldos-versiones-web/2026-09-20_2123__wip-new-paquete-despliegue.zip`.
- El primer respaldo integral, incluyendo `wip-new/` y `redirect-root/`, es `respaldos-versiones-web/2026-09-20_215310__antes-de-establecer-linea-base-organizada.zip`.
- Los respaldos ZIP están excluidos de Git por tamaño y se conservan mediante el almacenamiento compartido. Los registros `.txt` y las sumas `.sha256` permiten verificar su identidad.

## Estado técnico de continuidad

- Repositorio remoto: `https://github.com/L0quillo/wip-web.git`.
- Rama principal: `main`.
- La URL local del remoto no debe contener usuarios, contraseñas ni tokens; la autenticación corresponde al gestor de credenciales del equipo.
- La web usa HTML, CSS, JavaScript y PHP nativos; no requiere Node.js, npm, base de datos ni proceso de compilación.
- El despliegue se controla mediante `.cpanel.yml`.

## Qué conservar al mover la carpeta

- Toda la carpeta raíz, sin seleccionar solamente los archivos visibles.
- `.git/`, para conservar historial, rama y cambios aún no confirmados.
- `.agents/`, `.claude/`, `agent/` y `skills-lock.json`.
- `respaldos-versiones-web/`, incluso los ZIP ignorados por Git.
- `produccion-audiovisual-y-ferias/`, incluyendo renders y entregables ignorados por Git.
- Los archivos históricos y corporativos ignorados por Git.

Antes de moverla, cerrar el Explorador que esté mostrando videos, editores, servidores locales y aplicaciones que mantengan archivos abiertos; esperar a que OneDrive indique sincronización completa. Después del traslado, comprobar que existan este archivo, `.git/`, `sitio-web-actual/`, los respaldos y los entregables audiovisuales.

Si se comparte mediante una plataforma que omite carpetas ocultas, comprimir primero la carpeta raíz completa o verificar expresamente la inclusión de `.git/`, `.agents/` y `.claude/`. Una copia sin esas carpetas conserva los contenidos, pero pierde parte del historial y de la configuración automática de agentes.
