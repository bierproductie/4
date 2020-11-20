CREATE TABLE VibOverTime (
    batch_id int NOT NULL REFERENCES Batch(id),
    VibrationAndTime_id int NOT NULL REFERENCES VibrationAndTime(id)
)
