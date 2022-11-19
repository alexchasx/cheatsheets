## Шпаргалка по Composer

```bash
# composer.json - описание пакетов, включая требования к их версиям
# composer.lock - содержит уже не требования, а реальные версии пакетов

composer help [command]
    # справка команд

composer list
    # показ. список команд

composer create-project vendor/package dir/
    # cоздать новый проект из указ. пакета в указ. каталоге

composer require vendor/package
    # загружает пакет
    # обновляет composer.json и composer.lock

composer install [--no-scripts]
    # если есть composer.lock - устан. версий из него,
    # иначе - из composer.json, и созд. composer.lock
    # --no-scripts - не запуск. скрипты, указанных в pre- и post- настройках

composer init 
    # создает базовый composer.json в текущем каталоге
    # далее при запуске команд Composer будет спрашивать параметры

composer update [--lock]
    # обнов. завис-ти по composer.json
    # обнов. composer.lock
    # --lock - обнов. composer.lock без обновления самих пакетов

composer validate
    # проверяет composer.json

composer status
    # проверить есть ли локальные изменения в любой из пакетов

composer dump-autoload [--optimize]
    # обновить автозагрузчик без установки/обнов-я пакетов
    # --optimize - преобр-е PSR-0 как для classmap (ускоряет автозагр-ку)

composer about
    # информация о Composer

composer archive vendor/package
    # архив-е проекта ил пакета

composer browse
    # открывает URL пакета

composer clear-cache
    # очищает внутренний кэш пакетов

composer remove vendor/package
    # удаляет пакет из секций require или require-dev

composer search <ключевые слова>
    # искать в репо. текущ. проекта (см. "repositories" в composer.json)

composer run-script
    # запустить скрипты, объявленные в composer.json

composer config --list
    # редак-е парам-в Composer в composer.json или в config.json

composer config --global cache-files-maxsize «2048MiB»  
    # пример изменения параметра конфигурации

composer depends vendor/package
    # сообщает какие пакеты зависят от указ-го пакета

composer global
    # для устан-ки командных утилит глобально

composer diagnose
    # диагностика проблем

composer licenses
    # показать инф. о лицензиях завис-ей

composer show [vendor/package [версия]] [--all]
    # cписок всех устан-ых или указ-ых пакетов
    # --all - всех доступных

composer suggest [vendor/package]
    # список всех пакетов, предложенных установленными

composer --profile      
    # добавление этого параметра к любой команде 
    # включит показ времени выполнения и объёма использованной памяти

composer --verbose  
    # инфомация о выполняемой операции

composer show --installed   
    # список установленных пакетов с описанием каждого

composer self-update   
    # обнов. composer.phar

php composer.phar require vendor/package   
    # устн-ка пакета, если  файл «composer.phar» находится в текущем каталоге
```