import requests
import dns
import json
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
from argparse import ArgumentParser
#Conexion a mongodb

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')#Indicarparametrosdel servidor

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

#SeleccionarSchema
DBS = ['Twitter-Violencia']


#Conexion a mongodb Atlas
SERVER = pymongo.MongoClient("mongodb+srv://Examen:examen@cluster0.60gzs.mongodb.net/Twiter?retryWrites=true&w=majority")

try:
    SERVER.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBSA = SERVER.get_database('mongoDB_to_mongoDBATlas')
dbsCollectionA = DBSA.violenciacopy

for db in DBS:
    if db in ('Twitter-Examen'):  
        cols = CLIENT[db].list_collection_names() 
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbsCollectionA.insert_one(documents)
                    print("Guardado Exitosamente")
                    print(documents)
                except:
                    print("El doc ya existe")