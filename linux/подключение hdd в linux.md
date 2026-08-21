
# Исправление ошибки подключения жесткого диска в Ubuntu

## Текст ошибки (пример):
Error mounting /dev/sdb1 at/media/name/Transcend:  
wrong fs type,bad option,bad superblock on /dev/sdb1,missing codepage  
or helper program,or other error

## Исправление:
```bash
sudo fdisk -l
sudo apt install nfs-common
sudo apt install cifs-utils
sudo ntfsfix -d /dev/sdc5   # /dev/sdb1 - заменить на своё
```
