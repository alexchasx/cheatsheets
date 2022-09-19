
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


```bash

```


