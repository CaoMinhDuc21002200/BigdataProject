-- Step 1: Create Table
CREATE TABLE my_table (
    column1 DATATYPE,
    column2 DATATYPE,
    ...
);

-- Step 2: Import CSV Data
LOAD DATA INFILE 'D:/Download/bigdataProject/data.csv'
INTO TABLE my_table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS; -- If your CSV file contains a header row
