-- Write your query below
-- purchased a b not c
SELECT o.customer_id, c.customer_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY o.customer_id, c.customer_name
HAVING SUM(
CASE 
WHEN product_name = 'A'
THEN 1
ELSE 0
END)>=1
AND 
SUM(
CASE 
WHEN product_name = 'B'
THEN 1
ELSE 0
END)>=1
AND
SUM(
CASE 
WHEN product_name = 'C'
THEN 1
ELSE 0
END)=0
ORDER BY customer_name