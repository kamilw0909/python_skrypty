## 1. Trzeba włączyć PowerShell Remoting:
- połączenia sieciowe muszą być prywatne:
  - `Get-NetConnectionProfile`
  - `Set-NetConnectionProfile -InterfaceIndex <index number> -NetworkCategory Private`
- `Enable-PSRemoting -Force`
## 2. Instalacja np z poziomu linux przez ssh:
- pobranie pliku exe
- `ssh użytkownik@192.168.1.2 "curl --output nazwa_plik.exe --url https://link_do_pliku_exe.com/plik.exe"`
- `ssh użytkownik@192.168.1.2 "powershell.exe -Command Invoke-Command -ScriptBlock { Start-Process -Wait -FilePath 'C:\path\do\pliku\program.exe' }"`


### !!! ssh błąd to many authentication errors
- `ssh -o IdentitiesOnly=yes login@192.168.0.12`