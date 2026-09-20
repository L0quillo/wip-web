# WIP Bolivia — instrucciones compartidas para agentes

## Compatibilidad

- Este proyecto se trabaja con Antigravity y Codex. Mantener compatibles ambos entornos.
- `.agents/skills/` es la fuente existente de habilidades del proyecto. No moverla, renombrarla ni reescribirla para adaptarla a Codex.
- Conservar `skills-lock.json`, `.claude/skills/` y `agent/skills/`; forman parte de la configuración ya usada por otros agentes.
- Antes de aplicar una habilidad local, leer su `SKILL.md` completo y seguir sus referencias necesarias.

## Estado protegido

- La web actual y sus diseños están congelados hasta que el usuario solicite expresamente modificarlos.
- No editar archivos dentro de `wip-new/` ni `redirect-root/` durante tareas de análisis, organización o configuración de agentes.
- No reemplazar, regenerar, comprimir ni borrar `wip-new.zip` salvo petición explícita.
- No alterar imágenes, documentos fuente ni material corporativo en `2. TRATAMIENTO DE AGUA/`, `3. FILTROS METALICOS/`, `13. SERVICIOS/` o `corporativo/` sin autorización explícita.
- No generar diseños, rediseños ni variantes visuales hasta que el usuario lo pida.

## Mapa del proyecto

- `wip-new/`: sitio desplegable actual; HTML, CSS, JavaScript, imágenes y formulario PHP.
- `redirect-root/`: archivos opcionales para redirigir el dominio raíz hacia `/wip-new/index.html`.
- `wip-new.zip`: paquete de despliegue existente.
- `2. TRATAMIENTO DE AGUA/`, `3. FILTROS METALICOS/`, `13. SERVICIOS/`: archivos fuente históricos de productos y servicios.
- `corporativo/`: identidad, documentos y recursos corporativos.
- `.agents/skills/`: habilidades compartidas instaladas por el flujo existente de Antigravity.

## Convenciones técnicas

- El sitio no requiere Node.js, npm ni base de datos; está pensado para Apache/cPanel con PHP 7.4+ u 8.x.
- Preservar rutas relativas y compatibilidad con despliegue en el subdirectorio `/wip-new/`.
- Tratar `wip-new/README-DEPLOY.md` como la guía de despliegue vigente.
- Mantener el idioma público en español y respetar la identidad WIP existente.
- Cuando se autoricen cambios, hacerlos de forma mínima, verificar enlaces y recursos locales, y validar `assets/js/main.js` y `send-contact.php` cuando las herramientas estén disponibles.
- No introducir dependencias, frameworks, procesos de compilación ni cambios de hosting sin autorización explícita.

## Seguridad y preservación

- Esta carpeta actualmente no tiene historial Git. Antes de una futura modificación sustancial, proponer una copia recuperable o inicializar control de versiones; no hacerlo automáticamente.
- No publicar, desplegar, enviar formularios reales ni cambiar direcciones de correo o WhatsApp sin una petición explícita.
- Los documentos e imágenes originales son material de referencia; no sobrescribirlos. Crear derivados con nombres nuevos cuando el usuario autorice trabajo visual.
