import pandas as pd
lst=[1,2,3,4,5,6,7,8,9,10]
S1=pd.Series(lst,index=[1,2,3,4,5,6,7,8,9,10])
print("Sort by:",'\n',"1.Values",'\n',"2.Index")
x=int(input("Enter option:"))
if x==1:
    S1.sort_values(axis=0,ascending=True,inplace=True)
else:
    S1.sort_index(axis=0,ascending=False,inplace=True)
print(S1)
