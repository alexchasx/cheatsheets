```sql

-- JSONB:

-- Показать значение свойства "age"
select '{"age": 12, "name": "vasia"}'::jsonb -> 'age';

-- с преобразованием типа в строку (->>)
select '{"age": 12, "name": "vasia"}'::jsonb ->> 'age';

-- JSON:

-- Получить элмент массива по ключу (результат: {"b":2})
SELECT '[{"a":1},{"b":2},{"c":3}]'::JSON -> 1;

--  результат: 2
SELECT '[{"a":1},{"b":2},{"c":3}]'::JSON -> 1 -> 'b';

-- используем #> для получения объекта JSON в объекте JSON
--  результат: {"ba":"b1","bb":"b2"}
SELECT '{"a":1,"b":{"ba":"b1","bb":"b2"},"c":3}'::JSON #> '{b}'

--  результат: "b1"
SELECT '{"a":1,"b":{"ba":"b1","bb":"b2"},"c":3}'::JSON#>'{b}'->'ba'

```

```php
// где `currentUser->id` содержится в массиве `visible_users` или `visible_users` пуст
->where(function($query) use ($currentUser) {
    $query->whereRaw("visible_users::jsonb @> '$currentUser->id'::jsonb");
    $query->orWhere('visible_users', '[]');
})


::whereRaw('branches_ids::jsonb @> \'['.$data['branch']['id'].']\'::jsonb')
```

```sql
-- Конкатенация при помощи ||
-- result: {"age": 45, "name": "Marie", "city": "Paris"}
SELECT '{"name": "Marie","age": 45}'::jsonb || '{"city": "Paris"}'::jsonb;

-- Удаление при помощи '-'
-- {"name": "Karina"}
SELECT '{"name": "Karina","email": "karina@localhost"}'::jsonb - 'email';
-- ["animal", "mineral"]
SELECT '["animal","plant","mineral"]'::jsonb - 1;

-- Удаление при помощи #-
-- Разница в сравнении с оператором - заключается в том, 
-- что #- оператор может удалить вложенную пару ключ/значение, если путь до нее указан
-- result: {"name": "Claudia", "contact": {"phone": "555-5555"}}
SELECT
    '{"name": "Claudia",
      "contact": {
          "phone": "555-5555",
          "fax": "111-1111"}}'::jsonb #- '{contact,fax}'::text[];
     
```
