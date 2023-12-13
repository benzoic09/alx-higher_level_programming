-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as Avg_temp
FROM temperatures
GROUP BY city
ORDER BY Avg_temp DESC;
