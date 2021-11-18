import pymongo

myclient = pymongo.MongoClient("mongodb+srv://hanzawnyine:HanZaw005@cluster0.icah5.mongodb.net/test")
mydb = myclient["blink"]
mycol = mydb["blink"]

mydict = {"LED": "testing", "starte": 0}

x = mycol.insert_one(mydict)