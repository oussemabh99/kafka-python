from PIL import Image
import pymongo
import base64
with open("bird-thumbnail.jpg", "rb") as f:
  image = Image.open(f)
with open("bird-thumbnail.jpg", "rb") as f:
 encoded_image = base64.b64encode(f.read())
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["collection1"]
mydict= { "ref": encoded_image}
x = mycol.insert_one(mydict)
print (x)
