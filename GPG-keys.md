# Шифрование файлов с помощью GPG

## создание ключа
 gpg --full-gen-key 
1
4096
0
y
name, email, comment
пароль

```
echo "keyid-format 0xlong              ✔  3m 41s  
dquote> throw-keyids
dquote> no-emit-version
dquote> no-comments" > ~/.gnupg/gpg.conf
```

### проверка
gpg -k     # покажет публиный ключ
gpg -K     # покажет приватный ключ


### шифрование файла dfgg.xlsx
gpg -e -a -r a.s.chasovnikov@yandex.ru dfgg.xlsx


### расшифровка файла из dfgg.xlsx.asc в dfgg.xlsx
gpg -d -o dfgg.xlsx dfgg.xlsx.asc  

### эскпорт ключей в файл
gpg --export -a a.s.chasovnikov@yandex.ru > public.gpg
gpg --export-secret-key -a a.s.chasovnikov@yandex.ru > secret.gpg

### удаление ключей
gpg --delete-secret-keys a.s.chasovnikov@yandex.ru
gpg --delete-keys a.s.chasovnikov@yandex.ru

### мпорт ключей из файлов
 gpg --import public.gpg
  gpg --import secret.gpg

### проверка
gpg -k     # покажет публиный ключ
gpg -K     # покажет приватный ключ
