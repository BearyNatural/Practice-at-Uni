-- shift+ctrl+e = execute
select * 
from sys.databases

SELECT *
FROM SYSOBJECTS
WHERE XTYPE = 'MOVIE'; --TABLE NAME, OR PK FOR PRIMARY KEY ETC;
GO

SELECT *
FROM INFORMATION_SCHEMA.TABLES; --VIEWS OR TABLES, ETC; SAME AS ABOVE CODE;

select name 
from sys.databases

-- create database kayhoweDB;
Drop table if exists PRODCATEGORY;
Drop table if exists PRODUCT;
Drop table if exists CUSTOMER2;
Drop table if exists ORDER2;
Drop table if exists ORDERLINE;

use kayhoweDB;

CREATE TABLE PRODCATEGORY(
    CATCODE NVARCHAR(5),
    [DESCRIPTION] NVARCHAR(200) NOT NULL,
    PRIMARY KEY(CATCODE)
);

CREATE TABLE PRODUCT(
    PRODID INT,
    [DESCRIPTION] NVARCHAR(MAX),
    COSTPRICE MONEY,
    RETAILPRICE MONEY,
    CATCODE NVARCHAR(5),
    PRIMARY KEY(PRODID),
    FOREIGN KEY(CATCODE) REFERENCES PRODCATEGORY,
    CHECK (COSTPRICE > 0),
    CHECK (RETAILPRICE > COSTPRICE)
);

CREATE TABLE CUSTOMER2(
    CUSTID NVARCHAR(10),
    FIRSTNAME NVARCHAR(200) NOT NULL,
    SURNAME NVARCHAR(200),
    EMAIL NVARCHAR(200) NOT NULL,
    PRIMARY KEY(CUSTID)
);

CREATE TABLE ORDER2(
    CUSTID NVARCHAR(10),
    DATETIMEPLACED DATETIME,
    DELIVERYADDRESS NVARCHAR(MAX) NOT NULL,
    PRIMARY KEY(CUSTID, DATETIMEPLACED),
    FOREIGN KEY(CUSTID) REFERENCES CUSTOMER2
);

CREATE TABLE ORDERLINE(
    CUSTID NVARCHAR(10),
    DATETIMEPLACED DATETIME,
    PRODID INT,
    QTY INT,
    PRIMARY KEY(CUSTID, DATETIMEPLACED, PRODID),
    FOREIGN KEY(PRODID) REFERENCES PRODUCT,
    FOREIGN KEY(CUSTID, DATETIMEPLACED) REFERENCES ORDER2,
    CHECK (QTY > 0),
);

DROP VIEW CUSTOMER_BRIEF;
DROP VIEW TOTAL_QTY_SOLD;

GO
CREATE VIEW CUSTOMER_BRIEF AS
SELECT CUSTOMER2.FIRSTNAME, CUSTOMER2.SURNAME
FROM CUSTOMER2
;
GO
CREATE VIEW TOTAL_QTY_SOLD AS
SELECT SUM(QTY) AS SUM
FROM ORDERLINE
;
GO

SELECT *
FROM CUSTOMER_BRIEF
;

SELECT *
FROM TOTAL_QTY_SOLD
;

-- DROP VIEW CUSTOMER_BRIEF;
-- DROP VIEW TOTAL_QTY_SOLD;

-- -- CREATING LOGINS & USERS:

DROP USER IF EXISTS ADMIN3018;
DROP LOGIN ADMIN3018;
DROP USER IF EXISTS API3018;
DROP LOGIN API3018;
DROP USER IF EXISTS DEV3018;
DROP LOGIN DEV3018;
DROP USER IF EXISTS BACKUP3018;
DROP LOGIN BACKUP3018;

GO
CREATE LOGIN ADMIN3018 WITH PASSWORD = 'PASSWORD3)18';
CREATE USER ADMIN3018 FOR LOGIN ADMIN3018;
EXEC SP_ADDROLEMEMBER 'DB_OWNER', 'ADMIN3018';
GO

CREATE LOGIN API3018 WITH PASSWORD = 'PASSWORD3)18';
CREATE USER API3018 FOR LOGIN API3018;
EXEC SP_ADDROLEMEMBER 'DB_DATAWRITER', 'API3018';
EXEC SP_ADDROLEMEMBER 'DB_DATAREADER', 'API3018';
GO

CREATE LOGIN DEV3018 WITH PASSWORD = 'PASSWORD3)18';
CREATE USER DEV3018 FOR LOGIN DEV3018;
EXEC SP_ADDROLEMEMBER 'DB_DDLADMIN', 'DEV3018';
EXEC SP_ADDROLEMEMBER 'DB_DATAWRITER', 'DEV3018';
EXEC SP_ADDROLEMEMBER 'DB_DATAREADER', 'DEV3018';
GO

CREATE LOGIN BACKUP3018 WITH PASSWORD = 'PASSWORD3)18';
CREATE USER BACKUP3018 FOR LOGIN BACKUP3018;
EXEC SP_ADDROLEMEMBER 'DB_BACKUPOPERATOR', BACKUP3018;
GO

DROP USER IF EXISTS ADMIN3018;
DROP LOGIN ADMIN3018;
DROP USER IF EXISTS API3018;
DROP LOGIN API3018;
DROP USER IF EXISTS DEV3018;
DROP LOGIN DEV3018;
DROP USER IF EXISTS BACKUP3018;
DROP LOGIN BACKUP3018;


















































