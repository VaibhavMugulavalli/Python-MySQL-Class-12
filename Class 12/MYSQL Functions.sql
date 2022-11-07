#MySQL 1
create table employee(empno int,
ename varchar(20),
job varchar(20),
mgr int,
hiredate date,
sal float,
comm float,
deptno int);
insert into employee(empno,ename,job,mgr,hiredate,sal,comm,deptno)
values(8369,'Smith','Clerk',8902,'1990-12-18',800.00,null,20),
(8499,'Anya','Salesman',8698,'1991-02-20',1600.00,300.00,30),
(8521,'Seth','Salesman',8698,'1991-02-22',1250.00,500.00,30),
(8566,'Madhavan','Manager',8839,'1991-04-02',2985.00,null,20),
(8654,'Momin','Salesman',8698,'1991-09-28',1250.00,1400.00,30),
(8698,'Bina','Manager',8839,'1991-05-01',2850.00,null,30),
(8882,'Shivani','Manager',8839,'1991-06-09',2450.00,null,10),
(8888,'Scott','Analyist',8566,'1992-12-09',3000.00,null,20),
(8839,'Amir','President',null,'1991-11-18',5000.00,null,10),
(8844,'Kuldeep','Salesman',8698,'1991-09-08',1500.00,0.00,30),
(8886,'Anoop','Clerk',8888,'1993-01-12',1100.00,null,20),
(8900,'Jatin','Clerk',8698,'1991-12-03',950.00,null,30),
(8902,'Fakir','Analyist',8566,'1991-12-03',3000.00,null,20),
(8934,'Mita','Clerk',8882,'1992-01-23',1300.00,null,10);

select concat(empno,ename) as "full name "from employee;
select upper(ename) as 'upper' from employee;
select upper(ename) as 'upper',lower(ename) as 'lower' from employee where deptno=10;
select concat(upper(ename),lower(job)) as 'joint' from employee;
select substr(ename,1,5),sal from employee order by ename desc;
select right(ename,3),sal from employee where sal between 2500 and 5000;
select substr(ename,3,7) from employee where ename like 's%';
select ename,job,round(sal,1) as 'round' from employee;
select ename,job,sal,sal*12 as 'annual sal' from employee;
select trim(ename) as 'trimmed ename' from employee;
select ename,count(ename) as 'total',instr(ename,'a') as 'a in ename' from employee;	
select sysdate();
select right(date(),8);
select dayname('2004-09-15'),monthname('2004-09-15'),dayofyear('2004-09-15');
select ename,round(comm,0) as 'rounded comm' from employee;
select ename,instr(ename,'ta') as 'ename with ta' from employee;
#
select dayofweek(hiredate),dayofmonth(hiredate),monthname(hiredate);
select now();
select ename,job,sal,hiredate from employee where hiredate between '1990-05-20' and '1991-12-31' order by hiredate;
select year(curdate()),hiredate,concat(curdate,hiredate) as 'curentdate and hiredate' from employee where job like 'analyst';
select hiredate+10 from employee;
#
select mod(sal,2) "modulus";

#MySQL 2
#Q1
create database ExamDB;

#Q2
create table exam(AdmnNO varchar(4),sname varchar(20),percentage float,class varchar(3),stream varchar(15));

#Q3
select*from exam order by sname desc;
select concat(ucase(sname),percentage) from exam;
select substr(sname,2,3) from exam where stream='commerce';
select sname,stream,concat(sname,stream) as NAMEE from exam;
select*from exam where stream='science' and percentage<90;
select left(sname,3) from exam where percentage>80 and percentage<90;
select right(sname,3) from exam where percentage<70 and stream='commerce';
select length(sname) from exam;
select instr(stream,'m') from exam;
select*from exam where sname like '%i%';
select instr(sname,'ia') from exam;
 select substr(sname,3) from exam;
 select pow(6,3);

 #Q4
 SELECT POW(2,3);
+----------+
| POW(2,3) |
+----------+
|        8 |
+----------+

 SELECT ROUND(123.2345, 1), ROUND(342.9234,0);
+--------------------+-------------------+
| ROUND(123.2345, 1) | ROUND(342.9234,0) |
+--------------------+-------------------+
|              123.2 |               343 |
+--------------------+-------------------+

 SELECT LENGTH('Informatics Practices');
+---------------------------------+
| LENGTH('Informatics Practices') |
+---------------------------------+
|                              21 |
+---------------------------------+


mysql> SELECT YEAR("1979/11/26"), MONTH("1979/11/26"), DAY("1979/11/26");
+--------------------+---------------------+-------------------+
| YEAR("1979/11/26") | MONTH("1979/11/26") | DAY("1979/11/26") |
+--------------------+---------------------+-------------------+
|               1979 |                  11 |                26 |
+--------------------+---------------------+-------------------+

 SELECT MONTHNAME("1979/11/26");
+-------------------------+
| MONTHNAME("1979/11/26") |
+-------------------------+
| November                |
+-------------------------+

SELECT LEFT('INDIA',3), RIGHT('Computer Science',4);
+-----------------+-----------------------------+
| LEFT('INDIA',3) | RIGHT('Computer Science',4) |
+-----------------+-----------------------------+
| IND             | ence                        |
+-----------------+-----------------------------+

 SELECT substr('Informatics',3,4), SUBSTR('Practices',3);
+---------------------------+-----------------------+
| substr('Informatics',3,4) | SUBSTR('Practices',3) |
+---------------------------+-----------------------+
| form                      | actices               |
+---------------------------+-----------------------+

 SELECT SYSDATE() , CURDATE() , NOW() ;
+---------------------+------------+---------------------+
| SYSDATE()           | CURDATE()  | NOW()               |
+---------------------+------------+---------------------+
| 2022-11-04 14:23:39 | 2022-11-04 | 2022-11-04 14:23:39 |
+---------------------+------------+---------------------+

 SELECT LCASE('IP CLASS 11 TH ');
+--------------------------+
| LCASE('IP CLASS 11 TH ') |
+--------------------------+
| ip class 11 th           |
+--------------------------+

SELECT CONCAT(LOWER('CLASS'),UPPER('XII'));
+-------------------------------------+
| CONCAT(LOWER('CLASS'),UPPER('XII')) |
+-------------------------------------+
| classXII                            |
+-------------------------------------+

 SELECT MONTHNAME(CURDATE()) ,DAYNAME(CURDATE());
+----------------------+--------------------+
| MONTHNAME(CURDATE()) | DAYNAME(CURDATE()) |
+----------------------+--------------------+
| November             | Friday             |
+----------------------+--------------------+

#Q5
#1. dayname() 
#2. substr() 
#3. date(),monthname(),month() 
#4. upper()

#MySQL 3

#MySQL 4
#Q1
create database empno;
#Q2
insert into employee (ecode,ename,salary,job,city)
 values('R001','Vijay',NULL,'Manager','Delhi'),
 ('R002','Miara',45000,'Executive','Jaipur'),
 ('R003','Shristi',60000,'Analyst','Bengaluru'),
 ('R004','Sushanth',NULL,'Manager','Bengaluru'),
 ('R005','Riya',60000,'Accountant','Kanpur'),
 ('R006','Reena',55000,'Service','Kanpur'),
 ('R007','Siara',36700,'Clerk','Delhi');

