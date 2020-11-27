CREATE TABLE VibrationAndTime (
    id int PRIMARY KEY NOT NULL,
    time int NOT NULL,
    Vibration float NOT NULL
);
CREATE INDEX vibration_time_id ON VibrationAndTime(id);
