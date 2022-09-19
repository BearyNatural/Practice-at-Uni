use querytask1;

SELECT '104153018' as studentid, MOVIENO, TITLE, RELYEAR, RUNTIME, RATINGCODE, COLOURCODE, TMDB_SCORE, TMDB_VOTES, TMDB_ID
FROM MOVIE;
-- LIMIT 3;


SELECT '104153018' as studentid, M.TITLE, M.RELYEAR
FROM MOVIE AS M;

SELECT '104153018' as studentid, MOVIENO, TITLE, TMDB_SCORE, RELYEAR
FROM MOVIE
ORDER BY TMDB_SCORE DESC;

SELECT '104153018' as studentid, MOVIENO, TITLE, RATINGCODE
FROM MOVIE
WHERE RATINGCODE = 'PG'
ORDER BY TITLE ASC;

SELECT '104153018' as studentid, MOVIENO, TITLE, RELYEAR
FROM MOVIE
WHERE RELYEAR < '1975'
ORDER BY RELYEAR, TITLE ASC;

SELECT '104153018' as studentid, MOVIENO, TITLE, RELYEAR
FROM MOVIE
WHERE TITLE = 'Hamlet'
ORDER BY RELYEAR ASC;

SELECT '104153018' as studentid, *
FROM MOVIE
WHERE TMDB_SCORE >= '7.8' AND RELYEAR >= '2010'
ORDER BY MOVIENO ASC;

SELECT '104153018' as studentid, MOVIENO, TITLE, RELYEAR, RUNTIME, RATINGCODE, COLOURCODE, TMDB_SCORE, TMDB_VOTES, TMDB_ID
FROM MOVIE
WHERE MOVIENO = '70' OR MOVIENO = '114' OR MOVIENO = '1858' OR MOVIENO = '286217'
ORDER BY MOVIENO ASC;