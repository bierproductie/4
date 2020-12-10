CREATE TABLE batches (
    identifier SERIAL PRIMARY KEY,
    speed INTEGER,
    amount_to_produce INTEGER,
    started_dt TIMESTAMP WITH TIME ZONE,
    recipe_id VARCHAR(128) REFERENCES recipes(name),
    finished_dt TIMESTAMP WITH TIME ZONE,
    oee FLOAT
);
