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
select ename,instr(ename,'ta') as 'ename with tr' from employee;
#
select dayofweek(hiredate),dayofmonth(hiredate),monthname(hiredate);
select now();
select ename,job,sal,hiredate from employee where hiredate between '1990-05-20' and '1991-12-31' order by hiredate;
