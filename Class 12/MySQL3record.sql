CREATE TABLE PROJECT(
  PROJECTID CHAR(3) PRIMARY KEY,
  PROJECTNAME VARCHAR(255),
  SUBMISSIONDATE DATE,
  TEAMSIZE INT,
  GUIDETEACHER VARCHAR(255)
);

CREATE TABLE PROJECT_ASSIGNED(
  REGISTRATIONID CHAR(6) PRIMARY KEY,
  PROJECTID CHAR(3),
  ASSIGNDATE DATE,
  MARKS INT
);

CREATE TABLE STUDENT(
  ROLLNO INT PRIMARY KEY,
  NAME VARCHAR(255),
  STREAM VARCHAR(255),
  SECTION CHAR(2),
  REGISTRATIONID CHAR(6)
);

ALTER TABLE PROJECT_ASSIGNED SET ENGINE = INNODB;

ALTER TABLE STUDENT SET ENGINE = INNODB;

ALTER TABLE STUDENT ADD FOREIGN KEY(REGISTRATIONID) references PROJECT_ASSIGNED(REGISTRATIONID);
  
ALTER TABLE PROJECT_ASSIGNED ADD FOREIGN KEY(PROJECTID) REFERENCES PROJECT(PROJECTID);

-- Q2
INSERT INTO PROJECT VALUES
("P1", "PHYSICS", "2019-12-21", 2, "DHANYA"),
("P2", "CHEMISTRY", "2020-07-24", 2, "SHOBHA"),
("P3", "INFORMATICS PRACTICES", "2020-08-23", 3, "PRAVIN"),
("P4", "BIOLOGY", "2020-07-14", 3, "SHREYA"),
("P5", "COMP.SC", "2020-06-18", 4, "SOWMYA"),
("P6", "ACCOUNTANCY", "2020-06-23", 5, "GURU");

INSERT INTO PROJECT_ASSIGNED VALUES
("R1001", "P1", "2019-11-21" ,30),
("R1002", "P2", "2020-06-24" ,70),
("R1003", "P3", "2020-07-23" ,100),
("R1004", "P1", "2020-06-14" ,30),
("R1005", "P2", "2020-05-18" ,70),
("R1006", "P3", "2020-05-23" ,100);

INSERT INTO STUDENT VALUES
(1, "Arathi Verma", "Science", "A", "R1001"),
(2, "Shreyas Jain", "Commerce", "B", "R1002"),
(3, "Prabha Nayak", "Science", "A", "R1003"),
(4, "Anupama Rao", "Humanities", "C", "R1004"),
(5, "Rashi Mehta", "Commerce", "B", "R1005"),
(6, "Raghuram Shenoy", "Humanities", "C", "R1006");

-- Q3
SELECT NAME FROM STUDENT WHERE STREAM= "SCIENCE";

-- Q3
DESC STUDENT;

-- Q4
-- STUDENT - RNO , PROJECT_ASSIGNED - REGISTRATIONID , PRJECT - PID

-- Q5
-- STUDENT - FKEY - REGID , PROJECT_ASSIGN - FKEY - PID

-- Q6
SELECT * FROM STUDENT,PROJECT_ASSIGNED;

-- Q7
SELECT * FROM STUDENT,PROJECT_ASSIGNED WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID;

-- Q8
-- UMM DOESNT WORK :(
SELECT STUDENT.NAME FROM STUDENT,PROJECT_ASSIGNED,PROJECT 
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID AND PROJECT.PROJECTID = PROJECT_ASSIGNED.PROJECTID
    GROUP BY STUDENT.STREAM, PROJECT.GUIDETEACHER
    HAVING STUDENT.STREAM = "COMMERCE";

-- Q9
SELECT STREAM,COUNT(*) AS "NO OF STUDENTS" FROM STUDENT
    GROUP BY STREAM
    HAVING STREAM IN("SCIENCE","COMMERCE");

-- Q10
SELECT STUDENT.STREAM , SUM(PROJECT_ASSIGNED.MARKS) AS "TOTAL MARKS", AVG(PROJECT_ASSIGNED.MARKS) AS "AVG MARKS"
    FROM STUDENT,PROJECT_ASSIGNED
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID
    GROUP BY STUDENT.STREAM;

-- Q11
SELECT STUDENT.STREAM , MAX(PROJECT_ASSIGNED.MARKS) AS "MAX MARKS", MIN(PROJECT_ASSIGNED.MARKS) AS "MIN MARKS" 
    FROM STUDENT,PROJECT_ASSIGNED
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID
    GROUP BY STUDENT.STREAM;

-- Q13
SELECT ROLLNO,NAME,STUDENT.REGISTRATIONID,PROJECTID 
  FROM STUDENT,PROJECT_ASSIGNED 
  WHERE STUDENT.REGISTRATIONID=PROJECT_ASSIGNED.REGISTRATIONID AND STREAM = "SCIENCE";

-- Q14
SELECT PROJECTID,PROJECTNAME,SUBMISSIONDATE FROM PROJECT
    WHERE SUBMISSIONDATE = "2020-11-19";

-- Q15
SELECT * FROM PROJECT_ASSIGNED,PROJECT
    WHERE PROJECT.PROJECTID = PROJECT_ASSIGNED.PROJECTID AND TEAMSIZE > 4;

-- Q16
-- MIND NUMBING QUESTION - WHATS THE POINT OF A FUCKING QUERY IF IT DOESNT HAVE ANY FUCKING EFFECT
UPDATE PROJECT
    SET TEAMSIZE = 3
    WHERE TEAMSIZE < 2;

-- Q17
SELECT * FROM PROJECT,STUDENT,PROJECT_ASSIGNED
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID 
    AND PROJECT_ASSIGNED.PROJECTID = PROJECT.PROJECTID 
    AND STUDENT.STREAM IN ("SCIENCE", "COMMERCE") 
    AND PROJECT.TEAMSIZE >= 3;

-- Q18
UPDATE STUDENT
    SET STREAM = "ARTS"
    WHERE STREAM = "HUMANITIES";

-- Q19
SELECT * FROM STUDENT,PROJECT_ASSIGNED
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID
    ORDER BY STUDENT.NAME;

-- Q20
SELECT PROJECT.PROJECTID,PROJECT.PROJECTNAME,PROJECT.GUIDETEACHER,PROJECT_ASSIGNED.ASSIGNDATE 
    FROM PROJECT,PROJECT_ASSIGNED
    WHERE PROJECT.PROJECTID = PROJECT_ASSIGNED.PROJECTID 
    ORDER BY ASSIGNDATE DESC;

-- Q21
ALTER TABLE PROJECT MODIFY
    TEAMSIZE INT CHECK(TEAMSIZE > 0);

-- Q22
SELECT PROJECTID, SUM(MARKS)  AS "TOTAL MARKS" 
    FROM PROJECT_ASSIGNED
    GROUP BY PROJECTID
    HAVING PROJECTID = "P1";

-- Q23
SELECT * FROM STUDENT Natural Project_assigned;

-- Q24
SELECT * FROM PROJECT_ASSIGNED, PROJECT 
    WHERE PROJECT_ASSIGNED.PROJECTID = PROJECT.PROJECTID AND PROJECT.PROJECTID = "P3";

-- Q25
SELECT NAME,STREAM,STUDENT.REGISTRATIONID,PROJECT_ASSIGNED.MARKS
    FROM STUDENT,PROJECT_ASSIGNED
    WHERE STUDENT.REGISTRATIONID = PROJECT_ASSIGNED.REGISTRATIONID;