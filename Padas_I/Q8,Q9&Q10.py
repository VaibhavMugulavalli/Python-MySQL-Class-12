#8
import pandas as pd
PriceData=[23000,34500,56000,45000]
Item=['TV','FRIDGE','OVEN','LAPTOP']
s=pd.Series(PriceData,index=Item)
print(s)
#9
print(s['FRIDGE'])
#10
print(s[2])