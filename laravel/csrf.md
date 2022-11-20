### CSRF - межсайтовая подделка запроса

Laravel автоматически генерирует токен CSRF для каждого активного сеанса пользователя.

Laravel хранит текущий токен CSRF в зашифрованном XSRF-TOKEN cookie.

В `resources/js/bootstrap.js` библиотека Axios автоматически отправит X-XSRF-TOKEN.

```php
$token = $request->session()->token();
// или
$token = csrf_token();

// шаблон Blade
<form method="POST" action="/profile">
    @csrf
    // или
    <input type="hidden" name="_token" value="{{ csrf_token() }}" />
</form>
```

`App\Http\Middleware\VerifyCsrfToken` - мидлвар, отвечающий за проверку токена


```php
// Исключение URI из CSRF Protection

class VerifyCsrfToken extends Middleware
{
    protected $except = [
        'stripe/*',
        'http://example.com/foo/*',
    ];
}
```

```php
// дополнительная проверка заголовка X-CSRF-ТОКЕН во всех запросах
// токен в metaтеге HTML
<meta name="csrf-token" content="{{ csrf_token() }}">
```
```js
// на основе AJAX с использованием устаревшей технологии JavaScript
$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

```
