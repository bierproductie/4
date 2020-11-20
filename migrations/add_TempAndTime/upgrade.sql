CREATE TABLE TempAndTime (
    id int PRIMARY KEY NOT NULL,
    time int NOT NULL,
    temperature float NOT NULL
);
CREATE INDEX temp_time_id ON TempAndTime(id);
