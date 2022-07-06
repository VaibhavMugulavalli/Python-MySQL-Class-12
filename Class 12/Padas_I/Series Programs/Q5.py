import pandas as pd
sales=[2345,5432,3456,7654,3456]
s=pd.Series(sales,index=[i for i in range(2001,2006)])
print(s)