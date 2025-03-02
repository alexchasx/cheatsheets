# Шифрование файлов с помощью GPG

```bash
# создание ключа

 gpg --full-gen-key 
1
4096
0
y
name, email, comment
пароль

echo "keyid-format 0xlong              ✔  3m 41s  
dquote> throw-keyids
dquote> no-emit-version
dquote> no-comments" > ~/.gnupg/gpg.conf

# проверка

gpg -k     # покажет публиный ключ
gpg -K     # покажет приватный ключ

# шифрование файла dfgg.xlsx

gpg -e -a -r email@yandex.ru dfgg.xlsx

# расшифровка файла из dfgg.xlsx.asc в dfgg.xlsx

gpg -d -o dfgg.xlsx dfgg.xlsx.asc

# эскпорт ключей в файл

gpg --export -a email@yandex.ru > public.gpg
gpg --export-secret-key -a email@yandex.ru > secret.gpg

# удаление ключей

gpg --delete-secret-keys email@yandex.ru
gpg --delete-keys email@yandex.ru

# импорт ключей из файлов

gpg --import public.gpg
gpg --import secret.gpg

# проверка

gpg -k     # покажет публиный ключ
gpg -K     # покажет приватный ключ

# Перенос на Windows

# Скопировать файлы public.gpg, secret.gpg на c:\_documents\3\
# Запустить Ubunutu под WSL
# Перейти из под Ubuntu на c:\_documents\3\

cd /mnt/c/_documents/3/

gpg --import public.gpg
gpg --import secret.gpg

# расшифровка
gpg -d -o dfgg.xlsx dfgg.xlsx.asc

# шифрование
gpg -e -a -r a.s.chasovnikov@yandex.ru dfgg.xlsx
```