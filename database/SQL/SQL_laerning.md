
DDL - CREATE, ALTER, DROP

DML - SELECT, INSERT, UPDATE, DELETE

DCL - опер-ры доступа к данным
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