import json
import pymongo
import pandas as pd
MONGODB_DATABASE = 'Examen'
try:
    client = pymongo.MongoClient("mongodb+srv://Examen:examen@cluster0.60gzs.mongodb.net/Twiter?retryWrites=true&w=majority")
    client.server_info()
    print ('OK -- Connected to MongoDB Atlas at server %s' % ('cluster0'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB Atlas connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB Atlas: %s' % error)
db = client.Examen
col = db.examen  
mycursor = col.find()

aux=[]
for item in mycursor:
    aux.append(item)
    
pd.DataFrame([aux]).to_csv('examen.csv', index=False)