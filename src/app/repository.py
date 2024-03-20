from models import Results
from config import database 
import uuid

class ResultsRepo(): 
    @staticmethod
    async def retrieve():
        results_list = []
        collection = database.get_collection('results').find()
        async for result in collection: 
            results_list.append(result)
        return results_list
    
    @staticmethod
    async def insert(results: Results):
        id = str(uuid.uuid4())
        results_dict = {
            "_id": id,
            "name": results.name, 
            "x": results.x,
            "y": results.y,
            "scenary": {
                "bullet_weight": results.scenary.bullet_weight,
                "distance": results.scenary.distance,
                "ammo": results.scenary.ammo,
                "temperature": results.scenary.temperature,
                "altitude": results.scenary.altitude,
                "humidity": results.scenary.humidity,
                "scenary": results.scenary.scenary,
                "stress_level": results.scenary.stress_level,
                "caliber": results.scenary.caliber
            }
        }
        await database.get_collection('results').insert_one(results_dict)

    @staticmethod
    async def update(id:str, results: Results): 
        results_dict = await database.get_collection('results').find_one({"_id": id})
        results_dict["name"] = results.name
        results_dict["x"] = results.x
        results_dict["y"] = results.y
        results_dict["scenary"] = {
            "bullet_weight": results.scenary.bullet_weight,
            "distance": results.scenary.distance,
            "ammo": results.scenary.ammo,
            "temperature": results.scenary.temperature,
            "altitude": results.scenary.altitude,
            "humidity": results.scenary.humidity,
            "scenary": results.scenary.scenary,
            "stress_level": results.scenary.stress_level,
            "caliber": results.scenary.caliber
        }
        await database.get_collection('results').update_one({"_id": id}, {"$set": results_dict})

    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection('results').find_one({"_id": id})
    
    @staticmethod
    async def delete(id: str):
        await database.get_collection('results').delete_one({"_id": id})
