import pandas as pd 
s1=pd.Series((4570,4560,3460,2350),index=['P','Q','R','S'])
s2=pd.Series(s1)
s2=s2*0.9
print(s2)