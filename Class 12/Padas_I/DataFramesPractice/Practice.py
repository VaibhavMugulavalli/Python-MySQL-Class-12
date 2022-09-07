import pandas as pd
import numpy as np
#Q1
empty_df=pd.DataFrame()
print(empty_df)
#Q2
stud=['Rahul','Ramesh','Rohit','Ram','Suresh']
students=pd.DataFrame(stud)
print(students)
#Q3
players1=pd.DataFrame(['Virat'],['MS Dhoni'],['Anil Kumble'])
players2=pd.DataFrame({'Virat','MS Dhoni','Anil Kumble'})
print(players1,players2)
#Q4
sales_person=pd.Series(['Ram','Shyam','Mohan','Ramesh','Suresh'],index=[50,60,30,42,33])
salesman=pd.DataFrame(sales_person)
print(salesman)
#Q5
countries=pd.DataFrame({'India':["Delhi","1.3B"],'China':['Beijing','1.4B'],'USA':['Washington DC','33M']})
print(countries)
#Q6

#Q7
for(x,y) in players1.iterrows():
    print(x)
    print(y)
#Q8
for(x,y) in salesman.iteritems():
    print(x)
    print(y)
