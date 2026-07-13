$ErrorActionPreference = "Stop"

$repositoryRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot "..\.."))
$ruffCommand = Get-Command ruff -ErrorAction SilentlyContinue
$pyrightCommand = Get-Command pyright -ErrorAction SilentlyContinue
$missingCommands = @()

Write-Host "== Python quality tool preflight =="

if ($null -eq $ruffCommand) {
    $missingCommands += "ruff"
    Write-Host "ERROR: Required command 'ruff' is unavailable." -ForegroundColor Red
}

if ($null -eq $pyrightCommand) {
    $missingCommands += "pyright"
    Write-Host "ERROR: Required command 'pyright' is unavailable." -ForegroundColor Red
}

if ($missingCommands.Count -gt 0) {
    Write-Host "No tools were installed or updated. Install the missing development prerequisites and run this script again."
    exit 1
}

$ruffExitCode = 0
$pyrightExitCode = 0

Push-Location -LiteralPath $repositoryRoot
try {
    Write-Host ""
    Write-Host "== Ruff =="
    & $ruffCommand check "extensions/slicerSTRT/slicerSTRT"
    $ruffExitCode = $LASTEXITCODE
    if ($ruffExitCode -ne 0) {
        Write-Host "ERROR: Ruff failed with exit code $ruffExitCode." -ForegroundColor Red
    }

    Write-Host ""
    Write-Host "== Pyright =="
    & $pyrightCommand --project "pyrightconfig.json"
    $pyrightExitCode = $LASTEXITCODE
    if ($pyrightExitCode -ne 0) {
        Write-Host "ERROR: Pyright failed with exit code $pyrightExitCode." -ForegroundColor Red
    }
}
finally {
    Pop-Location
}

if ($ruffExitCode -ne 0 -or $pyrightExitCode -ne 0) {
    Write-Host "ERROR: Python quality checks failed." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Python quality checks passed."
exit 0
