from PIL import Image
import pymongo
import base64
import json
#with open("bird-thumbnail.jpg", "rb") as f:
#  image = Image.open(f)
#with open("bird-thumbnail.jpg", "rb") as f:
# encoded_image = base64.b64encode(f.read())
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["collection1"]
for x in mycol.find({},{ "ref": 1 }):
    if 'ref' in x:
        print (x['ref'])
        image_result = open('image.jpg', 'wb')
        image_result.write(x['ref'])