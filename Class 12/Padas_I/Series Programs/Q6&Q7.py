#Q6
import pandas as pd
s=pd.Series([i for i in range(50,100,5)],index=[i for i in 'ABCDEFGHIJ'])
print(s)
#Q7
print(s['B':'C'])
