
DDL - это CREATE, ALTER, DROP

DML - это SELECT, INSERT, UPDATE, DELETE

DCL - это опер-ры доступа к данным
- GRANT - предоставл. разрешения
- REVOKE - отзывает разрешения
- DENY - запрет в приоритете над разрешением

TCL - опер-ры управления транзакциями
- COMMIT
- ROLLBACK
- SAVEPOINT - делит транзакцию на более мелкие участки

### Создание БД

```sql
-- создать БД test
CREATE DATABASE test;

-- с указанием кодировки по умолчанию
CREATE DATABASE test DEFAULT CHARACTER SET utf8;

-- создать, если не существует
CREATE DATABASE IF NOT EXISTS test;

```

### Удаление БД

```sql
DROP DATABASE test;

-- с проверкой на существование
DROP DATABASE IF EXISTS test;

-- переименование
RENAME DATABASE test TO production;
```

### Создание таблицы

```sql
CREATE TABLE IF NOT EXISTS `region` (
  `id`          BIGSERIAL    NOT NULL  PRIMARY KEY,
  `country_id`  BIGINT       NOT NULL,
  `name`       VARCHAR(128) NOT NULL,
  FOREING KEY (`country_id`) REFERENCES `country` (`id`)
);


CREATE TABLE `departament` (
  `id`     int(11) unsidned NOT NULL AUTO_INCREMENT,
  `name`   varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### Удаление таблицы

```sql
DROP TABLE `departament`;

DROP TABLE IF EXISTS `departament`;
```

## Посмотреть список таблиц

```sql
SHOW TABLES;
```

### Типы данных

1) Целочисленные: 
- TYNYINT (здесь же BOOLEAN: 0 - false, остальное - true)
- SMALLINT
- MEDIUMINT
- INT
- BIGINT

    UNSIGNED - без знака (запрещает указывать отрицат. значения)

2) Дробные числа: 
- FLOAT(M.D)
- DOUBLE(M.D)
- DECIMAL(M.D) (подходит для хранения денег)

    M - кол-во отводимых под число символов
    D - кол-во символов дробной части

3) Строки
- VARCHAR (переменная длина)
- CHAR (фиксированная длина. Дополняется справа пробелами при недост. длине)

4) Текстовые
- TINYTEXT
- TEXT
- MEDIUMTEXT
- LONGTEXT

5) Бинарные
- TINYBLOB
- BLOB
- MEDIUMBLOB
- LONGBLOB

6) Составные
- SET
- ENUM (недостаток: список строк фиксирован, а для добавления или удаления нужно выполнять ALTER TABLE)

7) Время
- DATE      (YYYY-MM-DD)
- DATETIME  (YYYY-MM-DD HH:mm:SS) - поддерж. дробн. части сек.
- TIMESTAMP  (в сек.) - поддерж. дробн. части сек.
- TIME      (HH:mm:SS) - поддерж. дробн. части сек.
- YEAR      (YYYY)

### NULL
Обозначает отсутствующее или неизвестное значение.
Для сравнения с NULL использ-ся `IS NULL` или `IS NOT NULL`

### Принципы создания физической модели данных

- Стараться испол-ть типы данных минимального размера (экономия оперативки при доставании)
- Сравнение чисел проще чем строк, т.к. не учит-ся кодировки
- Используйте встроенные типы (не исп. строки для дат)
- Старайтесь избегать значений NULL (усложняет работу БД, порождает неопределенности)



## Внешние ключи

```sql
CREATE TABLE `departament` (
  `id`     int(11) unsidned NOT NULL AUTO_INCREMENT,
  `name`   varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  FOREING KEY (`departament_id`) REFERENCES `departament` (`id`)
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
-- или (удалять связанные данные)
    ON UPDATE CASCADE
    ON DELETE CASCADE
-- или (устанавливать NULL при удалении/изменении связанных данных)
    ON UPDATE SET NULL
    ON DELETE SET NULL
-- или
    ON UPDATE SET DEFAULT
    ON DELETE SET DEFAULT
-- или (можно по разному задавать)
    ON UPDATE SET NULL
    ON DELETE RESTRICT

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```


## INSERT

```sql
INSERT INTO `departament` VALUES (1, 'Отдел разраб-ки');
-- порядок значений важен


INSERT INTO `departament` 
(`name`,          `id` ) VALUES 
('Отдел дизайна',   2  );


-- игнорирование ошибок
INSERT IGNORE INTO `departament` 
(`name`,          `id` ) VALUES 
('Отдел дизайна',   2  );


-- можно так
INSERT INTO `departament` SET `name` = 'Бухгалтерия';


-- многострочная вставка
INSERT IGNORE INTO `departament` 
(`name`,           `id` ) VALUES 
('Отдел дизайна',    2  );
('Отдел разработки', 3  );
('Отдел маркетинга', 4  );
```

Домашнее задание:
- Пакетная загрузка
- mysqlimport
- INSERT DELAYED
- Использование выражения в INSERT


### Агрегационные функции и AS

- COUNT(expr) - expr м.б. "*" или имя атрибута
- MIN(expr)
- MAX(expr)
- AVG(expr) - среднее арифметическое значение
- SUM(expr)

```sql
SELECT COUNT(*) FROM `workers`;

SELECT COUNT(`salary`) FROM `workers`;

SELECT MAX(`salary`) FROM `workers`;

SELECT AVG(`salary`) FROM `workers`;
```

Задача: выбрать отдельно зарплату, премию и сумму зарплаты и премии одновременно.

```sql
SELECT `name`, `salary`, `bonus`,
  (`salary` * `bonus`/100) AS `bonus_money`,
  (`salary` + `salary` * `bonus`/100) AS `total`,
FROM `workers`;

SELECT SUM(`salary` + `salary` * `bonus`/100) AS `total`,
FROM `workers`;
```


### Строковые функции
- CONCAT(str1, str2, ...) - склевание строк
- SUBSTRING(str, pos, len) - поиск подстроки
- REPLACE(str, from_str, to_str) - замена строк

```sql
SELECT CONCAT(`Имя: `, `name`, `; Должность: `, `role`) as `description`
FROM `workers`

SELECT REPLACE(`name`, `a`, `A`) as `new_name` FROM `workers`
```


### Математические функции
- ABS(X) - возр. абсолютное знач.
- MOD(N, M) - остаток от деления N на M
- ROUND(X) - округление до ближайшего целого


### Функции работы с датами и временем
- NOW()
- WEEKDAY(X) - возр. индекс дня недели для аргумента (0 - понедльник)
- DAYOFMONTH(X) - порядковый номер дня месяца
- MONTH(X)
X - дата

```sql
SELECT MONTH(`birthday`) as `birthday_month` FROM `workers`;
```

### UNION - объединение 2-х и более запросов
Требования:
- Одинаковое кол-во и совместимость по данным выходных столбцов
- В результир. данных имена столбцов будут совпадать со столбцами первого запроса
- Можно применять ORDER BY ко всем результатам и указывать его можно только в конце всего запроса

```sql
SELECT `id`, `name` FROM `workers`
UNION
SELECT `id`, `name` FROM `old_workers`
```

### GROUP, HAVING

```sql
-- выбрать все роли без дубликатов
SELECT DISTINCT `role` FROM `workers`;
-- аналогично
SELECT `role` FROM `workers` GROUP BY `role`;

-- кол-во всех (плюс дубли)
SELECT COUNT(`role`) FROM `workers`;

-- кол-во уникальных ролей
SELECT COUNT(DISTINCT `role`) FROM `workers`;

-- кол-во по сгруппированным значениям
SELECT `role`, COUNT(`role`) as `count` FROM `workers` GROUP BY `role`;

-- условие на агрегацию (выбрать роли и ср.ЗП по ролям, где ср.ЗП д.б. больше 20К)
-- HAVING работает как WHERE, но уже после группировки
SELECT `role`, AVG(`salary`) as `avg_salary` 
FROM `workers` 
HAVING `avg_salary` > 20000
GROUP BY `role`;

-- Просто `name` не сработает. Применяем либо ANY_VALUE,
-- либо группировать еще и по `name`
SELECT `role`, ANY_VALUE(`name`), AVG(`salary`) as `avg_salary` 
FROM `workers` 
GROUP BY `role`;

```


### CROSS JOIN, INNER JOIN

```sql
-- JOIN = CROSS JOIN
-- перемножит две таблицы (крест накрест)
SELECT * FROM users JOIN departments;
-- аналогично 
SELECT * FROM users CROSS JOIN departments;

-- INNER JOIN + ON = JOIN + ON
SELECT * FROM users 
JOIN departments ON user.id = departments.id;

-- можно добавлять условия
SELECT * FROM users 
JOIN departments ON user.id = departments.id
WHERE users.id > 1;
```


### LEFT JOIN, RIGHT JOIN

```sql
-- левая таблица будет выведена вся
SELECT * FROM users 
LEFT JOIN departments ON user.id = departments.id;

SELECT * FROM users 
RIGHT JOIN departments ON user.id = departments.id;

-- Вывести имена всех сотрудников, которые работают над проектами 
-- в названии которых есть буква "р" (три таблицы)
SELECT `workers`.`name` FROM `workers`
JOIN `projects_workers` ON `worker`.`id` = `project_workers`.`worker_id`
JOIN `projects` ON `projects`.`id` = `project_workers`.`project_id`
WHERE `project`.`name` LIKE '%h%'
GROUP BY `workers`.`name`;
```

### DELETE, TRUNCATE

```sql
-- удалить всё из таблицы
DELETE FROM `workers`;

-- удалить по условию
DELETE FROM `workers` WHERE `id` = 2;

-- удалить 2-х самых молодых сотрудников
DELETE FROM `workers` ORDER BY `birthday` LIMIT 2;

-- Удаляет все данные
-- Не допускает никаких условий
-- Сбрасывает счетчик автоинкремента
-- Работает быстрее, чем DELETE
TRUNCATE TABLE `workers`;

-- Многотабличное удаление (например, из таблиц `workers`, `projects_workers` и `projects`)
DELETE `workers`, `projects_workers`
FROM `workers`, `projects_workers`
WHERE `workers`.`id`=`projects_workers`.`workers_id`
  AND `workers`.`id` = 3;
```


### UPDATE
```sql
UPDATE `workers` SET `name` = `Пример`;

UPDATE `workers` SET `name` = `Пример` 
WHERE `id` = 3
ORDER BY `id` LIMIT 1;

-- Можно накладывать выражения как в SELECT
UPDATE `workers` SET `salary` = `salary` * 1.1;

-- Можно проводить манипуляции с несколькими столбцами
UPDATE `workers` 
SET `salary` = `salary` * 1.1, `role` = 'Мастер'
WHERE `role` = 'Разнорабочий';

UPDATE + JOIN

```


### Вложенные запросы (Подзапросы)

```sql
-- Выбрать сотрудников с зарплатой выше средней:
SELECT * FROM `workers`
WHERE `salary` > (SELECT AVG(`salary`) FROM `workers`);

-- Выбрать всех сотрудников из отдела, в котором работает самый высокооплачиваемый сотрудник
SELECT * FROM `workers` WHERE `department_id` = (
  SELECT `department_id` FROM `workers` WHERE `salary` = (
    SELECT MAX(`salary`) FROM `workers`
  )
);

-- Выбрать все отделы, в которых работает больше 1 сотрудника
SELECT * FROM `departments` WHERE `id` IN (
  SELECT `department_id` FROM `workers`
  GROUP BY `department_id` HAVING COUNT(*) > 1
);

-- Выбрать отделы с указанием средней зарплаты в каждом из них
SELECT *, (
  SELECT AVG(`salary`) FROM `workers`
  WHERE `workers`.`department_id` = `departments`.`id`
) as `avg_salary` FROM `departments`;

```
Подзапросы можно указывать в секции FROM / JOIN.

Ограничения подзапросов:
- Нельзя изменять/удалять данные в таблице, если ее данные используются в подзапросе этого запроса
- Не поддерживается LIMIT в подзапросах

Производительность:
- По возможности стоит избегать подзапросов
- Использовть как можно меньше уровней вложенности подзапросов


### DESCRIBE, ALTER

```sql
-- Описание структуры таблицы
DESCRIBE `workers`;

-- Добавление столбцов в таблицу
ALTER TABLE `workers`
ADD COLUMN `last_name` varchar(255) FIRST `name`,
ADD COLUMN `middle_name` varchar(255) AFTER `name`;
```

