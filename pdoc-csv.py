# Use with : template.docx in same dir
# pip install python-docx
# pip install docxtpl <- Better for making new files from a template
import random
import time
import csv
import pandas as pd
from docxtpl import DocxTemplate

start_time = time.time()

# Source CSV - column names that must match the *** that are {{ *** }} inside "template.docx"
csvfn = "username.csv"

def mkw(n, fname):
    tpl = DocxTemplate("template.docx") # In same directory
    df = pd.read_csv(csvfn)
    df_to_doct = df.to_dict() # dataframe -> dict for the template render
    x = df.to_dict(orient='records')
    context = x
    tpl.render(context[n])
    tpl.save(f"{fname}.docx" )

    # Wait a random time - increase to (1,2) for tests run.
    # wait = time.sleep(random.randint(1,2))

#-------------------Main---------------------#

df2 = len(pd.read_csv(csvfn))

print ("There will be ", df2, "files")

for i in range(0,df2):
    df = pd.read_csv(csvfn)
    columnsData = df.loc[ : , 'username' ]
    fname = columnsData[i]
    print("Making file: ",f"{i}," ,"..Please Wait...")
    mkw(i, fname)

seconds = time.time() - start_time

print("Time Taken:", time.strftime("%H:%M:%S",time.gmtime(seconds)))
print("Done! - Now check your files")