import traceback
import pymongo

client = pymongo.MongoClient(
        "mongodb://aopenhimer:leyenda2009@cluster0-shard-00-00.khkbp.mongodb.net:27017,cluster0-shard-00-01.khkbp.mongodb.net:27017,cluster0-shard-00-02.khkbp.mongodb.net:27017/?ssl=true&replicaSet=atlas-45bvo3-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

)
result = str(client)

if "connect=True" in result:
    try:
        print("MONGODB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("MONGODB CONNECTION FAILED ❌")
    except:
        pass

folder = client["MASTER_DATABASE"]
usersdb = folder.USERSDB
chats_auth = folder.CHATS_AUTH
gcdb = folder.GCDB
sksdb = client["SKS_DATABASE"].SKS
confdb = client["SKS_DATABASE"].CONF_DATABASE
