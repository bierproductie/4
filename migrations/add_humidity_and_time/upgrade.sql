CREATE TABLE HumidityAndTime (
    id int PRIMARY KEY NOT NULL,
    time int NOT NULL,
    humidity float NOT NULL
);
CREATE INDEX humidity_time_id ON HumidityAndTime(id);
