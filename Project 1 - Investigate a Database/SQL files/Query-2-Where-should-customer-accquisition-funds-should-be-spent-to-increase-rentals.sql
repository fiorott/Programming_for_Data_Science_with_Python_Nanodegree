/*
Udacity's - 'Programming for Data Science' certified Nanodegree Program
SQL > Lesson 8 > Project: Investigate the 'Sakila DVD rental database'

Q2: Where should the customer accquisition funds should be spent to increase
the rentals?
*/

WITH countries AS (
    SELECT r.rental_id,
           cu.customer_id,
           a.district,
           ci.city,
           co.country
      FROM rental r
      JOIN customer cu
        ON r.customer_id = cu.customer_id
      JOIN address a
        ON cu.address_id = a.address_id
      JOIN city ci
        ON a.city_id = ci.city_id
      JOIN country co
        ON ci.country_id = co.country_id
  ORDER BY 5, 4, 3, 2, 1)

  SELECT DISTINCT country,
         COUNT(country) OVER (PARTITION BY country) AS rentals
    FROM countries
ORDER BY 2 DESC;
