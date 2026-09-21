# Estado de renders para el video de feria

Revisión actualizada el 20 de septiembre de 2026.

## Estado general

- Secuencia prevista: 34 clips, numerados del 00 al 33.
- Clips fuente presentes: 34 de 34.
- Duración por clip: 8 segundos.
- Resolución de los clips: 1280 × 720.
- Frecuencia de los clips: 24 fps.
- Todos los clips contienen pista de video y pista de audio nativa de Flow.
- El duplicado exacto de la secuencia 01 está conservado en `archivo-control/duplicados/` y no debe usarse en montaje.

## Entregables existentes

| Archivo | Duración | Resolución | Video | Audio | Uso |
|---|---:|---:|---|---|---|
| `entregables/Video-Feria-WIP-2026-Master.mp4` | 272,04 s | 1280 × 720, 25 fps | H.264 | AAC | Máster de mayor bitrate |
| `entregables/Video-Feria-WIP-2026-Liviano.mp4` | 272,02 s | 1280 × 720, 24 fps | H.264 | AAC | Copia liviana para traslado y reproducción |

## Secuencia

Los archivos de `renders/` están normalizados con el formato `NN - Título.mp4`. El orden de montaje es estrictamente numérico del 00 al 33 y coincide con `ORDEN-DE-MONTAJE.md`.

## Observación técnica

El máster actual fue exportado a 25 fps, mientras los clips originales y la versión liviana están a 24 fps. Para una futura remasterización conviene mantener toda la cadena a 24 fps y usar una sola banda sonora continua según `PLAN-DE-AUDIO.md`.

