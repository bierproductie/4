CREATE TABLE batches (
    identifier SERIAL PRIMARY KEY,
    speed INTEGER,
    amount_to_produce INTEGER,
    started_dt TIMESTAMP WITH TIME ZONE,
    recipe_id FLOAT REFERENCES recipes(identifier),
    finished_dt TIMESTAMP WITH TIME ZONE,
    oee FLOAT
);
