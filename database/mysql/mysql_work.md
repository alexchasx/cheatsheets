
# Удалить MySQL
https://losst.ru/kak-udalit-mysql-v-ubuntu


# Работа с mysql
https://jeka.by/post/1003/rabotaem-s-mysql-cherez-komandnuyu-stroku/


```bash
#
sudo systemctl status mysql
sudo systemctl restart mysql
sudo systemctl stop mysql
sudo systemctl start mysql

# или
sudo /etc/init.d/mysql status
sudo /etc/init.d/mysql restart
sudo /etc/init.d/mysql stop
sudo /etc/init.d/mysql start


# подключиться
mysql -u root

```

```mysql
<!-- показать все БД -->
SHOW DATABASES;

<!-- переключиться на БД "mybd" -->
use mybd;

SHOW TABLES;

CREATE DATABASE staff;

SELECT * FROM mysql;

SELECT <список полей> FROM <список названий таблиц> [WHERE <список условий>] [ORDER BY <список полей>];

SELECT name, project, works_since
FROM staff
WHERE
name > 'Иван' AND
works_since '1998-04-26';
```

# Войти в Mysql под Docker 
laravel-orchid-blog-mysql-1  - имя образа с MYSQL
```bash
docker exec -it laravel-orchid-blog-mysql-1 mysql -uroot -p
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