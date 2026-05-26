CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);