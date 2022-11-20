### Service Container (SC) 
Это инструмент управления зависимостями классов.
Используется внедрение зависимости через аргументы конструктора или сеттера.

```php
    public function __construct(private UserRepository $users)
    {}
```

### Неконфигурируемое внедрение

```php
    class Service
    {/** */}

    Route::get('/', function (Service $service) {/** */});
```

### Связывание

```php
// связывание интерфейсов и реализаций
$this->app->bind(EventPusher::class, RedisEventPusher::class);

$this->app->bind(
    Transistor::class, function ($app) {
        return new Transistor(
            $app->make(PodcastParser::class));
});

// или
App::bind(
    Transistor::class, function ($app) {
        // ...
});

// связ. класс, кот. должен быть извлечен только один раз
$this->app->singleton(
    Transistor::class, function ($app) {
        return new Transistor(
            $app->make(PodcastParser::class));
});

// Связывание singleton с заданной областью действия
$this->app->scoped(
    Transistor::class, function ($app) {
        return new Transistor(
            $app->make(PodcastParser::class));
});

// привязать существующий экземпляр
$service = new Transistor(new PodcastParser);
$this->app->instance(Transistor::class, $service);
```
