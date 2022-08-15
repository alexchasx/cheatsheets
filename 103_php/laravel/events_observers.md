
# Конспект по созданию события или наблюдателя в Laravel

1) Создать класс-событие и класс-обработчик через консоль:
```bash
php artisan make:event ArticleCreated   # По умолчанию в `app/Events`

# По умолчанию в `app/Listeners`
php artisan make:listener ClearSidebarCache [--event] [--queued]
# --event  - привязка к событию: путь к классу-событие
# --queued - добавить в очередь: имплементировать `Illuminate\Contracts\Queue\ShouldQueue`
```

2) Зарегистрировать их в `app\Providers\EventServiceProvider`:
```php
    protected $listen = [
        ArticleCreated::class => [
            ClearSidebarCache::class,   // обработчик
            // ...
```

3) Внедрить зависимости в класс события:
```php
    public function __construct(public Article $article)
    {}
```

4) Внедрить зависимости и логику в обработчик:
```php
    public function handle(ArticleCreated $event) 
    { /* код */ }
```


5) Прописать генерацию события в нужном месте:
```php
    Illuminate\Support\Facades\Event::dispatch(new ArticleCreated($article));
    // или (медленнее)
    event(new ArticleCreated($article));

```

6) Если нужно добавить в очередь - имплементировать в обработчик `Illuminate\Contracts\Queue\ShouldQueue`:
```php
class ClearSidebarCache implements ShouldQueue
{
```

## Наблюдатели (Observers)

1) Создать наблюдатель за моделью Rubric:
```bash
# По умолчанию в `app/Observers`
php artisan make:observer RubricObserver --model=Rubric

```

2) Связать с моделью в `app\Providers\EventServiceProvider`:

```php
    public function boot() {
        Rubric::observe(RubricObserver::class);
```

3) Редактировать класс наблюдателя:
```php
    public function created(Rubric $rubric)
    {
        Rubric::updateCache();
```