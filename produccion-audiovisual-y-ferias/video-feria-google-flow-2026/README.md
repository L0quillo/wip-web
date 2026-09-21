# Proyecto Google Flow — Video corporativo WIP para feria 2026

Esta carpeta conserva el proyecto completo de producción de 34 clips de 8 segundos: apertura de contacto, 30 escenas WIP/Arauterm, 2 escenas de sensores y monitoreo industrial IoT WebServi y cierre de contacto. El proyecto ya cuenta con los 34 clips y dos exportaciones finales de aproximadamente 4 minutos y 32 segundos.

## Contenido

- `INSTRUCCION-MAESTRA-AGENTE-FLOW.md`: directriz permanente para configurar el agente de Flow una sola vez.
- `AGENTS.md`: reglas permanentes para cualquier agente que trabaje aquí.
- `LINEAMIENTOS-FLOW.md`: lenguaje visual, cámara, color, continuidad y restricciones.
- `MARCA-BASE-COMUN.md`: posición y tamaño invariables del logotipo WIP.
- `FUENTES-ARAUTERM.md`: procedencia oficial, gama y condiciones de uso de la nueva línea de calderas y calentadores.
- `PLAN-DE-AUDIO.md`: mezcla continua, niveles, capas, transiciones y exportación de sonido.
- `CARGA-INICIAL-FLOW.md`: procedimiento para cargar toda la biblioteca una sola vez y reutilizarla por nombre.
- `CATALOGO-AUDIOVISUAL.md`: resumen técnico de las 32 escenas.
- `ORDEN-DE-MONTAJE.md`: secuencia final y reglas de unión.
- `prompts/`: una instrucción autocontenida por apertura, producto, servicio y cierre.
- `assets/referencias/`: copias de imágenes existentes, organizadas por clip.
- `renders/`: 34 clips fuente numerados del 00 al 33.
- `entregables/`: video final máster y versión liviana.
- `archivo-control/duplicados/`: duplicados conservados para trazabilidad.
- `control-calidad/`: fotogramas y revisiones visuales.
- `montaje-final/`: espacio de trabajo para futuros proyectos editables o nuevas exportaciones.

## Uso en Flow

Al comenzar el proyecto, cargue de una sola vez los 69 archivos de `assets/FLOW-CARGAR-UNA-VEZ/`, siguiendo `CARGA-INICIAL-FLOW.md`. Después cada prompt llama sus recursos por nombre, por ejemplo `@PPA-01`, `@PPA-02` y `@LOGO-WIP`. No es necesario volver a subir archivos para cada clip. Configure 16:9 y 8 segundos y no solicite voz ni música. Si Flow modifica el logo, reemplácelo por el PNG original en montaje. Finalmente, construya una única banda sonora siguiendo `PLAN-DE-AUDIO.md`.

No se modificaron la página web, los archivos corporativos ni las fotografías originales. Las imágenes de este paquete son copias de trabajo. El nombre del directorio principal es deliberadamente neutral (`produccion-audiovisual-y-ferias/`); Google Flow identifica sólo este proyecto y no condiciona futuros trabajos con otras herramientas.
