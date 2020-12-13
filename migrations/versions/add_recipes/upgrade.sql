CREATE TABLE recipes (
    machine_id FLOAT NOT NULL,
    max_speed INTEGER,
    recommended_speed INTEGER,
    name VARCHAR(128),
    PRIMARY KEY (name)
);

INSERT INTO recipes (machine_id, max_speed, recommended_speed, name)
VALUES (0.0, 600.0, 300.0, 'Pilsner'),
       (1.0, 300.0, 150.0, 'Wheat'),
       (2.0, 150.0, 75.0, 'IPA'),
       (3.0, 200.0, 100.0, 'Stout'),
       (4.0, 100.0, 50.0, 'Ale'),
       (5.0, 125.0, 75.0, 'Alcohol Free');
