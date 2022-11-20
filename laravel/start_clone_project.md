### Настройка клонированного проекта на Laravel

```bash


composer install    
    # если есть composer.lock (composer.lock не позволяет автоматически получать последние версии)

composer update     
    # если нужно обновиться до последних версий

cp .env.example .env
    # копир. и редактир.

php artisan key:generate    
    # записывает APP_KEY в файле .env

php artisan storage:link 
    # создать симлинк папки storage в папке public

sudo service mysql status
sudo service mysql start
sudo mysq
CREATE DATABASES mybd
    # создать БД

php artisan migrate --seed 
    # запуск миграций + создание тестовых данных

    
npm install         
    # уст-ка npm-завис-ти (см. package.jsoon)

npm audit fix --force  
    # если попросит

npm run dev
    # запуск команды из package.json: scripts: dev

php artisan serve

```