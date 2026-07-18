# Recupere le dernier rapport pousse par la routine cloud puis l'envoie par email via Brevo.
# Appele par les taches planifiees Windows "ScopIOM - Envoi rapport hebdo" et "ScopIOM - Envoi rapport mensuel".

$ErrorActionPreference = "Stop"
Set-Location "C:\Users\Julien\scopiom-reporting"

$logDir = "C:\Users\Julien\scopiom-reporting\logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$logFile = Join-Path $logDir ("send_{0:yyyy-MM-dd_HHmm}.log" -f (Get-Date))

Start-Transcript -Path $logFile -Append | Out-Null

try {
    git pull origin master --ff-only
    & "C:\Users\Julien\AppData\Local\Programs\Python\Python312\python.exe" scripts\send_report_email.py
} catch {
    Write-Error $_
} finally {
    Stop-Transcript | Out-Null
}
