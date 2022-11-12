# quick start

```bash

# check
sudo service nginx status 
ps -ax | grep nginx
sudo service php8.1-fpm status 
sudo systemctl status apache2

sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/site1
sudo ln -s /etc/nginx/sites-available/site1 /etc/nginx/sites-enabled/
sudo mcedit /etc/nginx/sites-available/site1
# 1) delete 'default_server';
# 2) server_name site1;

sudo mcedit /etc/hosts
# 127.0.0.1 site1

sudo nginx -t
sudo service nginx stop
sudo service nginx start

# check: http://site1

mkdir /home/myuser/sites/site1
touch /home/myuser/sites/site1/index.html
git
sudo mcedit /etc/nginx/sites-available/site1
# root /home/myuser/sites/site1;

# check: http://site1
# if there are problems:
# check checking the rights to the folders
# or create site in /var/www/
sudo nginx -V
# check logs

```

# Настройка виртуальных хостов
https://veesp.com/ru/blog/how-to-setup-lnmp-on-ubuntu/


Все настройки хостов содержатся в папке `/etc/nginx/sites-available/`.
По умолчанию уже есть один виртуальный хост с конфигом `/etc/nginx/sites-available/default`.


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
Рекомендуется для каждого домена делать отдельно:
- директорию с исходниками сайта;
- директорию с логами;
- в некоторых ситуациях отдельный `php-fpm`-пул для каждого сайта или группы сайтов.

Пример файла `/etc/nginx/nginx.conf/sites-available/mysite.local`:

```nginx
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
```

Перезапускаем nginx
```bash
sudo service nginx reload
# если ошибка "Reloading nginx configuration nginx [fail]"
sudo nano /var/log/nginx/error.log

# старт
sudo service nginx start

```

### Настроить права на папку `/var/www/`
```bash
# Для начала создадим группу:
sudo groupadd groupname

# Затем добавим себя в эту группу:
sudo gpasswd -a username groupname

# После чего дадим созданной группе права на запись в каталог:
sudo chown -R root:groupname /var/www
sudo chmod 775 /var/www
# username и groupname заменим на своё. Может понадобиться перелогиниться.

```

### Проверка работы

Если используем несуществующий домен, то пишем в `/etc/hosts`

```bash
<ip_адрес_сервера> example.com

# проверка сайта
curl -Is http://127.0.0.1 | head -1
```