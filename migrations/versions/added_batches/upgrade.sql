CREATE TABLE batches(
    identifier INTEGER ,
    speed INTEGER ,
    amount_to_produce INTEGER ,
    started_dt TIMESTAMP ,
    recipe_id VARCHAR(128) ,
    finished_dt TIMESTAMP ,
    oee FLOAT ,
    PRIMARY KEY (identifier)
)
