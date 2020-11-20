CREATE TABLE HumOverTime (
    batch_id int NOT NULL REFERENCES Batch(id),
    HumidityAndTime_id int NOT NULL REFERENCES HumidityAndTime(id)
)
