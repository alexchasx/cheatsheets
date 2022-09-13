### Добавление записей в БД с помощью консольной утилиты "tinker"


```bash

# Создаём основную запись

>>> use Illuminate\Support\Facades\Hash;
>>> use App\Models\User;
>>>  $user = User::create(['name' => 'admin',
... 'email' => 'admin@bboard.ru',
... 'password' => Hash::make('admin')]);


### Использование связи "один ко многим"

# 1-й способ:

>>> use App\Models\Bb;
>>> $bb = new BB();
>>> $bb->title = 'Пылесос';
>>> $bb->content = 'Старый, без шланга';
>>> $bb->price = 500;
>>> $user->bbs()->save($bb);

# 2-й способ:

>>> $user->bbs()->create(['title' => 'Грузовик',
... 'content' => 'Грузоподъмность - 5 т',
... 'price' => 1000000]);

# 3-й способ:

>>> $bb = new Bb(['title' => 'Шкаф',
... 'content' => 'Совсем новый, полированный, двухстворчатый',
... 'price' => 1000]);
>>> $bb->user()->associate($user);
>>> $bb->save();

```
