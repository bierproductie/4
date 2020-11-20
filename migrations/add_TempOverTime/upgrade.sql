CREATE TABLE TempOverTime (
    batch_id int NOT NULL REFERENCES Batch(id),
    tempAndTime_id int NOT NULL REFERENCES tempAndTime(id)
)
