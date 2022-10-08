
```bash
# запустить контейнеры в фоне
./vendor/bin/sail up -d

# остановить
./vendor/bin/sail down
./vendor/bin/sail stop

# перестроить
./vendor/bin/sail build --no-cache

alias sail='[ -f sail ] && bash sail || bash vendor/bin/sail'

# выполнение команд в контейнере
sail php --version
sail php script.php
sail composer require laravel/sanctum
sail artisan queue:work
sail node --version 
sail npm run prod
sail yarn
```