# 🚀 Guía de Despliegue en Subdirectorio (`wip-new/`) en cPanel

Esta guía explica cómo subir la web como subdirectorio en tu hosting para que esté accesible en:  
👉 **`https://wipbolivia.com/wip-new/index.html`**  
y además redirija automáticamente a cualquier usuario que ingrese a la raíz `https://wipbolivia.com`.

---

## 📁 1. Estructura final en tu servidor cPanel (`public_html`):

```
public_html/
│
├── index.html               <-- (Archivo de redirección de la carpeta redirect-root/)
├── index.php                <-- (Opcional para redirección PHP 301 instantánea)
│
└── wip-new/                 <-- (Sube la carpeta wip-new completa aquí)
    ├── index.html
    ├── tratamiento-agua.html
    ├── filtros-metalicos.html
    ├── servicios.html
    ├── nosotros.html
    ├── contacto.html
    ├── send-contact.php
    └── assets/
        ├── css/
        │   └── main.css
        ├── js/
        │   └── main.js
        └── img/
            ├── qr_whatsapp.png
            ├── logos...
            ├── products...
            └── services...
```

---

## 🛠️ 2. Paso a Paso para Desplegar:

1. **Subir la carpeta `wip-new/`**:
   - Comprime la carpeta `wip-new` en un archivo ZIP (`wip-new.zip`).
   - Ingresa a tu **cPanel** > **Administrador de Archivos (File Manager)** > carpeta **`public_html/`**.
   - Sube y descomprime `wip-new.zip`. Verás la subcarpeta `public_html/wip-new/`.

2. **Colocar el archivo de redirección en la raíz de `public_html/`**:
   - Sube el archivo [`index.html`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/redirect-root/index.html) (o [`index.php`](file:///c:/Users/lucas/OneDrive/Documents/WIP/PAGINA%20WEB%20150822/redirect-root/index.php)) que está en la carpeta `redirect-root/` directamente a la raíz de `public_html/`.
   - Cuando cualquier persona entre a `https://wipbolivia.com/`, el navegador lo redirigirá inmediatamente a `https://wipbolivia.com/wip-new/index.html`.

---

## 📧 3. Configuración de Contactos Ya Integrada:

- **WhatsApp Directo**: `+591 70057895` con enlace oficial `https://wa.me/59170057895` y código QR generado.
- **Recepción de Formularios**: `comercial@wipbolivia.com` en `send-contact.php`.

---

## ⚡ Requisitos:
- **No requiere Node.js, npm ni base de datos.**
- Funciona 100% en cualquier hosting compartido con Apache y PHP.
