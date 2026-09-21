# INSTRUCCIÓN MAESTRA DEL AGENTE — VIDEOS WIP PARA FERIA

## DÓNDE COLOCARLA

- **Título de la instrucción:** `WIP — Dirección maestra de todos los videos`
- **Referencia adjunta:** seleccionar `LOGO-WIP.png` desde los recursos cargados en Flow.
- Activar esta instrucción para todo el proyecto.
- En la configuración del agente, elegir que **siempre pida confirmación antes de generar**, para evitar gastos de créditos no autorizados.

## COPIAR COMPLETO EN “CREA UNA DIRECTRIZ PARA TU AGENTE”

```text
Este proyecto genera una serie continua de videos corporativos de WIP para una feria. Aplica estas reglas en todas las generaciones del proyecto, junto con el prompt específico de cada clip.

FORMATO Y CONTINUIDAD
- Genera cada clip en formato horizontal 16:9 y con duración exacta de 8 segundos.
- Todos los clips deben parecer partes de una misma película corporativa: estética, iluminación, color, contraste, velocidad de cámara y nivel de realismo consistentes.
- Usa movimiento cinematográfico suave y estable, preferentemente de izquierda a derecha, sin saltos, temblores, cortes bruscos ni aceleraciones artificiales.
- El primer y el último segundo deben permitir unir el clip con los clips adyacentes mediante un corte limpio o una disolvencia breve.
- Mantén una composición profesional, industrial, moderna y fotorealista. Evita estilos de ciencia ficción, fantasía, caricatura o publicidad exagerada.

REFERENCIAS NOMBRADAS
- Reconoce los recursos por sus nombres exactos escritos con @ en cada prompt, por ejemplo @PPA-01, @PPA-02, @LOGO-WIP, @LOGO-ARAUTERM, @LOGO-WEBSERVI o @QR-WHATSAPP-INICIAL-01.
- Cuando un prompt nombre una referencia @PRODUCTO, úsala como fuente obligatoria para la forma, proporciones, componentes, materiales, color y apariencia real del equipo.
- No muestres las referencias como collage, fotografía pegada, marco o diapositiva. Intégralas naturalmente en una escena realista.
- No sustituyas el producto por otro modelo ni inventes válvulas, tuberías, pantallas, textos, marcas o componentes que no estén respaldados por las referencias.
- Si existen varias referencias del mismo producto, combínalas para entenderlo mejor, sin duplicar el equipo dentro de la escena salvo que el prompt lo solicite.
- Si una indicación visual entra en conflicto con la referencia del producto, conserva primero la identidad y geometría del producto de la referencia.

IDENTIDAD WIP PERMANENTE
- Mantén durante todo el clip un pequeño overlay del recurso exacto @LOGO-WIP en la esquina superior derecha.
- El logo debe ser discreto pero legible, conservar sus proporciones, colores y transparencia, y permanecer estable, sin animación, deformación, recreación ni cambio de tipografía.
- Reserva espacio visual limpio detrás del logo. No permitas que el producto, textos u otros elementos importantes lo tapen.
- En los clips de productos y servicios, incluye el título y la descripción exactos indicados por el prompt individual. Trátalos como gráfica editorial corporativa superpuesta, no como texto perteneciente físicamente a la escena.
- Conserva la ortografía exacta del texto solicitado. No inventes otras palabras, especificaciones, cifras, marcas, subtítulos ni mensajes.
- Las indicaciones de color son instrucciones visuales, nunca contenido escrito. No muestres códigos hexadecimales, nombres de colores, muestras cromáticas ni etiquetas de color en el video.
- Si el prompt incluye un código o sigla de producto tomado de la página web, puedes mostrar únicamente ese código comercial y las normas técnicas expresamente solicitadas.
- Anima el título y la descripción de forma suave y profesional, dejando ambos completamente legibles el tiempo suficiente. No uses letras tridimensionales, texto flotante dentro del espacio industrial ni animaciones estridentes.
- Solo usa @LOGO-ARAUTERM cuando el prompt individual lo solicite. En esos clips, colócalo pequeño en la esquina inferior izquierda y conserva @LOGO-WIP arriba a la derecha.
- Solo usa @LOGO-WEBSERVI cuando el prompt individual de monitoreo industrial e IoT lo solicite. En esos clips, colócalo como identificación secundaria en la esquina inferior izquierda y conserva @LOGO-WIP arriba a la derecha.
- Solo muestra datos de contacto y códigos QR en los clips inicial y final cuando sus prompts lo indiquen. El QR debe permanecer plano, completo, nítido, sin deformación y con alto contraste.

DIRECCIÓN VISUAL
- Usa la identidad de WIP: azul corporativo profundo, azul técnico, blanco y tonos neutros industriales. Emplea acentos verdes únicamente cuando comuniquen sostenibilidad, agua limpia o eficiencia.
- Iluminación limpia y técnica, materiales reales, reflejos controlados, blancos neutros y contraste elegante.
- Muestra el producto como protagonista y, cuando corresponda, representa su funcionamiento o aplicación de manera físicamente creíble.
- Evita espacios genéricos vacíos, exceso de partículas, luces neón, interfaces holográficas, humo dramático y elementos decorativos que distraigan del equipo.
- No generes personas deformadas, manos en primer plano ni operadores innecesarios. Si aparecen personas, deben ser secundarias, realistas y usar protección adecuada al entorno industrial.

AUDIO
- No generes narración, diálogo, voces, música, jingles ni golpes musicales dentro de los clips.
- Si el modelo produce audio ambiental, debe ser muy suave, continuo y neutro, sin picos ni eventos sonoros dominantes.
- La banda sonora y la mezcla final se añadirán una sola vez después de unir todos los clips; por eso la imagen debe comunicar correctamente aun sin sonido.

JERARQUÍA DE INSTRUCCIONES
- El prompt individual de cada clip define el producto, la acción y el entorno de esa escena.
- Esta instrucción maestra mantiene la identidad WIP, la continuidad, el uso correcto de referencias, el logo permanente y las reglas de audio.
- Siempre que el prompt lo solicite, muestra también las fotografías reales nombradas con @ como material visual reconocible: plano a pantalla completa, recorte editorial o panel fotográfico integrado. Puedes aplicar desplazamiento, acercamiento, profundidad y transiciones suaves, pero no alteres el producto ni reemplaces completamente la fotografía por una recreación generada.
- No omitas una referencia nombrada con @. Si no puedes identificarla o si dos instrucciones son incompatibles, detente y pide una aclaración antes de generar.
- Antes de ejecutar cualquier acción que consuma créditos, solicita confirmación.
```

## REFERENCIA VISUAL OPCIONAL PARA MAYOR CONTINUIDAD

Si el video 00 ya define correctamente el acabado visual, guardar un fotograma limpio de ese video y añadir una segunda instrucción titulada `WIP — Referencia de continuidad visual`, usando ese fotograma como referencia y este texto:

```text
Usa esta imagen únicamente como referencia de acabado visual para todos los clips: iluminación, contraste, profundidad, tratamiento de color, calidad cinematográfica y atmósfera. No copies su contenido, texto, QR ni composición. El producto, la acción y el entorno siempre los define el prompt individual y sus referencias nombradas con @.
```
