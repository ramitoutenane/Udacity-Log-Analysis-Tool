# Project #3 : Logs Analysis Project.
This project is intended to be delivered as part of [Udacity's Full Stack Developer Nanodegree Program](https://mena.udacity.com/course/full-stack-web-developer-nanodegree--nd004) graduation requirements.

**By : "Mohamed Rami" Toutenane**

## Project Overview
Building an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like by answering 3 questions:

**1. What are the most popular three articles of all time?**
**2. Who are the most popular article authors of all time?**
**3. On which days did more than 1% of requests lead to errors?**

## Requirements
* Python  version 2.7.9 or higher.
* Vagrant
* VirtualBox
* [Udacity FSND Virtual Machine Configruration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* [Udacity newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## SQL Views 
### failed requests view

    CREATE VIEW fail AS 
    SELECT TO_CHAR(time,'FMmonth dd, yyyy')AS date, COUNT(*) AS num
    FROM log
    WHERE status ='404 NOT FOUND'
    GROUP BY date
    ORDER BY date;
### succeeded requests view

    CREATE VIEW success AS 
    SELECT TO_CHAR(time,'FMmonth dd, yyyy')AS date, COUNT(*) AS num
    FROM log
    WHERE status ='200 OK'
    GROUP BY date
    ORDER BY date;

### failed requests daily percentage view

    CREATE VIEW error_stats AS
    SELECT fail.date as date,TRUNC(fail.num/(success.num + fail.num*1.0)*100,2) AS error_percentage 
    FROM success, fail
    WHERE success.date = fail.date;

## Running the code 
 1. Bring the virtual machine online using **(vagrant up)** command. 
 2. Log into virtual machine using **(vagrant ssh)** command. 
 3. Copy **newsdata.sql** file into vagrant directory
 4. Load the data by using the command **psql -d news -f newsdata.sql**.
 5. Insert the **SQL Views** into news database.
 6. Copy python source code **LAT.py** into vagrant directory.
 7. Execute python code by using **(python LAT.py)** command.

**new text file named log.txt will be created in vagrant directory, it will contain the result of code execution**

## References
- [Udacity : Full Stack](https://classroom.udacity.com/nanodegrees/nd004-mena/parts/5d463571-1999-4e1d-adbb-dec1b3aa97e7)
- [Python 2.7.15 documentation](https://docs.python.org/2/index.html)
- [Postgresql Tutorial ](http://www.postgresqltutorial.com/)
- [Shebang line](https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3)
- [Udacity : Writing READMEs](https://classroom.udacity.com/courses/ud777)	
- [Stackdit MD Editor and Convertor](https://stackedit.io/app#)
- [Pyhton 2.7.9](https://www.python.org/downloads/release/python-279/)
- [JetBrains PyCharm ](https://www.jetbrains.com/pycharm/download/#section=windows)
- [Sublime Text 3](https://www.sublimetext.com/3)
- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [PEP8 Code Checker](http://pep8online.com/)

## Contact Information
**"Mohamed Rami" Toutenane 
Email: Mhtoutenane119@cit.just.edu.jo**
