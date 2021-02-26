import pymongo
from bson.objectid import ObjectId

class Database(object):

	# URI = "mongodb+srv://vitor:123mudar@cluster0.c192b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
	URI = "mongodb://mongo:27017"
	DATABASE = None
	COLLECTION = "appointment"

	def inicialize():
		client = pymongo.MongoClient(Database.URI)
		Database.DATABASE =  client['consulta']
		
	def insert(data):
		res = Database.DATABASE[Database.COLLECTION].insert_one(data).inserted_id
		return str(res)

	def get(id):
		res = Database.DATABASE[Database.COLLECTION].find_one({"_id": ObjectId(id)})
		return res

	def getLast():
		res = Database.DATABASE[Database.COLLECTION].find().sort("_id",-1).limit(1)
		return res
	
	def save(item):
		return Database.DATABASE[Database.COLLECTION].save(item)

