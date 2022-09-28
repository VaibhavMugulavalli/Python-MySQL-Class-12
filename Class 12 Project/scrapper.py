import pandas as pd #importing pandas library
url='https://en.wikipedia.org/wiki/Formula_One' #Assigning url
df=pd.read_html(url) #Reading html format of url
n=len(df) #Finding number of tables in url
print("Number of tables in webpage:",n)
x=int(input("Enter table number to be selected:")) #User input
if x>n: #Logical Block
    print("Enter correct number of tables")
else:
    df_final=df[x-1] #Creating new df from data extracted from url(indexing starts from 0 therfore x-1)
    print(df_final)
print(".CSV file:",df_final.to_csv('Scrapped Table CSV')) #Exporting data to CSV file
print(".XLSX file:",df_final.to_excel("Scrapped Table Excel.xlsx")) #Exporting data to XLSX file
