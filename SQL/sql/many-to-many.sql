CREATE TABLE products 
(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders 
(
    id INT PRIMARY KEY,
    order_date DATE NOT NULL
);

-- This is the junction table that creates the many-to-many link
CREATE TABLE order_items 
(
    order_id INT,
    product_id INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);