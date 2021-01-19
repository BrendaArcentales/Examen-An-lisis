import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#Script 1: twitter a couch db
ckey = "N31wuT1bPEiM2cmx8ccu1orxb"
csecret = "O4avAsvM6g10JCgRzAnq3mv2QvBqve518tB4ix78dT6u3DAtvh"
atoken = "360193692-rekUZMqpMZFsnVvXovgqCuuVfwtp3aO4gui2O8zl"
asecret = "BW1PeKHghRdZ8YUxYbizidV043U3P7ysxXJvZk8i6AWJX"
class listener(StreamListener):
    
    def on_data(self, data):
        Tweet = json.loads(data)
        try:
            Tweet["_id"] = str(Tweet['id'])
            doc = db.save(Tweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
server = couchdb.Server('http://admin:brenda@localhost:5984/')  
try:
    db = server.create('twitter-examen')
except:
    db = server['quito','violencia','valorant']
twitterStream.filter(track=['quito','yolo'])