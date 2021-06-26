#Name: Chris Gollnick
#Class: CS340-T5459
#Assignment 5-1 Milestone
#Date: 6 June 2021

from pymongo import MongoClient
from bson.objectid import ObjectId



class AnimalShelter(object):
    """CRUD Operations for Animal Collection in MongoDB"""
    def __init__(self,username,password):
        #Initializing the MongoClient to access Mongo DB Database and collections
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:33822/AAC'%(username,password))
        self.database = self.client['AAC']
    
#Create Methodology
    def create(self, data):
        if data is not None:
            fileInsert = self.database.animals.insert(data)
            if fileInsert != 0:
                return "TRUE"
            else:
                return "FALSE"
        else:
            raise Exception("Nothing to save, data parameter empty")
            
#Read Methodology
    def read(self, criteria=None):
        if (criteria):
            data = self.database.animals.find(criteria,{"_id":False})    
        else:
            raise Exception("No Criteria Defined")
        return data
    
    def readAll(self, criteria):
        data = self.database.animals.find(criteria,{"_id":False}).limit(35)           
        return data
    
#Update Methodology
    def update(self,query,newvalue):
        data = self.database.animals.update(query, newvalue)
        if data is not None:
            newData = self.database.animals.find(newvalue, {"_id":False})
        return newData
        
#Delete Methodology
    def delete(self, criteria=None):
        data = self.database.animals.find(criteria, {"_id":False})
        if data is not None:
            delData = self.database.animals.delete_one(criteria)
        return delData