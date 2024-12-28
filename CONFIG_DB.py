import pymongo

client = pymongo.MongoClient(
        "mongodb://aopenhimer:leyenda2009@cluster0-shard-00-00.hr9qd.mongodb.net:27017,cluster0-shard-00-01.hr9qd.mongodb.net:27017,cluster0-shard-00-02.hr9qd.mongodb.net:27017/?ssl=true&replicaSet=atlas-xlt5ts-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"
)

result = str(client)

if "connect=True" in result:
    try:
        print("CONFIG DB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("CONFIG DB CONNECTION FAILED ❌")
    except:
        pass


COLLECTIONS = client["CONFIG_DATABASE"]
BLACKLISTED_SKS = COLLECTIONS.BLACKLISTED_SKS
TOKEN_DB = COLLECTIONS.TOKEN_DB
SKS_DB = COLLECTIONS.SKS_DB
