import pandas as pd #importing pandas library
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


def __initTableTitles__(content):
    # Finds all containers having tag = table
    tables=content.findAll('table')
    captionList={}
    count=1
    
    for table in tables:
        # Querying through each table to find all <caption></caption> tags which is conventionally used to assign table title
        captions = list(table.findAll('caption'))
        # Handler for captions returning None/empty list
        if len(captions):
            caption = captions[0]
            # Removes the "\n" at the end of the caption string
            stripNewLine = str(caption.getText())[:-1]
        else:
            stripNewLine = " "
        # removes all refs like [8][9] by splitting it and then taking the first one
        captionRefSplit = stripNewLine.split("[")
        cleanCaption = captionRefSplit[0]
        # adds to caption dictionary
        captionList[count] = cleanCaption
        count +=1
    # assgins tableTitles attribute to object

    return captionList


url=input("Enter valid url:") #Assigning url


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
