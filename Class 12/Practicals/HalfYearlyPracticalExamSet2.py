import pandas as pd
#Q1
project=pd.DataFrame({'EnrolmentNo':[101,102,103,104],'Name':['Reena','Divya','Geet','Jeet'],'Section':['12','12','12','12'],'Section':['B','C','A','B',],'ProjectName':['DataAnalysis','GraphicalAnalysis','MachineLearning','AppDevlopment']})
print(project)
project.loc[len(project.index)]=['105','Supreet','12','D','Language Processor']
project.loc[len(project.index)]=['106','Gurpreet','12','C','AI']
print(project)
project.insert(4,'Grade',['A','A+','B','B','A+','A'],True)
print(project)
newproject=project.iloc[:,[1,3]]
print(newproject)
newproject2=project.iloc[1:2,]
print(newproject2)
project.insert(2,'SchoolName',['NHVPS','JSS','DPS','NHVPS','DPS','NPS'],True)
print(project)
newproject3=project.iloc[2:3,]
print(newproject3)
project.at[3,'Section']='A'
project.at[3,'Class']='11'
print(project)
project.drop(project.columns[[4]],axis=1,inplace=True)
project.drop(project.columns[[3]],axis=1,inplace=True)
print(project)

#Q2
import matplotlib.pyplot as plt
year=[1960,1970,1980,1990,2000,2010,2022]
Popul_India=[449.98,553.57,783.00,870.133,1000.40,1309.10,1590.51]
Popul_Pakistan=[44.91,58.09,78.07,107.70,138.50,170.60,230.24]
plt.plot(year,Popul_India,color='b')
plt.plot(year,Popul_Pakistan,color='g')
plt.legend()
plt.title("Population chart")
plt.xlabel("Years")
plt.ylabel("Population")
plt.show()

#Q3
import matplotlib.pyplot as plt
import pandas as pd
student=pd.read_csv("//workspaces//Python-Class-12//Students.csv")
student.plot.bar()
student.plot.barh()
plt.show()