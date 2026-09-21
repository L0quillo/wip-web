# Plan de audio continuo para la película de feria

## Decisión de producción

No ensamblar el audio generado independientemente por cada clip de Flow. Aunque Veo admite audio, Google describe la función como experimental: ambientes, intensidad, timbre y mezcla pueden cambiar entre generaciones, y una generación puede fallar por baja calidad de audio. Para una película continua, usar Flow para imagen y construir después una única banda sonora.

Fuentes oficiales consultadas:

- https://blog.google/innovation-and-ai/products/veo-updates-flow/
- https://support.google.com/flow/answer/16353333
- https://support.google.com/flow/answer/16352836

## Estructura de la mezcla

### Pista 1 — Música corporativa continua

- Una sola composición instrumental de 4:32, o una pieza más larga editada exactamente a esa duración.
- Estilo: tecnología industrial elegante, pulso firme de 96 a 108 BPM, percusión contenida, sintetizadores cálidos y textura mecánica sutil.
- Sin voz cantada, jingle, golpes cinematográficos exagerados ni cambios bruscos de género.
- La armonía evoluciona suavemente por bloques y mantiene un pulso constante en los cortes de 8 segundos.
- Crear un final que pueda volver musicalmente al inicio para la versión en bucle.

### Pista 2 — Ambiente industrial continuo

- Cama estéreo baja y estable durante toda la película.
- Combinar sala industrial limpia, flujo de agua, ventilación y resonancia metálica tenue.
- No reiniciar el ambiente en cada clip.
- Usar crossfades de 12 a 24 fotogramas cuando cambie la textura del ambiente.

### Pistas 3 y 4 — Efectos puntuales

- Agua, bombas, burbujas, válvulas, aire, vapor, soldadura, quemador y obra civil.
- Elegir uno o dos efectos característicos por escena, no llenar todos los segundos.
- Hacer entrar el efecto entre 6 y 12 fotogramas antes del corte y dejar una cola corta después del corte cuando ayude a unir escenas.
- El efecto nunca debe ocultar la música ni generar sobresaltos en el stand.

### Pista 5 — Voz

- No usar narración en la versión principal de feria. La pantalla debe entenderse sin sonido y los datos aparecen en apertura y cierre.
- Si después se solicita locución, grabarla como una sola toma continua y hacer una versión alternativa; no generar una voz diferente por clip.

## Mapa temporal

| Tiempo | Bloque | Tratamiento sonoro |
|---|---|---|
| 00:00–00:08 | Apertura y contacto | Inicio musical limpio, agua suave y campana técnica discreta |
| 00:08–02:24 | Tratamiento de agua | Flujo, bombas, burbujas y válvulas; ambiente claro y ligero |
| 02:24–02:48 | Filtración metálica | Graves mecánicos suaves, aire y circulación de fluidos |
| 02:48–03:36 | Servicios industriales | Vapor, soldadura controlada, herramientas y sala técnica |
| 03:36–04:08 | Arauterm | Quemador contenido, circulación térmica y vapor estable; crecimiento musical moderado |
| 04:08–04:24 | WebServi — Sensores y monitoreo IoT | Textura tecnológica discreta, pulsos de telemetría y alertas suaves sin cortar la música |
| 04:24–04:32 | Contacto final | Reducir efectos, mantener música y agua; resolver de forma compatible con el reinicio |

## Transiciones

- Los cortes visuales ocurren cada 8 segundos, pero el audio no debe cortar en esos puntos.
- Desplazar efectos respecto del corte visual crea continuidad y evita sensación de presentación por diapositivas.
- Usar automatización suave de volumen, sin silencios entre clips.
- No colocar un golpe musical en cada producto.
- Para el bucle, superponer entre 1 y 2 segundos del final con el comienzo en la cama ambiental, sin alterar la duración del video.

## Especificaciones de mezcla

- Frecuencia de muestreo: 48 kHz.
- Profundidad: 24 bits durante edición.
- Mezcla: estéreo.
- Objetivo aproximado: −14 LUFS integrados.
- Pico máximo: −1 dBTP.
- Exportación maestra: WAV PCM 48 kHz/24-bit.
- Exportación dentro del video: AAC, 48 kHz, 320 kbps estéreo.
- Conservar una copia del video sin audio para pantallas que operen silenciadas.

## Control antes de la feria

1. Reproducir la película completa y escucharla sin mirar para detectar saltos.
2. Reproducirla en bucle durante al menos tres vueltas.
3. Probar en los parlantes reales del stand a volumen conversacional.
4. Verificar que no haya distorsión, silencios accidentales ni cambios bruscos de nivel.
5. Confirmar que apertura, QR, productos y contacto final se entiendan con el audio apagado.
