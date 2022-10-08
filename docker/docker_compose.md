
# после редактирования файла docker-compose.yml
docker-compose build   # сделать образ по файлу docker-compose.yml

# если нужно выполнить команды из docker-compose.yml
docker-compose run django django-admin startproject <NAME_PROJECT> .

docker-compose up      # запуск
docker-compose up -d   # запуск в фоне

docker-compose down    # останов

# выполнить команду, если контейнер уже запущен
docker exec -it <CONTAINER ID> bash
# или (если в кон-ре нет bash)
docker exec -it <CONTAINER ID> sh

