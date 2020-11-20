CREATE TABLE Batch (
    id int NOT NULL AUTO_INCREMENT,
    productType int NOT NULL,
    AmountProduced int NOT NULL,
    OEE float NOT NULL,
    machineSpeed int NOT NULL,
    amountToProduce int NOT NULL,
    productionTime int NOT NULL,
    acceptableProductAmount int NOT NULL,
    defectProductAmount int NOT NULL
)