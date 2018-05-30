import urllib, sys, bs4
import pandas as pd
import csv

with open('merged_new.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    news = pd.read_csv("merged_new.csv")
    with open('Alexa_new.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=["url","Alexa"])
    
        for i in range(len(news['url'])):
            try:
                
#                print news['url'][i]
                rank= bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ news['url'][i]).read(), "xml").find("REACH")['RANK']
#                print rank
                
                writer.writerow({'url':news['url'][i],'Alexa':str(rank)})
            except:
                writer.writerow({'url':news['url'][i],'Alexa':'None'})
#                pass
    
    
    
    
    
    
#    with open('alexa.csv', 'wb') as csvfile:
#            writer = csv.DictWriter(csvfile,fieldnames=["url","Alexa"])
#            
##            for row in reader['url']:

                
