import urllib, sys, bs4
import pandas as pd
import csv

with open('output.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    news = pd.read_csv("input.csv")
    with open('Alexa_rank.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=["url","Alexa"])
    
        for i in range(len(news['url'])):
            try:
                rank= bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ news['url'][i]).read(), "xml").find("REACH")['RANK']
                writer.writerow({'url':news['url'][i],'Alexa':str(rank)})
            except:
                writer.writerow({'url':news['url'][i],'Alexa':'None'})       
