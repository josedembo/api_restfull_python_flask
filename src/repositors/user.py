from src.database.connerction import collection
from bson import json_util, ObjectId
import json

class UserRepositor:
    def insert(self, nome:str, ativo:str):
        user = {"nome":nome,"ativo":ativo}
        id = collection.insert_one(user).inserted_id
        return id
     
    def select(self):
        users = collection.find({})
        users = json.loads(json_util.dumps(users).encode("utf-8"))
        return users
    
    def select_by_id(self, user_id):
        _id = ObjectId(user_id)
        user = collection.find_one({"_id": _id})
        print(user)
        user = json.loads(json_util.dumps(user))
        return user

    def update(self, user_id, nome):
        _id = ObjectId(user_id)
        updates = {
            "$set": {"nome": nome}
        }
        collection.update_one({"_id": _id}, updates)
        
    def delete(self, user_id):
        _id = ObjectId(user_id)
        collection.delete_one({"_id": _id})