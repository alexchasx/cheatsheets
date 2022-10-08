
# Удалить MySQL
https://losst.ru/kak-udalit-mysql-v-ubuntu


# Работа с mysql
https://jeka.by/post/1003/rabotaem-s-mysql-cherez-komandnuyu-stroku/


```bash

sudo systemctl stop mysql
# или
sudo systemctl stop mysql.service

sudo systemctl start mysql
# или
sudo systemctl start mysql.service

#
sudo systemctl status mysql
sudo systemctl restart mysql

# запустить в WSL
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


Решение проблемы "su: предупреждение: не могу поменять каталог на /nonexistent: Нет такого файла или каталога":
```bash
sudo service mysql stop
sudo usermod -d /var/lib/mysql/ mysql
sudo service mysql start
```


