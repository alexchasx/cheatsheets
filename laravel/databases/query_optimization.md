
# Конспект по оптимизации запросов к БД в Laravel.


1) Сокращайте использование памяти, разбивая набор записей на части.

```php
$posts = Post::chunk(100, function($posts) {
    foreach ($posts as $post){
        // ...  
    }
});
```

2) Не используйте `select *` (выбор всех полей).

Лучше так:

```php
// только поля 'id' и 'name'
$posts = Post::where('name','=', 'vasia')
    ->first(['id', 'name']);
```


3) Правильно считайте кол-во записей в таблице.

Правильно:

```php
// select count(*) from posts
$posts = Post::count();     
// или
$posts = DB::table('posts')->count();
```

Не правильно:

```php
// ( select * from posts )->count()
$posts = Post::all()->count();  
// или
$posts = DB::table('posts')->get()->count();
```

4) Избегайте проблемы `N+1`. Используйте `жадную загрузку`.

Проблема `N+1` - это, когда для каждой записи основной таблицы запроса выполняются множество дополнительных запросов к связанной талице. Вместо этого можно один запрос к связанной таблице.

```php
// избегайте делать так
$posts = Post::all();
// лучше делайте так
$posts = Post::with(['user'])->get();
```

Эта же проблема может возникать с вложенными отношениями. Решается так:

```php
$posts = Post::with(['user.team'])->get();
```

5) Используйте индексацию для часто запрашиваемых полей.

```php
// Миграция
Schema::table('posts', function (Blueprint $table) {
   $table->index('email');
});
```

6) Предпочитайте использовать `simplePaginate` вместо `Paginate`.
simplePaginate - не может считать общее кол-во записей.

7) Выделяйте поля с большими данными в отдельную таблицу.

8) Для получения последней записи `id` лучше, чем `created_at` (сортировка по `id` быстрее).

Лучше:
```php
$posts = Post::latest('id')->get();
// или
$posts = Post::orderBy('id', 'desc')->get();

```
Хуже:
```php
$posts = Post::latest()->get();
// или
$posts = Post::orderBy('created_at', 'desc')->get();
```