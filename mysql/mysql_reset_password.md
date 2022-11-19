
# Mysql. Сброс пароля root

```bash
sudo /etc/init.d/mysql stop

sudo mysqld --skip-grant-tables &

sudo mkdir -v /var/run/mysqld && sudo chown mysql /var/run/mysqld

mysql -u root mysql
```