# Gobernanza de archivos WIP

## Objetivo

Mantener este repositorio como fuente compartida y comprensible para personas y agentes de IA, sin depender de Antigravity, Codex, Claude, Gemini, ChatGPT ni una herramienta específica.

## Fuentes de verdad

| Tema | Ubicación canónica |
|---|---|
| Web en producción | `sitio-web-actual/wip-new/` |
| Redirecciones web | `sitio-web-actual/redirect-root/` |
| Respaldos recuperables de la web | `respaldos-versiones-web/` |
| Marca, logos y plantillas comerciales | `lineamientos-y-recursos-corporativos/` |
| Documentación técnica y decisiones web | `documentacion-tecnica-y-propuestas/` |
| Producción audiovisual y ferias | `produccion-audiovisual-y-ferias/` |
| Fotografías y fuentes históricas | `historico-web-fuentes-2022/` |
| Reglas y memoria general | `AGENTS.md`, `README.md`, `PROJECT_KNOWLEDGE_BASE.md` |

## Dónde guardar materiales nuevos

### Cambios web

- Antes de la primera edición de cualquier tarea, crear un respaldo completo con `scripts/crear-respaldo-web.ps1 -Motivo "descripcion-breve"`.
- Confirmar que el ZIP, su `.sha256` y su registro `.txt` fueron creados correctamente. No reutilizar ni sobrescribir un respaldo anterior.
- Código aprobado: `sitio-web-actual/wip-new/`.
- Propuestas, wireframes y textos no implementados: una subcarpeta fechada dentro de `documentacion-tecnica-y-propuestas/`.
- Recursos optimizados que sí usa la web: `sitio-web-actual/wip-new/assets/`.
- Fuentes originales: nunca dentro del código productivo; conservarlas en histórico, documentación o identidad corporativa.
- Una tarea exclusivamente de lectura o análisis no requiere un respaldo nuevo.

### Retención de respaldos web

- Cada ZIP representa el estado anterior a un cambio y debe conservarse sin modificaciones.
- No borrar respaldos automáticamente. La depuración futura requiere una decisión explícita del usuario.
- Los ZIP se sincronizan mediante OneDrive y se excluyen de Git por tamaño; sus archivos `.txt` y `.sha256` permiten identificarlos y verificar su integridad.
- Los paquetes de despliegue no sustituyen los respaldos completos: un respaldo válido incluye `wip-new/` y `redirect-root/` dentro de `sitio-web-actual/`.

### Documentos comerciales

- Manuales y plantillas maestras: `lineamientos-y-recursos-corporativos/`.
- Entregables de una campaña o cliente: crear una carpeta de proyecto separada, con fuentes y entregables claramente identificados.

### Producción audiovisual

- Crear una subcarpeta por campaña dentro de `produccion-audiovisual-y-ferias/`.
- Separar `assets`, `trabajo`, `control-calidad`, `entregables` y `archivo-control`.
- No mezclar videos finales con clips fuente.

### Material histórico

- `historico-web-fuentes-2022/` es sólo lectura.
- No renombrar, optimizar ni sobrescribir originales históricos.
- Toda adaptación se realiza sobre una copia con nombre nuevo.

## Convención de nombres

- Carpetas de proyecto: `tema-campana-AAAA`.
- Entregables: `Marca-Tipo-Tema-AAAA-Variante.ext`.
- Clips secuenciales: `NN - Título descriptivo.ext`.
- Evitar nombres del tipo `final-final2`, marcas de tiempo automáticas y nombres dependientes del agente.
- Incluir la herramienta sólo cuando sea relevante para reproducir el trabajo, por ejemplo `video-feria-google-flow-2026`.

## Estado documental

Cada proyecto importante debe incluir:

1. `README.md`: propósito, alcance y mapa.
2. `AGENTS.md`: reglas locales si son necesarias.
3. Estado del proyecto: pendiente, en producción, aprobado o archivado.
4. Fuentes y procedencia de recursos externos.
5. Registro de entregables y validaciones.
6. Pendientes conocidos y decisiones que requieren aprobación humana.

## Regla de continuidad

Antes de trabajar, cualquier agente debe leer primero `AGENTS.md`, `PROJECT_KNOWLEDGE_BASE.md`, `CONTINUIDAD-DEL-PROYECTO.md` y el `README.md` de la carpeta involucrada. Después debe verificar el estado Git y evitar duplicar material que ya tenga una ubicación canónica. Toda documentación interna debe usar rutas relativas para que el proyecto pueda cambiar de nombre o ubicación.

## Regla de carpeta compartida

- Drive/OneDrive conserva el conjunto completo; Git conserva principalmente código, instrucciones y trazabilidad.
- No asumir que un archivo ignorado por Git es temporal: videos, ZIP, documentos corporativos y fuentes históricas pueden ser esenciales.
- No crear vínculos a archivos fuera de la raíz compartida.
- Antes de copiar o mover, asegurar disponibilidad local completa y sincronización finalizada.
- Evitar modificaciones simultáneas del mismo archivo y revisar cualquier copia de conflicto antes de decidir cuál es canónica.

## Archivos temporales

`tmp/` se usa únicamente para renders, extracciones y revisiones transitorias. No debe considerarse fuente de verdad ni entregarse como material final.
