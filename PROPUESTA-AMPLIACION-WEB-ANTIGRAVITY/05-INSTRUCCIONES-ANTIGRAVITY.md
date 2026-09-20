# Instrucciones de implementación para Antigravity

## Objetivo

Complementar `wip-new` con dos nuevas divisiones —Calderas & Vapor y Automatización & IoT— sin rediseñar la web ni alterar su identidad visual.

## Reglas obligatorias

1. Trabajar primero sobre una copia o rama recuperable. No sobrescribir la versión desplegable sin aprobación.
2. Mantener HTML, CSS y JavaScript nativos. No incorporar Node, frameworks ni compilación.
3. Preservar rutas relativas y funcionamiento bajo `/wip-new/`.
4. Reutilizar cabecera, topbar, navegación, `page-hero`, tarjetas, botones, formularios, modal, footer y estilos responsive existentes.
5. No cambiar logos, paleta, tipografías, radios, sombras o lenguaje visual global.
6. Crear `calderas-vapor.html` y `automatizacion-iot.html` siguiendo la anatomía de `tratamiento-agua.html` y `servicios.html`.
7. Añadir ambas opciones a la navegación y al footer de todas las páginas.
8. Actualizar home y formulario sólo con las entradas descritas en `02-ARQUITECTURA-PROPUESTA.md`.
9. Mantener los datos comerciales actuales de WIP hasta que el usuario confirme cambios.
10. No mostrar correos ni teléfonos de Arauterm como contacto principal; dirigir cotizaciones a WIP.

## Tratamiento de la marca Arauterm

- Usar el logo Arauterm únicamente en la nueva página de calderas y en la tarjeta correspondiente del home.
- Texto permitido por confirmación del usuario: “Representantes de Arauterm en Bolivia”.
- No usar “representante exclusivo”, “servicio oficial” o “distribuidor exclusivo”.
- Respetar proporción y área de seguridad del logo.

## Tratamiento de WebServi

- WIP debe seguir siendo la marca dominante de la página.
- Presentar WebServi como tecnología/servicio integrado como partner.
- No reemplazar el contacto WIP por `info@webservi.net` ni por `+591 75020555` sin aprobación.

## Imágenes

- Priorizar fotografías WIP reales para héroes y bloques de servicio.
- Usar la selección Arauterm de 600 px para familias de equipos.
- Usar thumbnails oficiales de 300 px sólo en tarjetas pequeñas o fichas/modales.
- No usar páginas completas de folleto como imagen de fondo; sirven como referencia o descarga.
- Mantener `object-fit: cover` o `contain` según el tipo de recurso, siguiendo los componentes actuales.
- Añadir `alt` descriptivo y no introducir texto crítico dentro de imágenes.

## Validaciones mínimas

- Menú sin desbordamiento a 1280, 1024, 768 y 375 px.
- Navegación, dropdowns y enlaces internos por teclado.
- Contraste de títulos, texto y botones.
- Todos los enlaces relativos y assets locales válidos.
- Formularios y parámetros `?equipo=` / `?servicio=` compatibles con el JavaScript actual.
- Sin errores en consola.
- Sin cambios no solicitados en las páginas actuales.
- Verificación visual final de las dos páginas nuevas y del home.

## Orden recomendado de trabajo

1. Duplicar estructura de páginas existentes.
2. Integrar navegación y footer.
3. Construir `calderas-vapor.html`.
4. Construir `automatizacion-iot.html`.
5. Añadir las dos tarjetas al home.
6. Actualizar formulario y enlaces cruzados.
7. Optimizar únicamente copias de imágenes dentro de `wip-new/assets/img/`.
8. Validar escritorio y móvil.

