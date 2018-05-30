import csv
import pandas as pd

def filtering():

    with open('results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('filtered.csv', 'wb') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=["Truthiness", "url","Reference","Category"])
            
            for row in reader:
                print row
#                if row["Truthiness"] != "" or row["url"]!="":
#            
#                    writer.writerow(row)
            
        
def merging():        
    with open("merged.csv",'wb') as csvfile:
            
        df = pd.read_csv("filtered.csv")
        dfi = pd.read_csv("more_data.csv")
        df = pd.merge(df,dfi,how = 'outer', on = ["url", "url"])
        df.to_csv("merge.csv")

######already executeed functions###########

filtering()
#merging()
