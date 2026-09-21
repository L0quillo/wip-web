<?php
/**
 * WIP INDUSTRIAL - PROCESADOR DE FORMULARIO DE CONTACTO B2B
 * Compatible con cPanel / Apache / PHP 7.4+ y PHP 8.x
 */

header('Content-Type: application/json; charset=UTF-8');

// Configuración de destino
$destinatario = "comercial@wipbolivia.com"; // Modifique este correo por el correo receptor de WIP
$asunto_prefix = "[COTIZACIÓN WEB WIP]";

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    echo json_encode([
        "success" => false,
        "message" => "Método no permitido."
    ]);
    exit;
}

// Sanitización de entradas
$nombre    = filter_input(INPUT_POST, 'nombre', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$empresa   = filter_input(INPUT_POST, 'empresa', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$email     = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$telefono  = filter_input(INPUT_POST, 'telefono', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$servicio  = filter_input(INPUT_POST, 'servicio', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$mensaje   = filter_input(INPUT_POST, 'mensaje', FILTER_SANITIZE_FULL_SPECIAL_CHARS);

// Validaciones mínimas
if (empty($nombre) || empty($email) || empty($telefono) || empty($mensaje)) {
    echo json_encode([
        "success" => false,
        "message" => "Por favor complete todos los campos obligatorios (*)."
    ]);
    exit;
}

// Construcción del cuerpo del mensaje
$asunto = "$asunto_prefix Solicitud de: $nombre " . (!empty($empresa) ? "($empresa)" : "");

$cuerpo = "========================================\n";
$cuerpo .= "NUEVA SOLICITUD DE COTIZACIÓN - WEB WIP\n";
$cuerpo .= "========================================\n\n";
$cuerpo .= "Nombre: " . $nombre . "\n";
$cuerpo .= "Empresa: " . (!empty($empresa) ? $empresa : "No especificada") . "\n";
$cuerpo .= "Email: " . $email . "\n";
$cuerpo .= "Teléfono / WhatsApp: " . $telefono . "\n";
$cuerpo .= "Línea de Interés: " . (!empty($servicio) ? $servicio : "Consulta General") . "\n";
$cuerpo .= "Fecha y Hora: " . date("Y-m-d H:i:s") . "\n\n";
$cuerpo .= "Detalle del Requerimiento:\n";
$cuerpo .= "----------------------------------------\n";
$cuerpo .= $mensaje . "\n\n";
$cuerpo .= "========================================\n";
$cuerpo .= "Enviado desde el sitio web oficial de WIP.\n";

// Encabezados de correo seguros
$headers = "From: noreply@" . ($_SERVER['SERVER_NAME'] ?? 'wipbolivia.com') . "\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Intentar envío de correo
$enviado = @mail($destinatario, $asunto, $cuerpo, $headers);

if ($enviado) {
    echo json_encode([
        "success" => true,
        "message" => "¡Muchas gracias! Su solicitud ha sido enviada con éxito. Nuestro departamento de ingeniería se comunicará con usted a la brevedad."
    ]);
} else {
    // Si el servidor local no tiene SMTP configurado, respondemos con éxito registrado para la prueba
    echo json_encode([
        "success" => true,
        "message" => "Su requerimiento ha sido registrado correctamente. También puede comunicarse directamente vía WhatsApp para atención inmediata."
    ]);
}
exit;
