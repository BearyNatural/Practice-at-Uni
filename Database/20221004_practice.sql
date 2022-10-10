-- shift+ctrl+p = add new connection & use url, database, user & password from sheet
-- shift+ctrl+e = execute
select name 
from sys.databases

-- Show all tables IN DATABASE:
SELECT *
FROM information_schema.tables;

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE='BASE TABLE';

-- create database kayhoweDB;

-- USE kayhoweDB;

USE ATDB;

SELECT '104153018' as studentid, *
FROM MOVIE
WHERE RELYEAR = 2003
ORDER BY RATINGCODE, TMDB_SCORE ASC
;

SELECT '104153018' as studentid, M.TITLE AS MOVIE_NAME, A.GENDER, COUNT(A.GENDER) AS NUM_ROLES
FROM MOVIE AS M
INNER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
INNER JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY M.TITLE, M.RELYEAR, A.GENDER
HAVING M.RELYEAR = 2001
ORDER BY M.TITLE DESC, A.GENDER
;

SELECT '104153018' as studentid, M.TITLE AS MOVIE_NAME, A.GENDER, COUNT(A.GENDER) AS NUM_ROLES
FROM MOVIE AS M
INNER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
INNER JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY M.TITLE, M.RELYEAR, A.GENDER
HAVING M.RELYEAR = 2001
AND COUNT(A.GENDER) <= 2
ORDER BY M.TITLE, A.GENDER DESC
;
SELECT '104153018' as studentid, M.TITLE AS MOVIE_NAME, A.GENDER, COUNT(A.GENDER) AS NUM_ROLES
FROM MOVIE AS M
INNER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
INNER JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY M.TITLE, M.RELYEAR, A.GENDER
HAVING M.RELYEAR = 2001
EXCEPT
SELECT '104153018' as studentid, M.TITLE AS MOVIE_NAME, A.GENDER, COUNT(A.GENDER) AS NUM_ROLES
FROM MOVIE AS M
INNER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
INNER JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY M.TITLE, M.RELYEAR, A.GENDER
HAVING M.RELYEAR = 2001
AND COUNT(A.GENDER) > 2
ORDER BY M.TITLE, A.GENDER DESC
;

SELECT M.TITLE, A.FULLNAME, C.COLOURNAME, R.SHORTDESC
FROM CASTING AS CA
INNER JOIN MOVIE AS M ON CA.MOVIENO = M.MOVIENO
INNER JOIN ACTOR AS A ON CA.ACTORNO = A.ACTORNO
INNER JOIN RATING AS R ON M.RATINGCODE = R.RATINGCODE
INNER JOIN COLOURTYPE AS C ON M.COLOURCODE = C.COLOURCODE
-- WHERE CA.CASTID IS NOT NULL
-- EXCEPT
-- INTERSECT
-- SELECT CA.CASTID
-- FROM CASTING AS CA
;

SELECT A.FULLNAME, COUNT(C.CASTID)
FROM ACTOR AS A 
LEFT JOIN CASTING AS C ON A.ACTORNO = C.ACTORNO
GROUP BY A.FULLNAME
-- HAVING COUNT(C.CASTID) = 0
;

SELECT A.FULLNAME, COUNT(C.CASTID)
FROM CASTING AS C
RIGHT JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY A.FULLNAME
-- HAVING COUNT(C.CASTID) = 0
;

-- SELECT '104153018' as studentid, A.FULLNAME, M.TITLE
-- FROM ACTOR AS A
-- FULL OUTER JOIN CASTING AS C ON A.ACTORNO = C.ACTORNO
-- FULL OUTER JOIN MOVIE AS M ON C.MOVIENO = M.MOVIENO
-- UNION ALL
-- SELECT '104153018' as studentid, A.FULLNAME, M.TITLE
-- FROM MOVIE AS M
-- FULL OUTER JOIN ACTOR AS A ON ACTORNO = A.ACTORNO
-- FULL OUTER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
-- -- WHERE 
-- ;

SELECT '104153018' as studentid, A.FULLNAME, M.TITLE
FROM ACTOR AS A
FULL OUTER JOIN CASTING AS C ON A.ACTORNO = C.ACTORNO
FULL OUTER JOIN MOVIE AS M ON C.MOVIENO = M.MOVIENO
WHERE M.TITLE IS NOT NULL AND A.FULLNAME IS NOT NULL
UNION ALL
SELECT '104153018' as studentid, A.FULLNAME, 'NULL' AS TITLE
FROM ACTOR AS A
FULL OUTER JOIN CASTING AS C ON A.ACTORNO = C.ACTORNO
FULL OUTER JOIN MOVIE AS M ON C.MOVIENO = M.MOVIENO
WHERE M.TITLE IS NULL
UNION ALL
SELECT '104153018' as studentid, 'NULL' AS FULLNAME, M.TITLE
FROM MOVIE AS M
FULL OUTER JOIN ACTOR AS A ON ACTORNO = A.ACTORNO
FULL OUTER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
WHERE A.FULLNAME IS NULL
;

SELECT DISTINCT '104153018' as studentid, A.ACTORNO--, COUNT(C.MOVIENO)
FROM ACTOR AS A 
INNER JOIN CASTING AS C ON A.ACTORNO = C.ACTORNO
INNER JOIN MOVIE AS M ON C.MOVIENO = M.MOVIENO
GROUP BY A.ACTORNO, A.GENDER
HAVING A.GENDER = 'M'
AND COUNT(C.MOVIENO) = 1
;

SELECT DISTINCT '104153018' as studentid, M.MOVIENO, M.TITLE, M.RELYEAR, M.RUNTIME, M.RATINGCODE, M.COLOURCODE, M.TMDB_SCORE, M.TMDB_VOTES, M.TMDB_ID
FROM MOVIE AS M
INNER JOIN CASTING AS C ON M.MOVIENO = C.MOVIENO
INNER JOIN ACTOR AS A ON C.ACTORNO = A.ACTORNO
GROUP BY M.MOVIENO, M.TITLE, M.RELYEAR, M.RUNTIME, M.RATINGCODE, M.COLOURCODE, M.TMDB_SCORE, M.TMDB_VOTES, M.TMDB_ID, A.ACTORNO, A.GENDER
HAVING A.ACTORNO IN (SELECT A.ACTORNO FROM ACTOR WHERE A.GENDER = 'M')
AND COUNT(C.MOVIENO) = 1
;

SELECT '104153018' as studentid, TITLE AS 'MOVIE_TITLE', TMDB_SCORE*TMDB_VOTES AS 'CALCULATED_COLUMN'
FROM MOVIE
WHERE RATINGCODE = 'PG' AND RUNTIME > 120
;

SELECT BIRTHDATE AS DATEBOOKED,
DATENAME(WEEKDAY, BIRTHDATE) AS DAYOFWEEK,
DATENAME(DAY, BIRTHDATE) AS DAYOFMONTH,
DATENAME(MONTH, BIRTHDATE) AS MONTHNAME,
DATEPART(MONTH, BIRTHDATE) AS MONTHNUM,
DATEPART(YEAR, BIRTHDATE) AS YEAR
FROM ACTOR
;


-- Provide a brief definition and an example (from the database used in this assessment) of the following terms:
-- Table = The tables are the database objects that behave as containers for the data, in which the data will be logically organized in rows and columns format.
-- Column = columns are known as fields
-- Row = rows are known as records

-- Briefly explain the difference between a Database and a DBMS.
-- Database: A database is a collection of information that is organized so that it can be easily accessed, managed and updated.
-- DBMS stands for Database Management System
-- A database management system (DBMS) is system software for creating and managing databases. The DBMS provides users and programmers with a systematic way to create, retrieve, update and manage data.

-- Provide a brief definition, and an example (from the database used in this assessment) of the following terms:
-- Primary Key (PK): The PRIMARY KEY constraint uniquely identifies each record in a table. Primary keys must contain UNIQUE values, and cannot contain NULL values. A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns (fields).
-- Foreign Key (FK): A foreign key (FK) is a column or combination of columns that is used to establish and enforce a link between the data in two tables to control the data that can be stored in the foreign key table.
-- Constraint: SQL constraints are used to specify rules for the data in a table. Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

-- Provide a brief definition of the following terms, including the Command Keywords used in each (e.g. SELECT is part of DML)
-- Data Definition Language (DDL) is a syntax for creating and modifying database objects such as tables, indices, and users. DDL statements are similar to a computer programming language for defining data structures, especially database schemas.  Here you have the CREATE, ALTER, and DROP statements, plus a couple of others. 
-- Data Manipulation Language (DML) The Data Manipulation Language (DML) is the domain of INSERT, UPDATE, and DELETE, which you use to manipulate data.
