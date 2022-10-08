apt-get --purge remove mysql-server
apt-get --purge remove mysql-client
apt-get --purge remove mysql-common

apt purge mysql-server-8.0
apt purge mysql-server

apt-get autoremove
apt-get autoclean

rm -rf /etc/mysql
rm -rf /var/lib/mysql
