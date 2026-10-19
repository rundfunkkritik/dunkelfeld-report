# veroeffentlichen.ps1 - holt Stand, committet, pusht und prueft die Live-Seite.
# Aufruf: .\veroeffentlichen.ps1 "Commit-Nachricht"
param([Parameter(Mandatory=$true)][string]$Nachricht)
Set-Location $PSScriptRoot
$ErrorActionPreference = 'Continue'
[Console]::OutputEncoding = [Text.Encoding]::UTF8

git pull --rebase --autostash
if ($LASTEXITCODE -ne 0) { Write-Host "ABBRUCH: pull --rebase fehlgeschlagen." -ForegroundColor Red; exit 1 }

git add -A
$geaendert = @(git diff --cached --name-only)
if ($geaendert.Count -eq 0) { Write-Host "Nichts zu veroeffentlichen (keine Aenderungen)."; exit 0 }
git diff --cached --stat

git commit -m $Nachricht
if ($LASTEXITCODE -ne 0) { Write-Host "ABBRUCH: Commit fehlgeschlagen." -ForegroundColor Red; exit 1 }
git push
if ($LASTEXITCODE -ne 0) { Write-Host "ABBRUCH: Push fehlgeschlagen." -ForegroundColor Red; exit 1 }

# Live-Pruefung der geaenderten HTML-Seiten (GitHub Pages braucht ~1 Minute)
$seiten = $geaendert | Where-Object { $_ -like '*.html' } | Select-Object -First 5
foreach ($s in $seiten) {
    $url = "https://dunkelfeld.report/$s"
    $status = '?'
    for ($i = 1; $i -le 12; $i++) {
        $kopf = (curl.exe -s -I -o NUL -w "%{http_code}" $url)
        $status = $kopf
        if ($status -eq '200') { break }
        Start-Sleep -Seconds 10
    }
    Write-Host "$status  $url"
}