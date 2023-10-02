
# Доступ к файловой системе Linux из Windows:
`\\wsl$\`

## Установка WSL2:

```bash
# Включите WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Включите «Платформу виртуальных машин» в Windows 10 (20.04)
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
# для  Windows 10 (19.03, 19.09)
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart

# перезагрузить систему

#  установить версию 2
wsl --set-default-version 2

# изменить WSL версию дистрибутиву Linux на другую
wsl --set-version <distribution name> <versionNumber>

# Проверить WSL версию для каждого дистриб-ва Linux
wsl -l -v

#
wsl --status
wsl --help

# Что бы из WSL перейти на диск C:\ 
cd /mnt/c

# Установите дистрибутив из Microsoft Store
```
