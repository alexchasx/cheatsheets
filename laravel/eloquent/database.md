
### Динамические настройки БД и дебажинг

- Разные соединения для чтения и записи (CQRS):

```php
// config/database.php
'mysql' => [
    'read' => [ /* ... */ ],
    'write' => [ /* ... */ ],
    'sticky' => true, // операции "чтения" используют соединение "запись"
]
```

- Использование нескольких подключений:

```php
$users = DB::connection('sqlite')->select(/* ... */);

$pdo = DB::connection()->getPdo();
```

- Прослушивание событий запроса:

```php
// App\Providers\AppServiceProvider::boot
    DB::listen(function ($query) {
        // $query->sql;
        // $query->bindings;
        // $query->time;
    });
```

- Контроль порогового времени запроса (в миллисекундах):

```php
// App\Providers\AppServiceProvider::boot
    DB::whenQueryingForLongerThan(500, function (Connection $connection) {
        // Уведомить разработчиков...
    });
```

- Транзакции:

```php
DB::transaction(function () {
    DB::update('update users set votes = 1'); 
    DB::delete('delete from posts');
}, 1); // 1 - кол-во повторов при возникновении взаимоблокировки


// Вручную с использованием транзакций
DB::beginTransaction(); // начать транзакцию вручную
try {
    // Что-то делаем ...
    DB::commit(); // совершить транзакцию
} catch {$e} {
    while (DB::transactionLevel() > 0) { // количество активных транзакций
        DB::rollBack(); // откатить транзакцию
    }
} 
```