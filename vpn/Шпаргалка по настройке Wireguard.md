 
# Шпаргалка по настройке Wireguard

## Покупка виртуального сервера

...

## Настройка сервера:

```bash
# вход на сервер
ssh root@<server-ip>
exit

# копируем ключи для входа на сервер без пароля 
ssh-copy-id root@<server-ip>

# закрыть доступ по паролю на сервер (если надо)
nano /etc/ssh/sshd_config
# PasswordAuthentification no
service ssh restart

apt update && apt upgrade -y
apt install -y wireguard

```

### Настройка сервера Wireguard:

- Создаем SSH-ключи для сервера:
 
```bash
cd /etc/wireguard
wg genkey | tee /etc/wireguard/server_privatekey | wg pubkey | tee /etc/wireguard/server_pubkey
# имена файлов любые

wg genkey | tee /etc/wireguard/server_privatekey | wg pubkey | tee /etc/wireguard/server_pubkey

# смотрим ключи. Далее будем их копировать в файл настроек
cat server_privatekey
cat client1_pubkey

# создаем файл настроек Wireguard
nano wg0.conf
```
Вставляем в файл текст (вместо <server_privatekey> и <client1_pubkey> вставляем соответствующие ключи):

```conf
[Interface]
PrivateKey = <server_privatekey>
Address = 10.0.0.1/24
ListenPort = 51830
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <client1_pubkey>
AllowedIPs = 10.0.0.2/32

[Peer]
PublicKey = <client2_pubkey>
AllowedIPs = 10.0.0.3/32
```
На каждый Peer должен быть свой уникальный AllowedIPs, который потом пропишем в файле настроек на компьютере клиента

```bash
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p

# включаем автозапуск wiregurad
systemctl enable wg-quick@wg0.service
# включаем wiregurad
systemctl start wg-quick@wg0.service
# проверяем состояние
systemctl status wg-quick@wg0.service
# перезапускаем при любом изменении настроек
systemctl restart wg-quick@wg0.service
```

## На компьютере клиента
- Устанавливаем Wireguard 

```bash
sudo su
cd /etc/wireguard
nano wg0.conf
```
- Создаем файл wg0.conf по примеру и подставляем соответственно ключи <client1_privatekey> и <server_pubkey>, <server-ip>.
Address берем из своего Peer на сервере
```conf
[Interface]
PrivateKey = <client1_privatekey>
Address = 10.0.0.2/32
DNS = 8.8.8.8

[Peer]
PublicKey = <server_pubkey>
Endpoint = <server-ip>:51830
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 20
```
- Из программы Wireguard нажимаем "Импорт тунелей из файла"

или на Ubuntu

```bash
systemctl start wg-quick@wg0
```

-------

wg-quick up wg0-client

