import pandas as pd
section=['A','B','C','D']
lst=[6700,5600,500,5200]
s13=pd.Series(lst,index=section)
s13[0]=7600
s13[2:]=7000
print("Series after modifying amounts:",s13)