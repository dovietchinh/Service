import pymongo

class MyMongo():

    def __init__(self,mongo_string=None):
        if mongo_string is None:
            mongo_string = "mongodb://root:root@localhost:37017/"
        self.mongo_string = mongo_string
        self.client = pymongo.MongoClient(self.mongo_string)
        self.all_db = self.client.list_database_names()
        self.db_selected = None
        
    def write_one_document(self,db_name,collection_name,document):
        db = self.client[db_name]
        collection = db[collection_name]
        collection.insert_one(document)

    def list_databases(self):
        return self.client.list_database_names()
    
    def select_db(self,index):
        self.db_selected = index 
    

    def list_collections(self):
        db = self.client[self.all_db[self.db_selected]]
        return db.list_collection_names()
    
    def list_collection(self,index):
        db = self.client[self.all_db[self.db_selected]]
        return db.list_collection_names()[index]
        
    def read_one_document(self,collection_name):
        db = self.client[self.all_db[self.db_selected]]
        collection = db[collection_name]
        return collection.find_one()

if __name__ == "__main__":
    m = MyMongo()
    print(m.list_databases())
    m.select_db(0)
    print(m.list_collections())
    print(m.list_collection(0))
    m.write_one_document('db_name',"my_collection",{"name":"John","age":30})
    print(m.read_one_document("my_collection"))