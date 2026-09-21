param(
    [Parameter(Mandatory = $true)]
    [string]$Motivo
)

$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $projectRoot 'sitio-web-actual'
$destination = Join-Path $projectRoot 'respaldos-versiones-web'

if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "No se encontró la carpeta web: $source"
}

if (-not (Test-Path -LiteralPath $destination -PathType Container)) {
    New-Item -ItemType Directory -Path $destination | Out-Null
}

$safeReason = $Motivo.ToLowerInvariant() -replace '[^a-z0-9áéíóúñ]+', '-'
$safeReason = $safeReason.Trim('-')
if ([string]::IsNullOrWhiteSpace($safeReason)) {
    $safeReason = 'cambio-web'
}

$timestamp = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$baseName = "${timestamp}__antes-de-${safeReason}"
$zipPath = Join-Path $destination "${baseName}.zip"
$hashPath = Join-Path $destination "${baseName}.sha256"
$recordPath = Join-Path $destination "${baseName}.txt"

if (Test-Path -LiteralPath $zipPath) {
    throw "Ya existe un respaldo con este nombre: $zipPath"
}

Compress-Archive -LiteralPath $source -DestinationPath $zipPath -CompressionLevel Optimal
$hash = (Get-FileHash -LiteralPath $zipPath -Algorithm SHA256).Hash
$fileCount = (Get-ChildItem -LiteralPath $source -Recurse -File).Count

Set-Content -LiteralPath $hashPath -Encoding UTF8 -Value "$hash  $([IO.Path]::GetFileName($zipPath))"
@(
    "Fecha: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss K')"
    "Motivo: $Motivo"
    "Origen: sitio-web-actual/"
    "Archivos: $fileCount"
    "ZIP: $([IO.Path]::GetFileName($zipPath))"
    "SHA256: $hash"
) | Set-Content -LiteralPath $recordPath -Encoding UTF8

Write-Output "Respaldo creado: $zipPath"
Write-Output "Archivos incluidos: $fileCount"
Write-Output "SHA256: $hash"
