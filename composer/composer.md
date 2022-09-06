composer.json - файл в котором содержится описание основных пакетов, включая требования к их версиям
composer.lock» - это файл, содержащий реальные версии пакетов

Команды:

```bash
# создание базового composer.json
composer init 

# обновить зависимости по composer.json
composer update     

# установка пакетов, прописанных в composer.json
composer install    

 # пересборка автозагрузчика
composer dumpautoload  

# добавление нового пакета 
composer require package/package:version 

# обновления файла «composer.lock» без обновления самих пакетов
composer update --lock     

# пример изменения параметра конфигурации
composer config --global cache-files-maxsize «2048MiB»  

# добавление этого параметра к любой команде 
# включит показ времени выполнения и объёма использованной памяти
composer --profile      

# подробная инфомация о выполняемой операции
composer --verbose  

# список установленных пакетов с описанием каждого
composer show --installed   

# сведения о PHP
composer show --platform    

# обновить composer
composer self-update   

# удаление пакета
composer remove vendor/package    

# устн-ка пакета, если  файл «composer.phar» находится в текущем каталоге
php composer.phar require vendor/package   
```