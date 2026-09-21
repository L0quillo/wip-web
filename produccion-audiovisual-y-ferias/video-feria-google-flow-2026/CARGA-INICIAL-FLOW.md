# Carga única de recursos en Google Flow

## Objetivo

Subir las imágenes y logos una sola vez al proyecto `WIP Feria — Video corporativo`. Después, cada prompt reutiliza los recursos por su nombre con `@`.

## Pasos

1. Abrir el proyecto principal en Flow.
2. Entrar a la biblioteca o cuadrícula de recursos del proyecto.
3. Abrir la carpeta local `assets/FLOW-CARGAR-UNA-VEZ/`.
4. Seleccionar sus 69 archivos al mismo tiempo.
5. Arrastrarlos juntos a la biblioteca de Flow o utilizar la opción de carga múltiple.
6. Esperar a que finalice toda la carga antes de generar otra escena.
7. Confirmar que Flow muestra nombres reconocibles como `PPA-01`, `FILTRO-ARENA-01`, `LOGO-WIP` y `QR-WHATSAPP-INICIAL-01`.
8. No volver a subir esos archivos en las escenas siguientes.
9. En cada prompt, seleccionar desde la biblioteca únicamente los recursos enumerados bajo `Recursos ya cargados en Flow`.
10. Cuando Flow permita referencias mediante `@`, escribir o seleccionar exactamente los nombres indicados.

## Ejemplo para PPA

El prompt 01 solicita `@PPA-01`, `@PPA-02` y `@LOGO-WIP`. Esos tres recursos ya están en el proyecto: solo se seleccionan, no se cargan nuevamente.

## Reglas

- No cambiar los nombres dentro de Flow.
- No crear copias duplicadas del logo.
- Mantener un solo proyecto para los 34 clips.
- En los clips Arauterm seleccionar también `@LOGO-ARAUTERM`.
- En la apertura y el cierre seleccionar el QR correspondiente.
- Si Flow limita la cantidad de ingredientes simultáneos, priorizar la primera referencia del producto y `@LOGO-WIP`; usar las demás en una segunda variante.
