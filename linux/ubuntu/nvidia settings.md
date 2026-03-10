
```bash
# https://askubuntu.com/questions/206283/how-can-i-uninstall-a-nvidia-driver-completely
# Если вы хотите быть уверены, что удалите всё, что связано с Nvidia, вы можете использовать эту команду.
sudo apt-get remove --purge '^nvidia-.*'
# Приведённая выше команда также удалит nvidia-commonпакет, и этот nvidia-commonпакет будет иметь в качестве зависимости другой ubuntu-desktopпакет.
# Таким образом, после выполнения указанной выше команды вам также следует выполнить команду установки ubuntu-desktopпакета.
sudo apt-get install ubuntu-desktop


# Для удаления достаточно одной команды
sudo nvidia-uninstall

# Проверьте, какие пакеты от Nvidia у вас установлены.
dpkg -l | grep -i nvidia

nvidia-smi # показывает актуальную версию установленного драйвера, информацию о GPU и, как можно заметить в верхнем правом углу, версию CUDA

# https://help.ubuntu.ru/wiki/%D0%B4%D1%80%D0%B0%D0%B9%D0%B2%D0%B5%D1%80_%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82_nvidia?redirect=1

# Модель видеокарты можно узнать выполнив команду в терминале:
lspci -k | grep -EA2 'VGA|3D'

# Смотрим какие версии драйвера Nvidia есть в репозитории:
sudo apt-get update && clear && apt-cache search nvidia-[0-9] | grep 'binary driver'


# полезные команды (см. в инете)
sudo ubuntu-drivers autoinstall
sudo ubuntu-drivers install
sudo ubuntu-drivers --gpgpu autoinstall nvidia

sudo apt install nvidia-driver-570
ubuntu-drivers devices
sudo apt install nvidia-driver-570-or-whatever-version-you-need

```