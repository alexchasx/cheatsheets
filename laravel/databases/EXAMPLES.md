
# Примеры запросов в БД

Получить только тух, польз-й которые оставили хотя бы один комментарий

```php
$commenters = DB::table('users')
    ->whereExists(function ($query) {
        $query->select('id')
            ->from('comment')
            ->whereRow('comment.user_id = users.id');
    })
    ->get();
```

