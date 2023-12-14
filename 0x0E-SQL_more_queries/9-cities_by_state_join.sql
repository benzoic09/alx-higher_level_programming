-- script that lists all cities contained in the database hbtn_0d_usa
SELECT x.id, x.name, y.name
FROM cities AS x
INNER JOIN states AS y
ON y.state_id = x.id
ORDER BY x.id;
