
## Для Linux Mint / Ubuntu

```bash
sudo service apache2 status
sudo service apache2 start
sudo service apache2 stop
sudo service apache2 restart
sudo service apache2 reload

apachectl -k restart            # жесткую перезагрузку
apachectl -k graceful           # обновление конфигурации без перезагрузки сервиса

# Включить автозапуск при загрузке системы
sudo systemctl enable apache2   # [On Systemd]   Ubunt/Debia
# или
sudo chkconfig apache2 on       # [On SysVInit]  Ubunt/Debia

# убрать из автозагрузки
sudo systemctl disable apache2

# Проверка на ошибки синтаксиса конфигурации Apache
sudo apache2ctl -t
```
