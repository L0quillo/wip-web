# Inicio aquí — WIP Soluciones Integrales

Este es el punto de entrada para cualquier persona o agente que reciba la carpeta mediante Drive, OneDrive, una unidad compartida o una copia completa.

## Instrucción lista para copiar y pegar al agente

```text
Trabaja sobre esta carpeta como raíz del proyecto WIP. Antes de hacer cambios, lee completos AGENTS.md, PROJECT_KNOWLEDGE_BASE.md, CONTINUIDAD-DEL-PROYECTO.md, ESTADO-DE-PROYECTOS.md y GOBERNANZA-DE-ARCHIVOS.md. Después lee el README.md del área involucrada y aplica .agents/skills/wip-bolivia/SKILL.md cuando la tarea sea sobre WIP. Usa rutas relativas y no dependas del nombre ni de la ubicación local de la carpeta. No modifiques sitio-web-actual/ si solo te pido analizar u organizar. Antes de cualquier modificación web, crea el respaldo completo obligatorio con scripts/crear-respaldo-web.ps1 y verifica su ZIP, SHA-256 y registro TXT. Conserva compatibilidad con Antigravity, Codex, Claude, Gemini y otros agentes.
```

## Uso directo desde Drive o OneDrive

- Abrir como proyecto la carpeta raíz sincronizada, no una subcarpeta.
- Confirmar que los archivos necesarios estén descargados localmente y no solamente como accesos en línea.
- Esperar a que termine la sincronización antes de mover, renombrar, comprimir, renderizar o cerrar una tarea.
- Evitar que dos agentes o personas editen simultáneamente el mismo archivo.
- No usar accesos directos, enlaces simbólicos o rutas externas como fuente principal de un proyecto.

Un agente local puede trabajar directamente cuando la carpeta compartida está sincronizada o montada en el equipo. Un agente que solo trabaja en navegador necesitará acceso explícito al Drive o una copia de los archivos correspondientes.

## Copia completa a otra ubicación

Copiar la carpeta raíz entera, incluidos archivos ocultos. No basta con copiar solamente lo que Git muestra, porque los videos, respaldos ZIP, documentos corporativos y fuentes históricas se conservan en Drive aunque estén excluidos del repositorio.

Después de copiar, comprobar como mínimo:

- `INICIO-AQUI.md`, `AGENTS.md` y `CONTINUIDAD-DEL-PROYECTO.md`.
- `.git/`, `.agents/`, `.claude/`, `agent/` y `skills-lock.json`.
- `sitio-web-actual/` y `respaldos-versiones-web/`.
- `produccion-audiovisual-y-ferias/` con sus renders y entregables.
- `lineamientos-y-recursos-corporativos/`, `documentacion-tecnica-y-propuestas/` e `historico-web-fuentes-2022/`.

El nombre de la carpeta raíz y su ubicación pueden cambiar. Las rutas internas y las instrucciones están diseñadas para seguir funcionando de forma relativa.
