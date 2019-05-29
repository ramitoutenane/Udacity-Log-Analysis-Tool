#!/usr/bin/env python

import psycopg2

file = open('log.txt', 'w')
db = psycopg2.connect("dbname=news")
cur = db.cursor()

# 1. What are the most popular three articles of all time?
query = '''SELECT title , COUNT(*) AS views
FROM log,articles
WHERE path LIKE '%'||slug||'%'
AND status = '200 OK'
GROUP BY title
ORDER BY views DESC
LIMIT 3;'''
cur.execute(query)
result = cur.fetchall()

file.write('''
1. What are the most popular three articles of all time?\r\n
''')
for i in result:
    file.write("* '" + i[0] + "' -- " + str(i[1]) + " views.\r\n")

# 2. Who are the most popular article authors of all time?
query = '''SELECT name , COUNT(*) AS views
FROM log,articles,authors
WHERE path LIKE '%'||slug||'%'
AND status = '200 OK'
AND authors.id = articles.author
GROUP BY name
ORDER BY views DESC;'''
cur.execute(query)
result = cur.fetchall()

file.write('''
\r\n2. Who are the most popular article authors of all time?\r\n
''')
for i in result:
    file.write("* " + i[0] + " -- " + str(i[1]) + " views.\r\n")

# 3. On which days did more than 1% of requests lead to errors?
query = '''SELECT date , error_percentage
FROM error_stats
WHERE error_percentage>=1;'''
cur.execute(query)
result = cur.fetchall()

file.write('''
\r\n3. On which days did more than 1% of requests lead to errors?\r\n
''')
for i in result:
    file.write("* " + i[0] + " -- " + str(i[1]) + "% errors.\r\n")

db.close()
file.close()

with open("log.txt") as file:
    print file.read()
