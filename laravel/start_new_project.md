Загрузим Laravel в папку `new_project` и перейдем внутрь
(`--prefer-dist` - не загружать всю историю зависимостей VCS)
```bash
composer create-project laravel/laravel --prefer-dist new_project
cd new_project
```

Сгенерируем уникальный ключ `APP_KEY` в файле `.env`
```bash
php artisan key:generate --ansi
```

Сгенерируем базовый пользовательский интерфейс (UI)
```bash
composer require laravel/ui
```

Добавим `Bootstrap`
```bash
php artisan ui bootstrap
```

Устанавливаем UI авторизации
```bash
php artisan ui:auth
```

Если нужен UI для `Vue.js`
```bash
php artisan ui vue
```

Установка npm-зависимости (см. `package.json`)
```bash
npm install
```

Если нужно для исправления зависимостей
```bash
npm audit fix --force
```

Здесь можно вернуться к `Mix` вместо `Vite` (это отдельная история).

Запустим конвертацию ресурсов HTML и CSS:
```bash
npm run dev
```
или
```bash
npm run watch
```

Здесь создаём БД.

Запускаем миграции
```bash
php artisan migrate --seed
```

Генерируем тестовые данные
```bash
php artisan db:seed
```

Создаем симлинк для хранилища файлов
```bash
php artisan storage:link
```

Установим `debugbar` (<a class="link" href="https://github.com/barryvdh/laravel-debugbar">https://github.com/barryvdh/laravel-debugbar</a>)
```bash
composer require barryvdh/laravel-debugbar --dev
```
В файле `.env` проверим `APP_DEBUG=true`.

В файл `config/app.php` добавим в соответствующий массив

```php
Barryvdh\Debugbar\ServiceProvider::class,
```

и, что бы использовать фасад `Debug`

```php
'Debugbar' => Barryvdh\Debugbar\Facades\Debugbar::class,
```