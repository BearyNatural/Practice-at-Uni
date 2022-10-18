-- shift+ctrl+p = add new connection & use url, database, user & password from sheet
-- shift+ctrl+e = execute
select name 
from sys.databases

-- SELECT '104153018' as studentid, *

USE ATDB;

-- Q1:
SELECT '104153018' as studentid, *
FROM BOOKING
WHERE EVENTYEAR = '2021'
ORDER BY EVENTMONTH ASC, EVENTDAY ASC
;

-- Q2:
SELECT '104153018' as studentid, E.TOURNAME, C.GENDER, COUNT(B.DATEBOOKED) AS NUM_BOOKINGS
FROM BOOKING AS B
INNER JOIN CLIENT AS C ON B.CLIENTID = C.CLIENTID
INNER JOIN EVENT AS E ON B.TOURNAME = E.TOURNAME
GROUP BY C.GENDER, E.TOURNAME
ORDER BY E.TOURNAME DESC
;

-- Q3:
SELECT '104153018' as studentid, E.TOURNAME, C.GENDER, COUNT(B.DATEBOOKED) AS NUM_BOOKINGS
FROM BOOKING AS B
INNER JOIN CLIENT AS C ON B.CLIENTID = C.CLIENTID
INNER JOIN EVENT AS E ON B.TOURNAME = E.TOURNAME
GROUP BY C.GENDER, E.TOURNAME, B.EVENTMONTH
HAVING B.EVENTMONTH = 'FEB' 
AND COUNT(B.DATEBOOKED) < 2
ORDER BY E.TOURNAME
;
SELECT EVENTMONTH --CHECK
FROM EVENT;

-- Q4:
SELECT '104153018' as studentid, C.GIVENNAME, C.SURNAME, E.TOURNAME, B.DATEBOOKED, E.EVENTFEE, T.DESCRIPTION
FROM BOOKING AS B
INNER JOIN CLIENT AS C ON B.CLIENTID = C.CLIENTID
INNER JOIN EVENT AS E ON B.TOURNAME = E.TOURNAME
INNER JOIN TOUR AS T ON B.TOURNAME = T.TOURNAME
WHERE B.EVENTMONTH = 'JAN'
;

-- Q5:
SELECT '104153018' as studentid, C.GIVENNAME, C.SURNAME, COUNT(B.PAYMENT) AS NUM_BOOKINGS
FROM CLIENT AS C
LEFT JOIN BOOKING AS B ON C.CLIENTID = B.CLIENTID
GROUP BY C.GIVENNAME, C.SURNAME
;
SELECT GIVENNAME, SURNAME --CHECK
FROM CLIENT;

-- Q6:
SELECT '104153018' as studentid, C.GIVENNAME, C.SURNAME, COUNT(B.PAYMENT) AS NUM_BOOKINGS
FROM BOOKING AS B
RIGHT JOIN CLIENT AS C ON B.CLIENTID = C.CLIENTID
GROUP BY C.GIVENNAME, C.SURNAME
;

-- Q7:
SELECT '104153018' as studentid, C.CLIENTID, C.SURNAME, C.GIVENNAME, C.GENDER, B.CLIENTID, E.TOURNAME, E.EVENTMONTH, E.EVENTDAY, E.EVENTYEAR, B.PAYMENT, B.DATEBOOKED
FROM CLIENT AS C
FULL OUTER JOIN BOOKING AS B ON C.CLIENTID = B.CLIENTID
FULL OUTER JOIN EVENT AS E ON B.TOURNAME = E.TOURNAME
;

-- Q8.1:
SELECT '104153018' as studentid, C.CLIENTID, C.GENDER
FROM CLIENT AS C 
WHERE C.GENDER = 'F'
;

-- Q8.2:
SELECT '104153018' as studentid, B.CLIENTID, B.TOURNAME, B.EVENTMONTH, B.EVENTDAY, B.EVENTYEAR, B.PAYMENT, B.DATEBOOKED
FROM BOOKING AS B
INNER JOIN CLIENT AS C ON B.CLIENTID = C.CLIENTID
WHERE C.CLIENTID IN (SELECT C.CLIENTID FROM CLIENT WHERE C.GENDER = 'F')
;

-- Q9:
SELECT '104153018' as studentid, C.GIVENNAME, C.SURNAME, E.EVENTFEE-B.PAYMENT AS 'AMOUNT_OWING'
FROM CLIENT AS C 
INNER JOIN BOOKING AS B ON C.CLIENTID = B.CLIENTID
INNER JOIN EVENT AS E ON B.TOURNAME = B.TOURNAME
WHERE (E.EVENTFEE-B.PAYMENT) < 0
;

-- Q10:
SELECT '104153018' as studentid, DATEBOOKED,
DATENAME(WEEKDAY, DATEBOOKED) AS DAYOFWEEK,
DATENAME(DAY, DATEBOOKED) AS DAYOFMONTH,
DATENAME(MONTH, DATEBOOKED) AS MONTHNAME,
DATEPART(MONTH, DATEBOOKED) AS MONTHNUM,
DATEPART(YEAR, DATEBOOKED) AS YEAR
FROM BOOKING
;

