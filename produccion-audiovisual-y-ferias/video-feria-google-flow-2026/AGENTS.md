# Agente de producción audiovisual WIP para Google Flow

## Objetivo

Crear clips corporativos de exactamente 8 segundos para una pantalla de feria. El paquete contiene una apertura de contacto, 30 clips de productos o servicios y un cierre de contacto, unidos como una sola película industrial continua.

## Fuentes autorizadas

- Usar `LINEAMIENTOS-FLOW.md` como norma visual maestra.
- Usar `CATALOGO-AUDIOVISUAL.md` como fuente técnica y comercial.
- Usar solamente las imágenes copiadas en `assets/referencias/` para conservar la apariencia real de equipos y trabajos.
- Para operar en Flow, cargar una sola vez la colección plana `assets/FLOW-CARGAR-UNA-VEZ/` y reutilizar cada recurso por su nombre `@NOMBRE`, siguiendo `CARGA-INICIAL-FLOW.md`.
- Los originales de la web y del archivo corporativo están fuera de esta carpeta: no modificarlos.

## Reglas obligatorias para todos los clips

- Duración: 8 segundos exactos.
- Formato maestro: horizontal 16:9, 1920 × 1080, 24 fps.
- Estética: fotografía industrial premium, realista, técnicamente creíble, limpia y sobria.
- Movimiento continuo: cámara y procesos avanzan de izquierda a derecha; el último segundo debe mantener movimiento para facilitar el empalme.
- Paleta ambiental: azul industrial `#244088`, rojo WIP `#C1303A`, carbón `#211915`, gris técnico y acero inoxidable. El rojo se usa solo como acento físico discreto.
- Mantener el logotipo oficial WIP como firma constante en los 34 clips, cargándolo en Flow como ingrediente y solicitando el mismo overlay descrito en `MARCA-BASE-COMUN.md`.
- Flow debe usar el PNG proporcionado, no inventar ni redibujar el logotipo. No introducir otros logotipos, isotipos, marcas de agua ni emblemas.
- Mostrar únicamente los títulos, descripciones, códigos y rótulos editoriales autorizados literalmente en cada prompt. No agregar texto adicional ni convertir códigos de color en texto visible.
- No colocar placa inicial, intro, bumper, marco, fundido desde negro, cierre, outro, llamado a la acción ni fundido a negro.
- No añadir narración, diálogo, presentador ni música dentro de los clips. El sonido final se resolverá en montaje.
- No inventar piezas imposibles, conexiones absurdas, tuberías flotantes, operarios deformes o procesos físicamente incorrectos.
- No usar estética futurista de ciencia ficción, hologramas, neón, animación caricaturesca o publicidad doméstica.

### Excepción para contacto

- Los clips `00-contacto-inicial` y `33-contacto-final` sí deben mostrar los datos de contacto especificados en sus prompts y el QR original suministrado.
- Los clips `31-webservi-sensores-industriales-iot` y `32-webservi-sistema-monitoreo-iot` pueden usar `LOGO-WEBSERVI.png` como identificación secundaria, manteniendo WIP como firma principal.
- Flow se usa para generar el fondo en movimiento; el QR y el texto se superponen en edición usando los archivos originales. No permitir que el modelo regenere, anime, estilice, recorte o distorsione el QR.
- Los clips de contacto conservan también la firma WIP común, además del QR.

### Segmentos Arauterm

- Los clips 27 a 30 incorporan líneas de equipos Arauterm con imágenes obtenidas del sitio oficial del fabricante.
- El acuerdo comercial y la participación conjunta en la feria fueron confirmados por el usuario. Mantener WIP como firma principal y usar el logo Arauterm como identificación secundaria autorizada, exclusiva de esos cuatro clips.
- No modificar los logos WIP o Arauterm, ni pedir a Flow que los regenere.
- No atribuir capacidades, certificaciones o rangos que no figuren en `FUENTES-ARAUTERM.md`.

## Audio

- Seguir `PLAN-DE-AUDIO.md` como norma maestra.
- Pedir a Flow imagen sin diálogo, narración ni música. El audio nativo generado por Veo no forma parte del máster.
- Si Flow entrega audio de ambiente, conservarlo solo como referencia y silenciarlo antes del montaje final.
- La película final usa una sola pista musical continua, una cama ambiental continua y efectos seleccionados en capas separadas.
- El contenido debe entenderse completamente sin sonido porque una feria puede ser ruidosa o reproducir la pantalla silenciada.

## Flujo de trabajo

1. Abrir el prompt numerado correspondiente.
2. Seleccionar en la biblioteca de Flow los recursos exactos enumerados dentro del prompt; no volver a subirlos.
3. Indicar que las referencias nombradas son identidad física, geometría, material y contexto, no fotogramas que deban copiarse literalmente.
4. Generar al menos dos variantes y elegir la que conserve mejor el equipo real.
5. Guardar el resultado en `renders/` con el mismo número y título del prompt.
6. Verificar duración, ausencia de texto no autorizado, realismo, continuidad y audio nativo silenciado antes de aprobar.
7. Cargar el logo WIP en Flow y comprobar en todos los clips la firma común de `MARCA-BASE-COMUN.md`; corregirla en montaje solo si el modelo la altera.
8. Para los clips 00 y 33, añadir QR y datos como capa editorial según el prompt.
9. Unir los clips según `ORDEN-DE-MONTAJE.md`.

## Criterio de aprobación

Un clip se aprueba solo si el producto o servicio se reconoce visualmente sin depender del texto, mantiene una escala industrial realista, empieza ya en acción y termina todavía en movimiento. Los títulos y descripciones autorizados deben aparecer exactamente como están escritos en el prompt; si Flow introduce texto adicional, altera los logotipos o crea una salida a negro, regenerar.
