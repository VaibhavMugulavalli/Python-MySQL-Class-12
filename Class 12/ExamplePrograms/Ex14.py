import pandas as pd
section=['A','B','C','D']
lst=[39,41,42,44]
s8=pd.Series(lst,index=section)
print("Tickets Amount:",s8[:2]*100)