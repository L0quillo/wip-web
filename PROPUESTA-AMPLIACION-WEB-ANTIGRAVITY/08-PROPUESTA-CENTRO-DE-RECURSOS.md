# Propuesta: Centro de Recursos para Ingeniería Industrial

## Objetivo

Crear una sección útil y recurrente para ingenieros, responsables de mantenimiento, proyectistas, compradores técnicos y operadores. Las herramientas deben resolver cálculos preliminares en pocos minutos y conducir naturalmente hacia una evaluación o cotización WIP.

Nombre recomendado en el menú: **Recursos Técnicos**.

Ruta recomendada: `recursos.html`.

Mensaje principal: **Cálculos, tablas y guías prácticas para sistemas de agua, vapor, tuberías, calderas y automatización industrial.**

## Referencias internacionales revisadas

- TLV ofrece más de 50 cálculos para vapor, condensado, agua, aire y gas, además de tablas de vapor: https://www.tlv.com/steam-info/eng-calc
- Spirax Sarco reúne tablas de vapor, manuales, cursos, guías y herramientas de diseño: https://www.spiraxsarco.com/resources-and-design-tools
- GF Piping Systems calcula caudal, velocidad y pérdida de presión en tuberías: https://www.gfps.com/en-mx/downloads-tools/online-tools.html
- Grundfos combina selección de bombas, curvas, documentación y comparación de consumo energético: https://www.grundfos.com/solutions/support/help-centre
- DuPont WAVE integra diseño de ósmosis inversa, ultrafiltración e intercambio iónico: https://www.dupont.com/water/resources/rosa-software.html
- Endress+Hauser Applicator permite seleccionar y dimensionar instrumentos de caudal, nivel, presión y temperatura: https://www.endress.com/en/support-overview/device-support-overview/applicator-select-size-instrument
- Siemens TIA Selection Tool ayuda a configurar proyectos de automatización y tableros: https://www.siemens.com/en-us/products/tia/selection-tool/
- Schneider Electric Ecodial dimensiona instalaciones eléctricas, cables, protecciones, caída de tensión y cortocircuito: https://www.se.com/mx/es/faqs/FA142943/
- AMPAC agrupa calculadoras preliminares de ósmosis inversa, recuperación, rechazo y costo operativo: https://ampacwatersystems.com/water-treatment-calculators/

## Arquitectura del centro

```text
Recursos Técnicos
├── Vapor y calderas
├── Agua y tratamiento
├── Tuberías, fluidos y bombas
├── Automatización e instrumentación
├── Electricidad industrial
├── Conversores y tablas
└── Guías, checklists y descargas
```

Cada calculadora debe tener una URL propia, explicación, fórmula utilizada, ejemplo, unidades, advertencias, fecha de revisión y CTA no invasivo.

## Prioridad 1: herramientas que conviene lanzar primero

Estas herramientas tienen alta frecuencia de uso, encajan directamente con WIP y pueden implementarse sin modelado excesivamente complejo.

### 1. Tabla interactiva de vapor saturado

**Entrada:** presión manométrica o absoluta, o temperatura.

**Salida:** temperatura de saturación, volumen específico, entalpía del agua, calor latente y entalpía total.

**Valor:** herramienta de consulta recurrente para todo trabajo con vapor.

### 2. Diámetro preliminar de tubería de vapor

**Entrada:** caudal de vapor, presión, longitud, velocidad máxima o pérdida de presión permitida.

**Salida:** diámetro interno calculado, diámetro nominal sugerido, velocidad y pérdida estimada.

**Advertencia:** selección preliminar; validar presión, schedule, accesorios, simultaneidad y código aplicable.

### 3. Pérdida de presión y velocidad en tuberías de agua

**Entrada:** caudal, diámetro, longitud, material, rugosidad y accesorios.

**Salida:** velocidad, pérdida lineal, pérdidas menores y presión/altura requerida.

**Método:** Darcy-Weisbach como base; Hazen-Williams puede ofrecerse como comparación claramente identificada.

### 4. Conversor universal industrial

Presión, temperatura, caudal, energía, potencia, longitud, volumen, conductividad, concentración y masa.

Debe incluir conversiones habituales en Bolivia: bar, kgf/cm², psi, kPa; kg/h de vapor; m³/h, L/min y GPM; kcal/h, kW y BTU/h.

### 5. Dosificación química

**Entrada:** caudal de agua, dosis objetivo en mg/L, concentración comercial, densidad y horas de operación.

**Salida:** consumo horario/diario, caudal de bomba dosificadora y volumen de tanque para autonomía seleccionada.

Aplicable a cloración, ajuste de pH, coagulantes, antincrustantes y otros químicos. Debe exigir que el usuario confirme concentración y densidad de la ficha del producto.

### 6. Balance simple de ósmosis inversa

**Entrada:** permeado requerido, recuperación y rechazo de sales.

**Salida:** alimentación, permeado, concentrado, TDS estimado del permeado y relación concentrado/permeado.

No debe recomendar presión, número de membranas ni antincrustante sin análisis completo de agua y proyección del fabricante.

### 7. Dimensionamiento preliminar de bomba

**Entrada:** caudal, altura estática, longitud, tubería, accesorios y eficiencia estimada.

**Salida:** altura dinámica total, potencia hidráulica y potencia de motor orientativa.

### 8. Calculadora eléctrica trifásica

Conversión entre kW, kVA, corriente, tensión, factor de potencia y eficiencia. Añadir cálculo preliminar de caída de tensión por longitud y sección.

### 9. Escalamiento de señal 4-20 mA

**Entrada:** rango mínimo/máximo del instrumento y corriente medida.

**Salida:** valor de ingeniería y porcentaje del rango. Incluir cálculo inverso de valor a corriente.

### 10. Volumen de tanque y tiempo de retención

Tanques rectangulares, cilíndricos verticales y horizontales. Calcular volumen útil, tiempo de retención y autonomía según caudal.

## Prioridad 2: diferenciadores directamente comerciales

### Vapor, calderas y condensado

- Consumo de vapor para calentar un tanque o lote.
- Tiempo estimado de calentamiento.
- Consumo de combustible de una caldera según producción de vapor y eficiencia.
- Eficiencia de caldera por método directo simplificado.
- Cantidad de condensado recuperable.
- Ahorro de energía, agua y químicos por retorno de condensado.
- Porcentaje y caudal de vapor flash después de una reducción de presión.
- Dimensionamiento preliminar de retorno de condensado.
- Estimación de pérdidas térmicas de tubería aislada/no aislada.
- Espesor económico orientativo de aislamiento.
- Dimensionamiento inicial de tanque de purga.
- Estimación de purga según ciclos de concentración o conductividad.
- Capacidad de agua de alimentación y tanque de condensado.

### Tratamiento de agua

- Dimensionamiento de filtro multimedia por velocidad superficial.
- Volumen de medio filtrante y expansión durante retrolavado.
- Caudal y duración de retrolavado.
- Dimensionamiento de filtro de carbón activado por tiempo de contacto EBCT.
- Capacidad y frecuencia de regeneración de ablandador.
- Consumo estimado de sal por regeneración.
- Conversión de dureza: mg/L como CaCO3, ppm, °f, °dH y grains/gal.
- Capacidad preliminar de desmineralizador por carga iónica.
- Balance RO con recuperación y rechazo.
- Índice de ensuciamiento SDI: guía de cálculo e interpretación.
- Estimación de autonomía de cartuchos por diferencial de presión e historial.
- Dosis de cloro a partir de demanda y residual objetivo.
- Tiempo de contacto CT para desinfección como hoja orientativa, sin sustituir normativa ni ensayo.
- Preparación y dilución de soluciones químicas.
- Conversión entre conductividad y TDS con factor seleccionable.
- Carga hidráulica y tiempo de retención para plantas de tratamiento.

### Tuberías y fluidos

- Caudal, diámetro y velocidad: despejar cualquiera de las tres variables.
- Pérdida de carga en tubería y accesorios.
- Longitud equivalente de accesorios.
- Número de Reynolds y régimen de flujo.
- Potencia hidráulica y rendimiento.
- NPSH disponible preliminar.
- Dimensionamiento de aire comprimido por velocidad y caída de presión.
- Dimensionamiento preliminar de líneas GN/GLP sólo como estimación; el diseño final debe cumplir normativa y ser revisado por especialista.

### Automatización, IoT e instrumentación

- Escalamiento 4-20 mA y 0-10 V.
- Conversión PT100 temperatura/resistencia.
- Selección de rango de transmisor y porcentaje de span.
- Incertidumbre combinada y error total básico.
- Frecuencia de muestreo, número de registros y almacenamiento mensual.
- Consumo y autonomía estimada de batería de nodo IoT.
- Presupuesto básico de enlace LoRaWAN, con advertencia de que requiere estudio de cobertura real.
- Conversión Modbus: registros, palabras de 16/32 bits y orden de bytes como guía educativa.
- Calculadora de umbrales y bandas de alarma.
- Tiempo de disponibilidad y porcentaje de uptime.

### Electricidad industrial

- Corriente monofásica y trifásica.
- kW, kVA, factor de potencia y eficiencia.
- Caída de tensión preliminar.
- Consumo mensual y costo de energía.
- Ahorro estimado con variador de frecuencia en cargas centrífugas.
- Conversión HP/kW y estimación de corriente de motor.
- Dimensionamiento orientativo de transformador por carga y simultaneidad.
- Energía reactiva y corrección de factor de potencia.

Los cálculos de sección de cable, cortocircuito, selectividad y protección deben derivar a herramientas normativas o revisión profesional; no conviene emitir una selección definitiva desde una calculadora simplificada.

## Tablas y referencias rápidas

- Vapor saturado por presión y por temperatura.
- Diámetros nominales y diámetros internos por schedule.
- Velocidades orientativas por tipo de fluido y servicio.
- Propiedades básicas del agua por temperatura.
- Conversión de unidades industriales.
- Dureza y alcalinidad como CaCO3.
- Rangos típicos de pH, ORP, conductividad y turbidez con contexto de aplicación.
- Compatibilidad química básica de materiales, enlazando siempre la tabla específica del fabricante.
- Códigos de colores y símbolos P&ID como guía, no como sustituto de la norma.
- Tabla rápida de señales industriales: 4-20 mA, 0-10 V, PT100, pulsos y Modbus.

No reproducir tablas protegidas de normas ASME, API, IEC, NFPA o equivalentes. Se pueden explicar conceptos, citar la norma y enlazar su fuente oficial.

## Guías y checklists que generan visitas recurrentes

- Datos necesarios para cotizar una caldera.
- Checklist de inspección diaria/semanal de una sala de calderas.
- Diagnóstico básico de golpe de ariete.
- Cómo identificar pérdidas en trampas de vapor.
- Datos necesarios para dimensionar una línea de vapor.
- Checklist de retorno de condensado.
- Cómo tomar una muestra de agua para análisis.
- Datos necesarios para cotizar una planta RO.
- Diagnóstico básico por diferencial de presión en filtros.
- Plan de mantenimiento de UV, ozono y bombas dosificadoras.
- Checklist de calibración de pH, ORP y conductividad.
- Datos necesarios para automatizar una máquina o proceso.
- Checklist de levantamiento de tableros eléctricos.
- Plantilla de lista de señales I/O.
- Plantilla de matriz de alarmas.
- Guía de selección entre sensor cableado y LoRaWAN.
- Glosario industrial español-inglés-portugués.

## Estrategia de recurrencia y posicionamiento

1. No exigir registro para usar las calculadoras principales.
2. Permitir compartir el resultado mediante URL o descargar una ficha PDF.
3. Recordar unidades y valores usados recientemente sólo en el navegador.
4. Mostrar un ejemplo resuelto debajo de cada herramienta.
5. Incluir “última revisión” y fuente técnica.
6. Publicar una calculadora o guía nueva cada mes.
7. Añadir enlaces cruzados desde cada producto WIP hacia su calculadora relacionada.
8. Después del resultado, ofrecer “Solicitar validación de ingeniería” o “Cotizar esta solución”.
9. Diseñar primero para móvil; muchos técnicos consultan desde planta.
10. Crear páginas independientes para SEO, no una única calculadora gigante.

## Lanzamiento recomendado por fases

### Fase 1 - Utilidad inmediata

1. Conversor industrial.
2. Tabla de vapor saturado.
3. Diámetro de tubería de vapor.
4. Caudal/diámetro/velocidad de agua.
5. Dosificación química.
6. Balance de ósmosis inversa.
7. Volumen de tanque y retención.
8. Escalamiento 4-20 mA.

### Fase 2 - Captación comercial

9. Consumo de vapor para calentamiento.
10. Eficiencia y combustible de caldera.
11. Vapor flash y recuperación de condensado.
12. Filtros multimedia y carbón activado.
13. Ablandador y consumo de sal.
14. Altura dinámica y potencia de bomba.
15. Electricidad trifásica y caída de tensión.

### Fase 3 - Biblioteca especializada

16. Purga y agua de alimentación de caldera.
17. Aislamiento y pérdidas térmicas.
18. Autonomía IoT y almacenamiento de datos.
19. PT100 y selección de transmisores.
20. Plantillas, checklists y guías descargables.

## Seguridad y responsabilidad

Todas las herramientas deben indicar:

> Resultado preliminar para apoyo de ingeniería. No sustituye el relevamiento, la ficha del fabricante, el análisis de agua, la normativa aplicable ni la revisión de un profesional competente.

Los resultados de vapor, gas, recipientes a presión, electricidad, químicos y desinfección requieren especial cautela. Evitar recomendaciones automáticas que puedan interpretarse como diseño final certificado.

## Recomendación final

La mejor primera versión no necesita decenas de calculadoras. Ocho herramientas bien resueltas, rápidas, en español y con unidades SI pueden convertir la web WIP en una referencia regional. La tabla de vapor, el diámetro de tubería, la dosificación química y el balance RO probablemente serán las herramientas de mayor recurrencia inicial.

