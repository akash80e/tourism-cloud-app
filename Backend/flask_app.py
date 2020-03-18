from flask import Flask
from flask import request
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
## Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb://akash:akashbharti@docdb-2020-03-10-02-58-58.cluster-ccv8tdst8buw.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

##Specify the database to be used
db = client.tourism

##Specify the collection to be used
col = db.places

##Insert a single document
col.insert_one(
{
        "id": "1",
        "name": "toronto",
        "title": "Capital of Ontario"
}
)
col.insert_one(
{
    "id": "2",
    "name": "Halifax",
    "title": "Capital of Nova Scotia"
}
)
col.insert_one(
{
        "id": "2",
        "name": "Halifax",
        "title": "Capital of Nova Scotia"
}
)

##Find the document that was previously written
x = col.find_one({'name':'Halifax'})

##Print the result to the screen
print(x)

##Close the connection
client.close()



app.config["MONGO_URI"] = "mongodb://localhost:27017/tourism"
mongo = PyMongo(app)
@app.route('/<keyword>', methods=['GET'])
def getPlace(keyword):
    #keyword = 'Hollow'
    st = '.*' + keyword + '.*'
    regx = re.compile(st, re.IGNORECASE)
    #regx = re.compile('.*keyword.*', re.IGNORECASE)
    places = mongo.db.places.find({"name": regx})
    return dumps(places, indent = 4)

@app.route('/note', methods=['POST'])
def saveNote():
    note_id = request.json['id']
    note = request.json['body']
    print(note_id, note)
    return "Submitted"


if __name__ == '__main__':
    app.run(debug=True)
