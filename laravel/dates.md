
# Настройка формата даты в Laravel. Конспект

В разных местах сайта может быть разный формат дат:

- Поля Базы данных должны быть в формате YYYY-MM-DD.
- В шаблонах должен быть человекопонятный формат.
- JavaScript datepicker: форматы дат в JS не совпадают с форматами PHP.

## Способы форматирования дат

1) В контроллере
```php
public function store(Request $request)
{
    $data = $request->all();

    $data['transaction_date'] = Carbon::createFromFormat('m/d/Y', $request->transaction_date)
        ->format('Y-m-d');
    // ...
}
```

2) Использовать мутаторы в модели:
```php
public function setTransactionDateAttribute($value)
{
    $this->attributes['transaction_date'] = Carbon::createFromFormat('m/d/Y', $value)
        ->format('Y-m-d');
}

public function getTransactionDateAttribute($value)
{
    return Carbon::parse($value)->format('m/d/Y');
}
```