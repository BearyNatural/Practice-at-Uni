select name 
from sys.databases

use kayhoweDB;

SELECT table_name
FROM INFORMATION_SCHEMA.TABLES;

-- build2
-- Drop table if exists COMPLAINT;

-- use kayhoweDB;
-- create table CUSTOMER(
--     CustNo int,
--     FirstName nvarchar(100),
--     Surname nvarchar(100),
--     Address nvarchar(100), 
--     Suburb nvarchar(100),
--     Postcode decimal(4),
--     Phone int,
--     PRIMARY KEY(CustNo)
-- );

-- use kayhoweDB;
-- create table VEHICLE(
--     Registration nvarchar(6),
--     VinNumber nvarchar(17),
--     Make nvarchar(50),
--     Model nvarchar(50),
--     YearOfManufacture decimal(4),
--     CustNo int,
--     Primary Key (Registration),
--     Foreign Key(CustNo) References CUSTOMER
-- );

-- use kayhoweDB;
-- create table CERTIFICATE(
--     CertificateNo int,
--     IssueDate DATE,
--     Registration NVARCHAR(6),
--     Primary Key(CertificateNo),
--     Foreign Key(Registration) References VEHICLE
-- );

-- build3
use kayhoweDB;

CREATE TABLE COMPETITOR(
    COMPETITORID NVARCHAR(10),
    FIRSTNAME NVARCHAR(100),
    SURNAME NVARCHAR(100),
    GENDER NVARCHAR(1),
    DATEOFBIRTH DATE,
    PRIMARY KEY(COMPETITORID)
);

CREATE TABLE LOCATION(
    LOCATION NVARCHAR(50),
    PRIMARY KEY(LOCATION)
);

CREATE TABLE MEET(
    LOCATION NVARCHAR(50),
    YEAR decimal(4),
    PRIMARY KEY(LOCATION, YEAR),
    FOREIGN KEY(LOCATION) REFERENCES LOCATION
);

CREATE TABLE EVENT(
    LOCATION NVARCHAR(50),
    YEAR decimal(4),
    GENDER NVARCHAR(1),
    AGERESTRICTION NVARCHAR(10),
    DISTANCE INT,
    PRIMARY KEY(LOCATION, YEAR, GENDER, AGERESTRICTION, DISTANCE),
    FOREIGN KEY(LOCATION, YEAR) REFERENCES MEET
);

CREATE TABLE ENTRY(
    COMPETITORID INT,
    LOCATION NVARCHAR(50),
    YEAR decimal(4),
    GENDER NVARCHAR(1),
    AGERESTRICTION NVARCHAR(10),
    DISTANCE INT,
    TIME decimal(6,2),
    PRIMARY KEY(COMPETITORID, LOCATION, YEAR, GENDER, AGERESTRICTION, DISTANCE),
    FOREIGN KEY(COMPETITORID) REFERENCES COMPETITOR,
    FOREIGN KEY(LOCATION, YEAR, GENDER, AGERESTRICTION, DISTANCE) REFERENCES EVENT
);
