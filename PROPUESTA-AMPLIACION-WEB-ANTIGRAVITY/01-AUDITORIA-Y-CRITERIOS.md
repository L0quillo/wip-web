# Auditoría de contenido y criterios de interpretación

## 1. Estado real del proyecto

En la raíz no existe otra web HTML independiente. La raíz contiene material histórico, fotografías, logos y documentos fuente. La web desplegable actual está en `wip-new/`; `wip-new.zip` es su paquete de despliegue y `redirect-root/` contiene únicamente la redirección opcional.

Por tanto, para la ampliación se debe tomar como patrón visual y técnico `wip-new`, y usar las carpetas raíz como biblioteca de contenido original.

## 2. Estructura actual de `wip-new`

Páginas existentes:

- `index.html`
- `tratamiento-agua.html`
- `filtros-metalicos.html`
- `servicios.html`
- `nosotros.html`
- `contacto.html`

Navegación actual:

`Inicio > Tratamiento de Agua > Filtros Metálicos > Ingeniería & Montajes > Nosotros > Contacto > Solicitar Cotización`

Sistema visual que debe conservarse:

- Rojo WIP `#C1303A` como primario.
- Azul industrial `#244088` como secundario.
- Inter para lectura y Montserrat para títulos.
- Contenedor máximo de 1280 px.
- Tarjetas, badges, botones, héroes internos, pie y modal técnico ya existentes.
- Sitio estático, rutas relativas, sin dependencias ni proceso de compilación.

## 3. Vacíos de contenido actuales

- El home sólo muestra tres especialidades; no presenta calderas ni automatización/IoT.
- Las líneas de vapor están presentes como servicio, pero no existe una división comercial de generación térmica.
- Instalaciones eléctricas aparecen dentro de servicios, pero no existe una propuesta completa de tableros, automatización, instrumentación y monitoreo.
- La oferta Arauterm no está explicada ni conectada con montaje, condensado, tratamiento de agua y control.
- La oferta WebServi está fuera del sitio y necesita integrarse sin mezclar contactos ni identidades de forma confusa.

## 4. Cómo interpretar las fuentes

### WIP

WIP es la marca principal del sitio y el punto comercial. Los servicios propios documentados incluyen líneas de vapor y condensado, instalaciones eléctricas, líneas de combustibles, soldadura, refractarios, obras civiles y montajes.

### Arauterm

El usuario confirmó que existe acuerdo comercial y participación conjunta en feria. Puede comunicarse **“Representantes de Arauterm en Bolivia”**, pero no debe afirmarse exclusividad, servicio oficial certificado ni cobertura territorial adicional sin confirmación escrita.

La web oficial del fabricante organiza su oferta en:

- Calderas de vapor.
- Calderas de biomasa.
- Calentadores de fluido térmico.
- Generadores de agua caliente.
- Proyectos especiales.
- Accesorios.

Arauterm describe proyectos especiales como tanques especiales y construcción de serpentines según necesidad del cliente.

### Folleto WIP de calderos

El folleto local presenta una línea WIP con modelos `WIP-CHL` y `WIP-CHG`, capacidades declaradas de 500 a 3000 kgv/h y presión de trabajo/prueba de 8/12 kg/cm². Esta línea no debe mezclarse visualmente con los códigos Arauterm. Presentarla como **“Configuraciones WIP según proyecto”** o validar antes si continúa comercialmente vigente.

El folleto también aporta el alcance complementario: quemadores, combustión a leña, bombas de alta presión, control de nivel, presostatos, manómetros, válvulas, aislación, tablero eléctrico, tanque de purga y dosificación química.

### WebServi / IoT

Los brochures definen una solución de extremo a extremo:

`sensores > interfaz de campo > red/gateway > plataforma > dashboard > alertas`

Incluyen sensores nativos LoRaWAN y adaptación de instrumentos 4-20 mA o RS485/Modbus; presión, temperatura, caudal, pH, ORP y conductividad; históricos, tendencias, API, MQTT, Modbus TCP, integración con SCADA/BMS y alarmas móviles.

Restricción técnica importante: la telemetría IoT complementa la supervisión. No reemplaza protecciones, enclavamientos ni controles críticos cableados.

## 5. Datos que no deben mezclarse automáticamente

| Fuente | Teléfono/correo | Criterio |
|---|---|---|
| Web actual WIP | `+591 70057895`, `comercial@wipbolivia.com` | Mantener como contacto principal del sitio hasta instrucción contraria. |
| Folleto calderos WIP | `76000939 - 70057895` | No añadir el segundo número sin validación. |
| Brochure WebServi | `+591 75020555`, `info@webservi.net` | No sustituir los datos WIP. Definir si se mostrará como aliado o contacto secundario. |
| Web Arauterm | Datos de Brasil | Usar sólo como enlace/fuente del fabricante; las consultas del sitio deben llegar a WIP. |

## 6. Riesgos a controlar

- No copiar descripciones técnicas largas del proveedor literalmente; resumir y enlazar la fuente.
- No presentar fotografías de fabricantes IoT como equipos necesariamente disponibles en stock.
- Usar “modelos referenciales, sujetos a selección técnica y disponibilidad”.
- No prometer rangos, combustible o presión fuera de la ficha específica del modelo.
- No usar imágenes pequeñas de 300 px como héroes; reservarlas para tarjetas o modales.
- Confirmar derecho de uso público del logo Arauterm dentro del acuerdo comercial.

