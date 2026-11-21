# Build JennyModSetup.exe from source on Windows.
param([string]$OutDir = "dist")

$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot\..
try {
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    pyinstaller --clean --distpath $OutDir installer\jennymod-setup.spec
    Write-Host "Built: $OutDir\JennyModSetup.exe"
} finally {
    Pop-Location
}