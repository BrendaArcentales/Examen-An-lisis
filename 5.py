import couchdb
import requests
from pymongo import MongoClient

#Conexion a couchDb
URL = 'http://admin:brenda@127.0.0.1:5984'

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
db = server['twitter-examen']

#Conexion a mongodb
Client = MongoClient('mongodb://localhost:27017')
try:
    Client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

dbs = Client.get_database('Examen')

db1 = dbs.Twitter

#Recopilar los documenos de la base de couchDB y guardarlos de uno en uno en mongoDB
for id in db:
    if(db1.find_one({"_id" : db[id].id})):
        print("This id of the document already exist")
    else:
        db1.insert_one(db[id])