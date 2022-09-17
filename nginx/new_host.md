
# Настройка виртуальных хостов
https://veesp.com/ru/blog/how-to-setup-lnmp-on-ubuntu/


Все настройки хостов содерж-ся в папке /etc/nginx/sites-available/
По умолч. уже есть один виртуальный хост с конфигом /etc/nginx/sites-available/default


```bash
# созд. и конфиг. файл для нового хоста
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/mysite.local

# созд. симлинк на конфиг нов. хоста
sudo ln -s /etc/nginx/sites-available/mysite.local /etc/nginx/sites-enabled/

# редак. конфиг. файл для нового хоста
sudo nano /etc/nginx/sites-available/mysite.local

# созд. корневой каталог сайта
mkdir /home/ch/develop/sites/mysite.local

```
Рекоменд. для каждого домена делать отдельно:
- директорию с исходниками сайта;
- директорию с логами;
- в некоторых ситуациях отдельный php-fpm пул для каждого сайта или группы сайтов.

Файл /etc/nginx/nginx.conf/sites-available/mysite.local:

server {
	listen 127.0.01:80;
    
    # доменное имя сайта
	server_name mysite.local www.mysite.local mysite.com;

	error_log /var/log/nginx/mysite.local.error.log;
	access_log /var/log/nginx/mysite.local.access.log;
	error_page 500 502 503 504 /50x.html;

	location / {
        # корневой каталог сайта
		root /home/ch/develop/sites/mysite.local;
		index  index.html index.htm index.php;
	}
}


```bash
sudo service nginx reload
# если ошибка "Reloading nginx configuration nginx [fail]"
sudo nano /var/log/nginx/error.log

# старт
sudo service nginx start

```

# Настроить права на папку /var/www/
```bash
# Для начала создай группу:
sudo groupadd groupname

# Затем добавь себя в эту группу:
sudo gpasswd -a username groupname

# После чего дай созданной группе права на запись в каталог:
sudo chown -R root:groupname /var/www
sudo chmod 775 /var/www

# username и groupname заменить на своё. Может понадобиться перелогиниться.

```

# Проверка работы

Если вы использовали несуществующий домен, то пишем в /etc/hosts

```bash
<ip_адрес_сервера> example.com

# проверка сайта
curl -Is http://127.0.0.1 | head -1
```