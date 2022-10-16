
# nginx + mysql + php-fpm

https://gist.github.com/positron48/f429fcd84027a16d7029a12774d0c255

### MySQL

```bash
sudo apt install mysql-server
sudo /etc/init.d/mysql start
sudo mysql_secure_installation

# команды для работы
sudo /etc/init.d/mysql start|stop|restart|reload|force-reload|status

sudo mysql -u root -p

# создаем нового пользователя
CREATE USER 'wwwuser'@'localhost' IDENTIFIED BY 'Password+12';
GRANT ALL PRIVILEGES ON *.* TO 'wwwuser'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### Nginx

```bash
sudo apt update
sudo apt install nginx
sudo /etc/init.d/nginx start
# 
nginx -s stop|reload|quit|reopen

# проверить запущенные процессы nginx
ps -ax | grep nginx
```
Проверить по http://127.0.0.1/


### PHP-fpm

```bash
sudo apt install php-fpm php-mysql
sudo /etc/init.d/php8.1-fpm start
```

### Настройка хоста

```bash
cd /etc/nginx/sites-available/
sudo cp default blog.local

# редактируем файл blog.local
sudo nano blog.local

sudo ln -s /etc/nginx/sites-available/blog.local /etc/nginx/sites-enabled/

# Тестируем конфиг (должно быть ok) и обновляем nginx:
sudo nginx -t
sudo /etc/init.d/nginx reload

# C:\Windows\System32\drivers\etc\hosts
# Добавляем строку
127.0.0.1		blog.local
```

### phpmyadmin

```bash
sudo apt install php-mbstring php-gettext
sudo apt install phpmyadmin
sudo /etc/init.d/php8.1-fpm restart
```

Создаем еще один конфиг для хоста phpmyadmin:

```bash
cd /etc/nginx/sites-available/
sudo cp default phpmyadmin
sudo nano phpmyadmin

# -------------------- Файл phpmyadmin
server {
    listen 81 default_server;
    listen [::]:81 default_server;

    root /var/www/html/;

    index index.php index.html index.htm index.nginx-debian.html;
    server_name phpmyadmin;

    location /pma {
        alias /usr/share/phpmyadmin/;
        location ~ \.php$ {
            fastcgi_buffering off;
            fastcgi_pass unix:/run/php/php8.1-fpm.sock;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $request_filename;
            include fastcgi_params;
            fastcgi_ignore_client_abort off;
        }
        location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
            access_log    off;
            log_not_found    off;
            expires 1M;
        }
    }
}
# ----------------- Конец файла

sudo ln -s /etc/nginx/sites-available/phpmyadmin /etc/nginx/sites-enabled/
sudo nginx -t
sudo /etc/init.d/nginx reload

```

### Автозагрузка сервисов
```bash
sudo update-rc.d nginx defaults
sudo update-rc.d php8.1-fpm defaults
sudo update-rc.d mysql defaults
```

### Если неполадки:

```
/var/log/nginx/access.log  - лог запросов к nginx
/var/log/nginx/error.log   - лог ошибок nginx
/var/log/php8.1-fpm.log    - лог php-fpm
```

Если проблемы с правами:
```bash
# проверяем права к папке с сайтом
sudo -u www-data stat /path/to/site/
# если ошибка, то далее
# добавим пользователя в группу, которая указа в настройках nginx
sudo gpasswd -a www-data myuser
sudo nginx -s reload 
```

