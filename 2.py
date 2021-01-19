import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from pymongo import MongoClient
def find_2nd(string,substring):
    return string.find(substring,string.find(substring)+1)
def find_1st(string,substring):
    return string.find(substring,string.find(substring))
response=requests.get('https://www.olx.com.ec/')
soup=BeautifulSoup(response.content,"lxml")
Products=[]
Price=[]
Localitation=[]
Date=[]
post_products=soup.find_all("span", class_="_2tW1I")
post_price=soup.find_all("span",class_="_89yzn")
post_localitation=soup.find_all("span",class_="tjgMj")
post_date=soup.find_all("span",class_="zLvFQ")
for element in post_products:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Products.append(limpio.strip())
for element in post_price:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Price.append(limpio.strip())
for element in post_localitation:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Localitation.append(limpio.strip())
for element in post_localitation:
    element=str(element)
    limpio=str(element[find_1st(element,'>')+1:find_2nd(element,'<')])
    Localitation.append(limpio.strip())
dfDS = pd.DataFrame({'Products':Products,'Price':Price,'Localitation':Localitation, 'Date':Date})
result = dfDS.to_json(orient = "records")
parsed = json.loads(result)
MONGO_HOST = 'mongodb://localhost/Examen'
for post in parsed:
    try:
        client = MongoClient(MONGO_HOST)
        db = client.Examen         
        db.WebScrapping.insert_one(post)
        print("Dato guardado en MongoDB")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))
