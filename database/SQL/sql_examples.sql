
SELECT
films.name_ru AS 'Название на русском',
films.name_en AS 'Название на английском',
films.year AS 'Год',
films.genre AS 'Жанр',
films.country AS 'Страна',
(SELECT GROUP_CONCAT(actors.name SEPARATOR ', ') FROM actors, actors_films WHERE
actors.id_actor=actors_films.id_actor and
actors_films.id_film=films.id_film) AS 'Актёры'
FROM films
LEFT JOIN genre ON films.id_genre=genre.id_genre
LEFT JOIN country ON films.id_country=country.id_country


-- Получить задачи за февраль
SELECT *, MONTH(`tasks`.`created_at`) as `month` FROM `tasks` HAVING `month`=2;

-- Выбрать завершенные задачи за январь.		
SELECT *, MONTH(`tasks`.`created_at`) as `month` FROM `tasks` HAVING `month`=1 AND `done`=1;

-- Вывести все начатые, но не завершенные задачи в порядке возрастания по дате начала работы
SELECT * FROM `tasks` WHERE `done`=0 AND `started_at` IS NOT NULL ORDER BY `started_at`;

-- Выбрать все задачи, которые содержат слово 'Бюджет"
SELECT * FROM `tasks` WHERE `description` LIKE '%Бюджет%';

-- Выбрать 3 самые свежие задачи
SELECT * FROM `tasks` ORDER BY `created_at` DESC LIMIT 3;

-- Выбрать 2 самые старые задачи, которые не были начаты
SELECT * FROM `tasks` WHERE `started_at` IS NULL ORDER BY `created_at` ASC LIMIT 2;

-- Выбрать все задачи для сотрудников с id = 8,9,11
SELECT * FROM `tasks` WHERE `worker_id` IN (8, 9, 11);

-- Выбрать все задачи которые: были завершены либо были не начаты
SELECT * FROM `tasks` WHERE `done`=1 OR `started_at` IS NULL;

-- Выбрать все задачи, которые были поставлены пользователем "на самого себя"
SELECT * FROM `tasks` WHERE `worker_id`=`creator_id`;

-- Выбрать все задачи, которые содержат слово "Изменить", либо поставлены пользователем с id=12 и не были завершены
SELECT * FROM `tasks` WHERE `description` LIKE '%Изменить%' OR `creator_id`=12 AND `done`=0;