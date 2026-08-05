-- Write your query below
SELECT name
FROM customers
LEFT JOIN orders o ON o.customer_id = customers.id
WHERE o.id IS NULL
GROUP BY name