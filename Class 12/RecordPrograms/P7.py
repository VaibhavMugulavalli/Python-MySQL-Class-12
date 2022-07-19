import pandas as pd
import numpy as np
rollno=pd.Series([1,2,3,4,5,6])
percentage1=pd.Series(np.random.randint(70,100,6))
percentage2=pd.Series(np.random.randint(70,100,6))
percentage3=pd.Series(np.random.randint(70,100,6))
percentage4=pd.Series(np.random.randint(70,100,6))
percentage5=pd.Series(np.random.randint(70,100,6))
students={'Roll No':rollno,'Percentage 1':percentage1,'Percentage 2':percentage2,'Percentage 3':percentage3,'Percentage 4':percentage4,'Percentage 5':percentage5}
df=pd.DataFrame(students)
print(df)