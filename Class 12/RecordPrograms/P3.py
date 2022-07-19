import pandas as pd
li=[]
ele=''
n=int(input("Enter number of areas you want in the series:"))
for i in range(n):
    ele=input("Enter Area:")
    li.append(ele)
s1=pd.Series(li)
s1.sort_values()
print("Smallest areas",s1.tail)
print("Largest areas",s1.head)