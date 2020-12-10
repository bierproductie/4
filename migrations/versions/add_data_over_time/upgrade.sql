CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE data_over_time (
    batch_id INTEGER NOT NULL REFERENCES batches(identifier),
    measurement_ts TIMESTAMP WITH TIME ZONE PRIMARY KEY,
    inserted_ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    vibration FLOAT,
    produced INTEGER,
    state INTEGER,
    rejected INTEGER
) PARTITION BY RANGE (measurement_ts);
CREATE INDEX data_over_time_idx ON data_over_time (batch_id, measurement_ts);


-- Fail safe table if client tries to insert with a 'measurement_ts' that 
-- doesn't match a partition

CREATE TABLE data_over_time_default PARTITION OF data_over_time DEFAULT;

CREATE OR REPLACE FUNCTION create_partitions(
    from_year INTEGER,
    to_year INTEGER
)
RETURNS VOID AS $$
DECLARE
    f_date text;
    t_date text;
BEGIN
    FOR year IN from_year..to_year LOOP
        FOR month in 1..11 LOOP
            SELECT TO_DATE(format(E'%s-%s-01', year, month),'YYYY-MM-DD') INTO f_date;
            SELECT TO_DATE(format(E'%s-%s-01', year, month+1),'YYYY-MM-DD') INTO t_date;
            EXECUTE format(E'CREATE TABLE data_over_time%s%s PARTITION OF data_over_time FOR VALUES FROM (''%s'') TO (''%s'');', year, month, f_date, t_date);
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT create_partitions(2020, 2030);
