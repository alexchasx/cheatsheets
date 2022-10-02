```bash
# обновление пакетов
sudo apt update && sudo apt upgrade

# установка Midnight Commander
sudo apt install mc

# ------- Настройка консоли 

# редактирование файла .bashrc
mcedit ~.bashrc
```
- Добавим в конец файла (двойная строка и подсветка ветки git):

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]$(__git_ps1)\n\[\033[00m\]\[\033[0;31m\]\$\[\033[0;33m\] '

- или (со стрелкой на второй строке)

PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\]\u\[\033[0;36m\] @ \[\033[0;36m\]\h \w\[\033[0;32m\]$(__git_ps1)\n\[\033[0;32m\]└─\[\033[0m\033[0;32m\] \$\[\033[0m\033[0;32m\] ▶\[\033[0m\] '

- или (с знаком "└─" на второй строке)

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]$(parse_git_branch)\n\[\033[00m\]└─\[\033[0m\033[0;32m\] \$\[\033[0m\] '

```bash
# запуск новой конфигурации
source ./.bashrc

# ------- 

sudo apt install git
sudo apt install composer

# смотреть установленные модули для php
dpkg -l | grep php | tee packages.txt 

# установка php и некоторые модули к нему
sudo apt install php8.1 -y
sudo apt install php8.1-common php8.1-mysql php8.1-xml
 php8.1-xmlrpc php8.1-curl php8.1-gd php8.1-imagick 
 php8.1-cli php8.1-dev php8.1-imap php8.1-mbstring 
 php8.1-opcache php8.1-soap php8.1-zip php8.1-intl php8.1-fpm -y 

# проверить версию
php -v

# установка Node.js (версию меняем на нужную) и npm
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

# ------- Установка docker вместе с docker-compose

# Для WSL docker устанавливается в Windows

sudo apt install docker-compose

# смотреть, есть ли docker в системе
dpkg -l | grep -i docker

# Чтобы запускать docker без sudo
sudo groupadd docker
sudo usermod -aG docker $USER
sudo service docker restart     # или перелогиниться

# проверить установку
docker run hello-world

# Настройка автозапуска при загрузке ОС
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# -------

# подключить диск из под винды (если нужно)
mkdir windows10
fdisk -l         # найти диск под виндой
sudo mount /dev/sda5 /home/chas/windows10

# Скачать яндекс-браузер через браузер и установить через приложение
# Скачать VSCode через браузер и установить через приложение

```