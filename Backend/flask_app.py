from flask import Flask
from flask import request
#from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
## Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
#mongo = pymongo.MongoClient('mongodb://akash:akashbharti@tourismapp.cluster-ccv8tdst8buw.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')


mongo = pymongo.MongoClient('mongodb://localhost')
##Specify the database to be used
db = mongo.tourism

##Specify the collection to be used
col = db.places

@app.route('/<keyword>', methods=['GET'])
def getPlace(keyword):
    st = '.*' + keyword + '.*'
    regx = re.compile(st, re.IGNORECASE)
    #regx = re.compile('.*keyword.*', re.IGNORECASE)
    places = col.find({'name': regx})
    return dumps(places, indent = 4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
