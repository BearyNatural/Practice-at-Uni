select name 
from sys.databases

use kayhoweDB;

Drop table if exists COMPLAINT;

use kayhoweDB;
create table CUSTOMER(
    CustNo int,
    FirstName nvarchar(100),
    Surname nvarchar(100),
    Address nvarchar(100), 
    Suburb nvarchar(100),
    Postcode decimal(4),
    Phone int,
    PRIMARY KEY(CustNo)
);

use kayhoweDB;
create table VEHICLE(
    Registration nvarchar(6),
    VinNumber nvarchar(17),
    Make nvarchar(50),
    Model nvarchar(50),
    YearOfManufacture decimal(4),
    CustNo int,
    Primary Key (Registration),
    Foreign Key(CustNo) References CUSTOMER
);

use kayhoweDB;
create table CERTIFICATE(
    CertificateNo int,
    IssueDate DATE,
    Registration NVARCHAR(6),
    Primary Key(CertificateNo),
    Foreign Key(Registration) References VEHICLE
);


