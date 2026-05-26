SELECT
    order_date,
    SUM(o.quantity * p.price) AS daily_revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY order_date
ORDER BY order_date;

SELECT
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;

SELECT
    c.name,
    SUM(o.quantity * p.price) AS total_spent
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 10;

SELECT
    p.category,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;