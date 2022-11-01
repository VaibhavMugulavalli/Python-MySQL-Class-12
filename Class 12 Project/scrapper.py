import pandas as pd #importing pandas library
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def initTableTitles(content):
    # Finds all containers having tag = table
    tables=content.findAll('table')
    captionList={}
    count=1
    
    for table in tables:
        # Querying through each table to find all <caption></caption> tags which is conventionally used to assign table title
        captions = list(table.findAll('caption'))
        print(captions)
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

def cleanDFs(url,content):
    captionlist=initTableTitles(content)
    # Gets all tables in webpage
    dirtyDF = pd.read_html(url)
    dfDict = {}
    cleanedTableTitles = []
    count = 0
    for (key,caption) in captionlist.items() :
        if(caption != ' '):
            dfDict[caption] = dirtyDF[count]
            cleanedTableTitles.append(caption)
        count +=1
    CleanTable = dfDict
    
    return [CleanTable,cleanedTableTitles]

def getTable(url,content):
    cleaneddata=cleanDFs(url,content)
    print("-------TABLES--------")
    tables=cleaneddata[0]
    captions = cleaneddata[1]
    print(captions)
    count = 1
    # Prints the options to use for each table
    for title in captions:
        print(f"{count} for {title}")
        count +=1
    num=int(input("Enter table number:"))
    return tables[captions[num-1]]


url=input("Enter valid url:") #Assigning url
response = urlopen(url)
content = BeautifulSoup(response.read(), 'html.parser')

requireddf=getTable(url,content)
print(".CSV file:",requireddf.to_csv('Scrapped Table CSV')) #Exporting data to CSV file

