
```sql
-- Описание структуры таблицы
DESCRIBE `products`;

SELECT COUNT(*) FROM `product`;
-- Кол-во записей 6 млн.


SELECT * FROM products WHERE vendor = 'ZEUS' LIMIT 100 OFFSET 1500;
-- Произойдет полное сканирование бд, кот. может занять более 1.8 сек.

-- Кол-во вендоров без дуликатов:
SELECT COUNT(DISTINCT vendor) FROM products;
-- 4085


```

# B-Tree Index

```sql
-- Добавляем индекс по vendor
ALTER TABLE products ADD INDEX vendor (vendor);

-- Посмотреть индексы таблицы
SHOW INDEX FROM products;
```

```sql
-- Тестовый запрос
SELECT * FROM products
WHERE price = 9990 and category = 'Телевизоры';
-- Время выполения 1.6 сек

-- Добавляем индекс
ALTER TABLE products
ADD INDEX price_category (price, category);
-- или ??
ALTER TABLE products
ADD INDEX category_price (category, price);
-- Первый индекс продуктивнее (price_category)

```
Чем меньшему кол-ву строк соотв-ет значение атрибута, тем выше селективность. Такие атрибуты следует использовать в начале индекса.

```sql
SELECT * FROM `products` WHERE `price` = 9990 and `category` = 'Телевизоры' 
ORDER BY    `year`;
```

Атрибуты в ORDER BY необходимо добавлять в "хвост" составного индекса.
```sql
ALTER TABLE products
ADD INDEX price_category_year (price, category, year);
```

Посмотрим какие индексы будут использоваться для этого запроса
```sql
EXPLAIN SELECT * FROM `products` 
WHERE `price` = 9990 and `category` = 'Телевизоры';
```