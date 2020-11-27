CREATE TABLE batches (
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    product_type int NOT NULL,
    Amount_produced int NOT NULL,
    oee float NOT NULL,
    machine_speed int NOT NULL,
    amount_to_produce int NOT NULL,
    production_time int NOT NULL,
    acceptable_product_amount int NOT NULL,
    defect_product_amount int NOT NULL
);
