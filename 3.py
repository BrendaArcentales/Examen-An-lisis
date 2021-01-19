from facebook_scraper import get_posts
from pymongo import MongoClient
import json
MONGO_HOST = 'mongodb://localhost/Examen'
for post in get_posts('videogames', pages = 1000):
    value = post['time'];
    value2 = post['user_id'];
    text = post['text']; 
    image = post['image'];
    video=  post['video']; 
    likes = post['likes'];
    share =  post['shares'];
    comments = post['comments'];
    link =  post['link'];
    doc = {'user_id' : value2 , 'date:' : value.timestamp(),
    'text' : text, 'image' : image,
    'video': video, 'likes': likes,
    'share': share, 'comments': comments,
    'link': link}
    try:
        client = MongoClient(MONGO_HOST)
        db = client.Examen         
        db.Facebook.insert_one(post)
        print("Dato guardado en MongoDB")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))
