
- Закомментировать "\Barryvdh\Debugbar\ServiceProvider::class" в config/app.php (в 2-х местах).

- В файле ".env":

APP_ENV=production
APP_DEBUG=false
APP_URL=<указать URL сайта>


```bash
# создать админа
php artisan orchid:admin nickname email@email.com secretpassword

composer install --optimize-autoloader --no-dev

npm run production 

php artisan config:clear

php artisan route:cache
php artisan config:cache 
php artisan view:cache
php artisan event:cache
```