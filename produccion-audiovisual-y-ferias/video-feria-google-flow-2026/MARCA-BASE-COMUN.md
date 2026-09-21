# Marca base común para los 34 clips

## Firma WIP permanente

- Archivo principal: `assets/branding/LOGO-WIP.png`.
- Archivo de mayor resolución disponible: `assets/branding/LOGO-WIP-ALTA-RESOLUCION.png`.
- `LOGO-WIP.png` se carga una sola vez desde `assets/FLOW-CARGAR-UNA-VEZ/` y se reutiliza como `@LOGO-WIP`.
- Pedir explícitamente a Flow que use ese archivo como overlay fijo, sin redibujarlo, durante los 8 segundos completos.
- Posición fija: esquina superior derecha.
- Lienzo maestro: 1920 × 1080.
- Ancho recomendado del logo: 210 px; conservar proporción original.
- Margen derecho: 56 px. Margen superior: 44 px.
- Colocar sobre una placa blanca al 90% de opacidad con 16 px de margen interior y esquinas redondeadas suaves. La placa evita que el logo pierda legibilidad sobre escenas cambiantes.
- Opacidad del logotipo: 92%. No animar, rotar, deformar ni cambiar colores.
- Mantener exactamente la misma posición, escala y opacidad en los 34 clips.
- No usar una entrada o salida individual. La firma permanece estable cuando cambia el video de fondo.
- Verificar cada resultado ampliando el logo: las letras, el óvalo, colores y proporciones deben permanecer intactos. Si hay deformación, reemplazar el logo por el PNG original en montaje sin descartar necesariamente el fondo generado.
- En la apertura y el cierre, el QR ocupa el lado derecho inferior; el logo permanece arriba a la derecha y no debe solaparse con el QR.

## Estructura visual compartida

- Todos los fondos usan dirección de cámara de izquierda a derecha, fotografía industrial realista y la paleta WIP.
- Mantener una zona de respiración en la esquina superior derecha: no colocar rostros, instrumentos importantes o detalles críticos debajo de la firma.
- No colocar marcos alrededor de todo el video. La unidad proviene del logo, color, movimiento y tratamiento fotográfico.
- Ninguna otra marca, watermark o texto permanente está autorizada.

## Identificación secundaria Arauterm

- En los clips 27, 28, 29 y 30 reutilizar también `@LOGO-ARAUTERM` como segundo ingrediente y pedir su overlay inferior izquierdo; la representación fue confirmada por el usuario.
- Posición: esquina inferior izquierda, ancho aproximado de 150 px, placa blanca discreta y opacidad del 90%.
- La firma WIP superior derecha conserva mayor jerarquía y nunca se reemplaza.
- No utilizar el logo Arauterm en los demás clips.
