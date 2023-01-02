import pandas as pd #importing pandas
from urllib.request import urlopen #importing urllib
from bs4 import BeautifulSoup #importing bs4
import re 

def initTableTitles(content): # Finds all containers having tag=table
    tables=content.findAll('table')
    captionList={}
    count=1
    for table in tables:
            # Querying through each table to find all <caption></caption> tags which is commonly used to assign table title
            if(table.findAll('th') or table.find('thead')):
                if(not len(table.findAll('caption'))):
                    heading = table.find_previous_sibling(re.compile("^h[1-6]$"))
                    print(heading)
                    if(heading != None):
                        cleanCaption = (heading.text)[0:-6]
                    else:
                        cleanCaption = " "
                else:
                    captions = list(table.findAll('caption'))
                    print(captions)# Handler for captions returning None/empty list
                    if len(captions):
                        caption = captions[0]# Removes the "\n" at the end of the caption string
                        stripNewLine = str(caption.getText())[:-1]
                    else:
                        stripNewLine = " " # removes all refrencess like [1],[2] by splitting it and then taking the first one
                    captionRefSplit = stripNewLine.split("[")
                    cleanCaption = captionRefSplit[0] # adds to caption dictionary
            else:
                cleanCaption = " "
            count +=1
            captionList[count] = cleanCaption 
    return captionList

def cleanDFs(url,content): #Used to clean data from dirty DF's
    captionlist=initTableTitles(content)# Gets all tables in webpage
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

def getTable(url,content): #Used to retrieve cleandata(filtered out from Dirty Df's)
    cleaneddata=cleanDFs(url,content)
    print("-------TABLES--------")
    tables=cleaneddata[0]
    captions = cleaneddata[1]
    print(captions)
    count = 1 
    for title in captions: #Prints the options to use for each table
        print(f"{count} for {title}")
        count +=1
    num=int(input("Enter table number:"))
    return tables[captions[num-1]]

url=input("Enter valid url:") #User input for URL
response = urlopen(url)
content = BeautifulSoup(response.read(), 'html.parser') #parsing URL 
requireddf=getTable(url,content)
print(".CSV file:",requireddf.to_csv('Scrapped Table CSV')) #Exporting data to CSV file