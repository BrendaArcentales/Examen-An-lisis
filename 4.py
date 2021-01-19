import sqlite3 as sq
import pandas as pd
import json
from pymongo import MongoClient
con=sq.connect("database.db")
dfsqlite=pd.read_sql_query("SELECT * FROM compras",con)
result = dfsqlite.to_json(orient ="records")
parsed=json.loads(result)
MONGO_HOST = 'mongodb://localhost/Examen'
for post in parsed:
    try:
        client = MongoClient(MONGO_HOST)
        db = client.Examen         
        db.SQLITE.insert_one(post)
        print("Dato guardado en MongoDB")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))