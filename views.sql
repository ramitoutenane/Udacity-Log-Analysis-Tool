CREATE VIEW fail AS 
SELECT TO_CHAR(time,'FMmonth dd, yyyy')AS date, COUNT(*) AS num
FROM log
WHERE status ='404 NOT FOUND'
GROUP BY date
ORDER BY date;

CREATE VIEW success AS 
SELECT TO_CHAR(time,'FMmonth dd, yyyy')AS date, COUNT(*) AS num
FROM log
WHERE status ='200 OK'
GROUP BY date
ORDER BY date;

CREATE VIEW error_stats AS
SELECT fail.date as date,TRUNC(fail.num/(success.num + fail.num*1.0)*100,2) AS error_percentage 
FROM success, fail
WHERE success.date = fail.date;