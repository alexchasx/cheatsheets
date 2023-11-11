
- скопировать дамп в OSPanel/userdata/

```
cd userdata

```

## MySQL

```
mysql -u root -p elcomspb < elcomspb.sql

```

---

## PostgreSQL

```
psql -U postgres
create database cot;
\q
psql -U postgres cot < data12_10_2023.dump

```


```
php artisan migrate

```