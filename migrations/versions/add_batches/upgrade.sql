CREATE TABLE batches (
    identifier SERIAL,
    speed INTEGER,
    amount_to_produce INTEGER,
    started_dt TIMESTAMP WITH TIME ZONE,
    recipe_id VARCHAR(128) REFERENCES recipes(name),
    finished_dt TIMESTAMP WITH TIME ZONE,
    oee FLOAT,
    PRIMARY KEY(identifier)
);
