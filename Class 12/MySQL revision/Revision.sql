create table employee(empno int primary key,
ename varchar(20) not null,
job varchar(20),
mgr int,
hiredate date,
sal float,
comm float,
deptno int);
insert into employee(empno,ename,job,mgr,hiredate,sal,comm,deptno)
values(8369,'Smith','Clerk',8902,'1990-12-18',800.00,null,20),
values(8499,'Anya','Salesman',8698,'1991-02-20',1600.00,300.00,30),
values(8521,'Seth','Salesman',8698,'1991-02-22',1250.00,500.00,30),
values(8566,'Madhavan','Manager',8839,'1991-04-02',2985.00,null,20),
values(8654,'Momin','Salesman',8698,'1991-09-28',1250.00,1400.00,30),
values(8698,'Bina','Manager',8839,'1991-05-01',2850.00,null,30),
values(8882,'Shivani','Manager',8839,'1991-06-09',2450.00,null,10),
values(8888,'Scott','Analyist',8566,'1992-12-09',3000.00,null,20),
values(8839,'Amir','President',null,'1991-11-18',5000.00,null,10),
values(8844,'Kuldeep','Salesman',8698,'1991-09-08',1500.00,0.00,30),
values(8886,'Anoop','Clerk',8888,'1993-01-12',1100.00,null,20),
values(8900,'Jatin','Clerk',8698,'1991-12-03',950.00,null,30),
values(8902,'Fakir','Analyist',8566,'1991-12-03',3000.00,null,20),
values(8934,'Mita','Clerk',8882,'1992-01-23',1300.00,null,10);
show tables;
desc employee;
SELECT * FROM employee;
SELECT empno,ename,job FROM employee;
SELECT * FROM employee WHERE sal BETWEEN 3000 AND 5000;
SELECT * FROM employee where sal NOT BETWEEN 3000 AND 5000;
SELECT * FROM employee WHERE sal BETWEEN 3000 and 5000 OR job='Salesman';
SELECT * FROM employee WHERE job in('clerk','Salesman');
SELECT * FROM employee WHERE sal>=3000;
SELECT * FROM employee WHERE sal<3000;
SELECT * FROM employee WHERE hiredate<'1991-01-01';
create table empl_copy LIKE employee;
insert into empl_copy select * from Employee;
select*from empl_copy;
SELECT DISTINCT job from employee;
SELECT 22*10;
SELECT * FROM employee where comm IS NULL;
select ename,sal,comm from employee where comm IS NOT NULL;
SELECT ename,'earns a salary of amount',sal FROM employee;
select empno,ename from employee where ename like '%a%';
select empno,ename from employee where ename like '_____';
select * from employee where ename like '____' and job='clerk';
select * from employee where deptno='10' or deptno='20';
drop table empl_copy;
alter table employee add dname varchar(20);
update employee set dname='service' where job='clerk';
alter table employee drop dname; 
