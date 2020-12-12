CREATE TABLE inventory_status (
    identifier SERIAL PRIMARY KEY,
    name VARCHAR(128),
    max_value FLOAT,
    current_value FLOAT
);
