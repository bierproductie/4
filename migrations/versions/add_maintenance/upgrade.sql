CREATE TABLE maintenance (
    value FLOAT DEFAULT 0,
    updated_ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION update_changetimestamp_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_ts = now(); 
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_maintenance_changetimestamp BEFORE UPDATE
    ON maintenance FOR EACH ROW EXECUTE PROCEDURE 
    update_changetimestamp_column();

INSERT INTO maintenance(value) VALUES(0);
