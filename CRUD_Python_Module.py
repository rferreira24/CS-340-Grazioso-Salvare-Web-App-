# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self,username,password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        # Updated password 
        PASS = 'RyanSNHU2499'
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    # Step 2a: method that inserts a document into acc database and collection 
    # Returns True if insert was successful 
    def create(self, data):
        if data is not None: 
            self.collection.insert_one(data)
            return True              
        else: 
            return False 

    # Create method to implement the R in CRUD.
    # Step 2b: Method that queries for documents from aac database and collection 
    # Returns result in list if successfull
    def read(self, query):
        if query is not None:
            results = self.collection.find(query)
            return list(results)
        else: 
            return[]
        
    # Create method to impelemnt U and CRUD 
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            results = self.collection.update_many(
                query, 
                {"$set": new_values}
            )
            return results.modified_count
        else:
            return 0
        
    # Create Method to implement D in CRUD 
    def delete(self, query):
        if query is not None:
            results = self.collection.delete_many(query)
            return results.deleted_count
        else: 
            return 0 
        