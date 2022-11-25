
# Настройка формата даты в Laravel. Конспект

В разных местах сайта может быть разный формат дат:

- Поля Базы данных должны быть в формате YYYY-MM-DD.
- В шаблонах должен быть человекопонятный формат.
- JavaScript datepicker: форматы дат в JS не совпадают с форматами PHP.


```php
// Способы форматирования дат

// 1) В контроллере
public function store(Request $request)
{
    $data = $request->all();

    $data['transaction_date'] = Carbon::createFromFormat('m/d/Y', $request->transaction_date)
        ->format('Y-m-d');
    // ...
}


// 2) Использовать мутаторы в модели:
class Role extends Model
{
    public function setTransactionDateAttribute($value)
    {
        $this->attributes['transaction_date'] = Carbon::createFromFormat('m/d/Y', $value)
            ->format('Y-m-d');
    }

    public function getTransactionDateAttribute($value)
    {
        return Carbon::parse($value)->format('m/d/Y');
    }
    // ...
}

// -----------------------------

class Role extends Model
{
    // отключить автоматические метки времени
    public $timestamps = false;
    
    // Изменение названия полей меток времени
    const CREATED_AT = 'create_time';
    const UPDATED_AT = 'update_time'; 
    
    // Изменить формат меток времени
    protected $dateFormat = 'U';
        
    // если вы хотите сохранять автоматически метки времени
    // в промежуточных таблицах
    public function roles()
    {
        return $this->belongsToMany(Role::class)->withTimestamps();
    }
}


// Сортировка меток времени 
User::latest()->get();  // по полю created_at (по убыв.)
User::oldest()->get();  // по полю created_at (по возр.)
$adf = User::newest('updated_at')->first(); // по другому столбецу


// Обновление без updated_at
$user = User::find(1);
$user->profile_views_count = 123;
$user->timestamps = false;
$user->save();


// Обновить только update_at
$user->update(['updated_at' => now()]);
// или
$user->touch();


// обновить не только updated_at текущей модели Eloquent, 
// но и родительскую запись в отношениях
class Comment extends Model {
    protected $touches = ['post'];
    public function post()
    {
        return $this->belongsTo('Post');
    }
}


// можно выполнять Carbon-операции без преобразования в экземпляр Carbon
$user->created_at->addDays(3);
now()->diffInDays($user->updated_at);
```