import pandas as pd
stud=pd.Series(['Shyam','Mohan','Rahul','Rohit','Ramesh','Ram'])
Result=pd.DataFrame({'Name':stud,'Percentage':[90,95,92,90,93,92]})
print(Result)
print("Extract data:",'\n',"1.Column wise",'\n',"2.Column wise series object(iteritems())")
x=int(input("Enter option:"))
if x==1:
    print(Result.iloc[:,0:2])
elif x==2:
    for x,y in Result.iteritems():
        print(x)
        print(y)
else:
    print("Error 404")