-- shift+ctrl+e = execute
select * 
from sys.databases

SELECT *
FROM SYSOBJECTS
WHERE XTYPE = 'MOVIE'; --TABLE NAME, OR PK FOR PRIMARY KEY ETC;
GO

SELECT *
FROM INFORMATION_SCHEMA.VIEWS; --OR TABLES, ETC; SAME AS ABOVE CODE;

select name 
from sys.databases

create database kayhoweDB;

use kayhoweDB;
create table COMPLAINT(
    FullName NVARCHAR(100),
    Mobile INT, --NOT NULL IF NO NULL'S ACCEPTED
    StaffName NVARCHAR(100),
    ComplaintDetails NVARCHAR(500),
    ResolutionDetails NVARCHAR(500),
    PRIMARY KEY (FullName)
);

--get list of tables in database
use kayhoweDB
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';

DELETE FROM COMPLAINT;

-- Best Practice
use kayhoweDB;
INSERT INTO COMPLAINT(FullName, Mobile, StaffName, ComplaintDetails,ResolutionDetails) VALUES
('BILL SMITH', 438363012, 'FRED FLINSTONE', 'I AM NOT HAPPY ABOUT SOMETHING', 'WE DID NOTHING'),
('JANE JONES', 404250670, 'BARNEY RUBBLE', 'I AM NOT HAPPY ABOUT SOMETHING DIFFERENT', 'WE GAVE A REFUND'),
('JANET JACKSON', NULL, 'FRED FLINSTONE', 'I AM ANGRY ABOUT SOMETHING', 'CLIENT TERMINATED CALL BEFORE RESOLUTION REACHED');

use kayhoweDB;
INSERT INTO COMPLAINT(FullName, StaffName) VALUES
('JESSICA SIMPSON', 'FRED FLINSTONE'),
('MICHAEL HUTCHINSON', 'BARNEY RUBBLE'),
('KRISTEN DUNNST', 'FRED FLINSTONE');


-- Not best practice
use kayhoweDB;
INSERT INTO COMPLAINT VALUES
('BILL SMITH', 438363012, 'FRED FLINSTONE', 'I AM NOT HAPPY ABOUT SOMETHING', 'WE DID NOTHING'),
('JANE JONES', 404250670, 'BARNEY RUBBLE', 'I AM NOT HAPPY ABOUT SOMETHING DIFFERENT', 'WE GAVE A REFUND'),
('JANET JACKSON', NULL, 'FRED FLINSTONE', 'I AM ANGRY ABOUT SOMETHING', 'CLIENT TERMINATED CALL BEFORE RESOLUTION REACHED');


-- insert a few rows


-- select data

select * from complaint;

select *;

-- mandatory keywords - select from

-- select <columns>
-- from <table> as <alias>
-- where <rows/BOLEAN CONDITION>;


-- PLAY

select c.FullName, c.StaffName
from complaint as c
where staffname = 'FRED FLINSTONE';

select *
from complaint
where staffname != 'FRED FLINSTONE';

-- BODMAS

/*
BRACKETS
ORDERS
DIVISION
MULTIPLICATION
ADDITION
SUBTRACTION
*/

 /*
operators , + > 
BRACKETS
AND
OR
 */

use querytask1;

SELECT '104153018' as studentid, M.TITLE, M.RELYEAR
FROM MOVIE AS M;

select '104153018' as studentid

-- To see a list of the tables in a particular database run the following query

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE='BASE TABLE';

-- show tables is mysql
