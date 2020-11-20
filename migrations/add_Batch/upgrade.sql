CREATE TABLE Batch (
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    productType int NOT NULL,
    AmountProduced int NOT NULL,
    OEE float NOT NULL,
    machineSpeed int NOT NULL,
    amountToProduce int NOT NULL,
    productionTime int NOT NULL,
    acceptableProductAmount int NOT NULL,
    defectProductAmount int NOT NULL
);
CREATE INDEX batch_id ON Batch(id);
