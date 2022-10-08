
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

