### Режим обслуживания (отображение спец. страницы о тех. работах)

Выбрасывает HttpException с 503 кодом состояния

Cвой шаблон для режима обслуживания: `resources/views/errors/503.blade.php`

```bash
php artisan down
php artisan up

php artisan down --refresh=15
    # обновлять страницу через каждые 15 сек

php artisan down --retry=60
    # установить значение в Retry-After HTTP

php artisan down --secret="1630542a-246b-4b66-afa1-dd72a4c43515"
    # указать токен для обхода режима обслуживания
    # использовать: https://example.com/1630542a-246b-4b66-afa1-dd72a4c43515

php artisan down --render="errors::503"
    # предварительный рендеринг шаблона (отобразит в самом начале цикла запроса)

php artisan down --redirect=/
    # перенаправить все запросы на URI /
```

Альтернативы режиму обслуживания: Laravel Vapor и Envoyer