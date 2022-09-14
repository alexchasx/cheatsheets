# Установка LAMP
https://itchief.ru/php/web-server-on-wsl

```bash
# Обновим Linux
sudo apt update
sudo apt upgrade

# Установим mc (необязательно)
sudo apt install mc

# Установим Apache
sudo apt install apache2

# Установим MySQL сервер
sudo apt install mysql-server

# Установим php и другие пакеты
sudo apt install php libapache2-mod-php php-mysql php-xml php-curl

# Для установки какой-то определённой версии php, например 7.1.x
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php7.1 libapache2-mod-php7.1 php7.1-mysql php7.1-xml php7.1-curl

# Включим модуль Mod rewrite в Apache
sudo a2enmod rewrite

# Создание директории для веб-проекта
\home\main\projects\test.ru\public_html

#


```

## Изменение метода аутентификации MySQL пользователя root

```bash
# Запустим службу mysql и войдём
sudo service mysql start
# по умолчанию пользователь root не имеет пароля
sudo mysql -uroot -p

# Проверим метод аутентификации, который используется для пользователя root
SELECT user, authentication_string, plugin, host FROM mysql.user WHERE user="root";

# Если использ-ся auth_socket, то изменить на использование пустого пароля:
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';

# применит внесённые изменения:
FLUSH PRIVILEGES;

```

## Создание базы данных

```bash
CREATE DATABASE testru;

# загрузить дамп некоторой базы:
use testru;
source backup.sql;

# выход
exit

```

## Настройка виртуальных хостов в Apache

## Команды для запуска и остановки веб-сервера

## Инструкция по установке phpMyAdmin