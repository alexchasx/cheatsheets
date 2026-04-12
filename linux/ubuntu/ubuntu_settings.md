# Мои настройки Ubuntu 22.04 для веб-разработки на PHP (конспект)

```
sudo apt update && sudo apt upgrade
```


### Создание точки восстановления системы с помощью `timeshift`
```
sudo apt install timeshift
```
Открыть `timeshift` (ищем в меню приложений) и настроить первую точку восстановления

### Установка полезных пакетов
https://github.com/proffix4/dev_for_ubuntu22/blob/main/BASE_SOFT_INSTALL.sh

```
sudo apt install gthumb retext qbittorrent gtkhash \
		img2pdf okular okular-extra-backends calibre -y
sudo apt install gnome-shell-extension-manager \ 
		menulibre pdfarranger drawing -y
sudo apt install curl wget xfburn gparted \ 
		synaptic gdebi smartmontools pavucontrol -y

gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'

sudo apt install telegram-desktop -y
sudo snap install whatsie
sudo snap install obs-studio
sudo snap set system refresh.retain=2

sudo apt install default-jdk -y

sudo apt-get install git -y
# укажите ваше имя и почту ниже
git config --global user.name "sdfsdf"
git config --global user.email "sdfsdf@gmail.com"

sudo apt install p7zip-full p7zip-rar -y
```

### Установка браузера `Firefox Developer Edition`

https://dev.to/harrsh2124/how-to-setup-firefox-developer-edition-on-ubuntu-4inp

Cкачать с оф. сайта файл типа `firefox*.tar.bz2`
```
sudo cp -rp firefox*.tar.bz2 /opt
sudo rm -rf firefox*.tar.bz2
cd /opt
sudo tar xjf firefox*.tar.bz2
sudo rm -rf firefox*.tar.bz2
sudo chown -R $USER /opt/firefox
nano ~/.local/share/applications/firefox_dev.desktop

# содержимое файла
[Desktop Entry]
Name=Firefox Developer 
GenericName=Firefox Developer Edition
Exec=/opt/firefox/firefox %u
Terminal=false
Icon=/opt/firefox/browser/chrome/icons/default/default128.png
Type=Application
Categories=Application;Network;X-Developer;
Comment=Firefox Developer Edition Web Browser.
StartupWMClass=Firefox Developer Edition
# конец файла

chmod +x ~/.local/share/applications/firefox_dev.desktop
```

### Установка php и некоторых модулей к нему
```
sudo apt install php8.1 -y
sudo apt install php8.1-common php8.1-mysql php8.1-xml \
 php8.1-xmlrpc php8.1-curl php8.1-gd php8.1-imagick  \
 php8.1-cli php8.1-dev php8.1-imap php8.1-mbstring \
 php8.1-opcache php8.1-soap php8.1-zip php8.1-intl php8.1-fpm -y 
```

### Установка composer 2
```
sudo apt install php-cli unzip
cd ~
curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
sudo php /tmp/composer-setup.php --install-dir=/usr/local/bin \
    --filename=composer

# проверка
php /usr/local/bin/composer

# добавим alias "composer"
cd ~
mcedit .bashrc
# добавить в конец файла:
alias composer='php /usr/local/bin/composer'

# запуск новой конфигурации
source ./.bashrc

# проверка
composer -v
```

### Установка Node.js и npm
Версию меняем на нужную.
```
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Установка MySQL
```
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql.service
sudo mysql_secure_installation

# Если не получится изменить пароль - перезапускаем терминал и пишем следующее

sudo systemctl stop mysql.service
sudo systemctl set-environment MYSQLD_OPTS="--skip-grant-tables"
sudo systemctl start mysql.service
sudo mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PassW0Rd++';
UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root';
FLUSH PRIVILEGES;
SELECT user,authentication_string,plugin,host FROM mysql.user;
quit

systemctl stop mysql.service
sudo systemctl unset-environment MYSQLD_OPTS
sudo systemctl start mysql.service

sudo snap install mysql-workbench-community
```
После установки `mysql-workbench`, найдите его в приложении `Ubuntu Software` и поставьте галочки в `Permissions`. Тоже самое проделайте и для других пакетов (например, для WhatSie)

### Установка Nginx

```bash
sudo apt update
sudo apt install nginx

# Настройка брандмауэра 
sudo ufw app list

sudo ufw allow 'Nginx HTTP'
sudo ufw status
sudo ufw enable

systemctl status nginx
# если apache мешает
sudo service apache2 stop
sudo update-rc.d apache2 disable

```

### Установка docker и docker-compose
https://totaku.ru/ustanovka-docker-i-docker-compose-na-ubuntu-22-04/


### Настройка псевдонимов команд и консоли

```
cd ~
nano .bashrc
```
Вставляем в конец файла

```
# двойная строка и подсветка ветки git
git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\
\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\
$(git_branch)\n\[\033[00m\]\[\033[0;31m\]\$\[\033[0;33m\] '


#======== my aliases

alias composer='php /usr/local/bin/composer'

# git
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m $*'
alias gaf='git add $*'
alias gaa='git add -A'
alias gpl='git pull'
alias gps='git push'
alias gca='git commit -a $*'
alias gcam='git commit -am $*'
alias gch='git checkout $*'
alias gchf='git checkout -f'
alias gbr='git branch'
alias gl='git log'
alias glpo='git log --pretty=oneline'
alias glpon='git log --pretty=oneline -n $*'

# docker
alias d1='docker-compose up -d'
alias d2='docker-compose down'
alias d3='docker exec -it cot_app bash'
alias d4='docker exec -it cot_db bash'
alias d5='docker exec -it cot_nginx bash'

# laravel
alias pa='php artisan $*'  
alias paclear='php artisan cache:clear && php artisan view:clear && php artisan route:clear && php artisan config:clear && php artisan clear-compiled'
alias sail='[ -f sail ] && sh sail || sh vendor/bin/sail'

alias m0='php artisan make:migration $'
alias m1='php artisan migrate'
alias m2='php artisan migrate:rollback'

# other
alias n1='npm run watch'
alias aliases='tail -n 45 ~.bashrc'
alias h='history'
alias c='clear'
alias up='sudo apt update && sudo apt upgrade'
alias scode='sudo code --no-sandbox --user-data-dir ~/supercode'
alias psnginx='echo "command: ps -ax | grep nginx"; ps -ax | grep nginx'
alias nanobash='sudo nano ~/.bashrc'
alias source='source ~/.bashrc'
```
Сохраняем, выходим из редактора и сохраняем настройки командой
```
source ~/.bashrc
```
### Установить gnome-tweaks
```
sudo apt-get install gnome-tweaks
```

### установка Docker и docker-compose
https://timeweb.cloud/tutorials/docker/kak-ustanovit-docker-na-ubuntu-22-04

## Настройка прав для Docker
sudo groupadd docker 
sudo gpasswd -a $USER docker 


## Установка проприетарных драйверов

```bash
sudo apt install software-properties-gtk
software-properties-gtk --open-tab=4 
# выбрать версию драйвера

sudo apt search nvidia-driver
# пример
sudo apt install nvidia-driver-550
```