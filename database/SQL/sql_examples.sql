
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

-- ====================================================
-- Даны таблицы:

-- departments (id, name)
-- projects (id, name)
-- salaries (id, worker_id, salary, date)
-- tags (id, name)
-- tags_tasks (tag_id, task_id)
-- tasks (id, project_id, creator_id, worker_id, description, done, created_at, started_at, end_at)
-- workers (id, department_id, name)

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

-- GROUP, HAVING

-- Подсчитать суммы зарплат по всем сотрудникам
SELECT `worker_id`, SUM(`salary`) as `sum_salary` FROM `salaries` GROUP BY `worker_id`;

-- Вывести средние суммы зарплат сотрудников до марта от больших к меньшим
SELECT `worker_id`, AVG(`salary`) as `avg_salary`, MONTH(`date`) as `month`
FROM `salaries` 
GROUP BY `worker_id`, `salary`, `date`
HAVING `month` < 4 
ORDER BY `avg_salary` DESC;

-- Вывести средние суммы зарплат по месяцам
SELECT `worker_id`, AVG(`salary`) as `avg_salary`, MONTH(`date`) as `month`
FROM `salaries`
GROUP BY `worker_id`, `month`
ORDER BY `month`;

-- Вывести суммы всех зарплат по месяцам в которых суммы зарплат больше или равны 2000
SELECT `worker_id`, SUM(`salary`) as `sum_salary`, MONTH(`date`) as `month`
FROM `salaries`
GROUP BY `worker_id`, `month`, `salary`
HAVING `sum_salary` >= 1000
ORDER BY `month`;

-- Подсчитать количество тегов по каждой задаче и вывести в порядке убывания количества
SELECT `task_id`, COUNT(`tag_id`) as `count`
FROM `tags_tasks`
GROUP BY `task_id`
ORDER BY `count` DESC;


-- CROSS JOIN, INNER JOIN

-- Выбрать описание всех не выполненных задач с указанием отделов сотрудников, которые их выполняют
SELECT `description`, `department_id` FROM `tasks` 
JOIN `workers` ON `tasks`.`worker_id` = `workers`.`id`;

-- Выбрать все задачи, название тегов которых закачивается на буквосочетание "ть"
SELECT `tasks`.`description` as `task`, `tags`.`name` as `tag_name` FROM `tasks` 
JOIN `tags_tasks` ON `tags_tasks`.`task_id` = `tasks`.`id`
JOIN `tags` ON `tags_tasks`.`tag_id` = `tags`.`id`
WHERE `tags`.`name` LIKE '%ть';


-- LEFT JOIN, RIGHT JOIN

-- Выбрать описание всех не выполненных задач с указанием отделов сотрудников, которые их выполняют
SELECT `tasks`.`description`, `tasks`.`done`, `departments`.`name` FROM `tasks` 
LEFT JOIN `workers` ON `tasks`.`worker_id` = `workers`.`id`
JOIN `departments` ON `departments`.`id`=`workers`.`department_id`
WHERE `tasks`.`done`=0;

-- Выбрать все задачи, название тегов которых закачивается на буквосочетание "ть"
SELECT `tasks`.`description`, `tags`.`name` FROM `tasks` 
LEFT JOIN `tags_tasks` ON `tasks`.`id` = `tags_tasks`.`task_id`
JOIN `tags` ON `tags`.`id`=`tags_tasks`.`tag_id`
WHERE `tags`.`name` LIKE '%ть';


-- DELETE, TRUNCATE, UPDATE

-- 1) Перевести всех дизайнеров в отдел маркетинга
UPDATE `workers` 
SET `department_id` = 3
WHERE `department_id` = 2;

-- 2) Изменить название тега "саппорт" на "поддержка"
UPDATE `tags` 
SET `name` = 'поддержка'
WHERE `name` = 'саппорт';

-- 3) Установить все задачи выполненными по проекту КайзерДом
UPDATE `tasks` 
SET `done` = 1
WHERE `project_id` = 1;

-- 4) Увеличить все выплаты после февраля на 200 единиц
UPDATE `salaries`
SET `salary` = `salary` + 200
WHERE MONTH(`date`) > 2;

-- 5) Изменить название проектов со словом Юнитраст, указав им в имени "(архив)"
UPDATE `projects`
SET `name` = CONCAT(`name`, '(архив)')
WHERE `name` LIKE '%Юнитраст%';

-- 6) Удалить все задачи, которые были поставлены раньше февраля и были выполнены
DELETE FROM `tasks`
WHERE `tasks`.`done`=1
  AND MONTH(`created_at`) < 2;

-- 7) Удалить тег "кнопки"
DELETE FROM `tags`
WHERE `tags`.`name`='кнопки';

-- 8) Удалить все выплаты от марта, кроме сотрудника с id=11
DELETE FROM `salaries`
WHERE MONTH(`date`) >= 3
    AND `worker_id` <> 11;
