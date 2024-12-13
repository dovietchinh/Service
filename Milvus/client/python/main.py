from pymilvus import MilvusClient
import os
# Authentication not enabled
# client = MilvusClient("http://localhost:19530")

# client.create_collection(collection_name="test_collection", dimension=5)

# # 3. List collections
# list_collection_names = client.list_collections(timeout=1) 
# print(list_collection_names)

class Command():

    def __init__(self):
        self.client = MilvusClient("http://localhost:19530")

    def create_collection(self, collection_name, dimension):
        # self.client = create_collection(
        #     collection_name: str,
        #     dimension: int,
        #     primary_field_name: str = "id",
        #     id_type: str = DataType,
        #     vector_field_name: str = "vector",
        #     metric_type: str = "COSINE",
        #     auto_id: bool = False,
        #     timeout: Optional[float] = None,
        #     schema: Optional[CollectionSchema] = None, # Used for custom setup
        #     index_params: Optional[IndexParams] = None, # Used for custom setup
        #     **kwargs,
        # ) -> None:

        self.client.create_collection(collection_name=collection_name, dimension=dimension)

    def list_collections(self):
        return self.client.list_collections(timeout=1)
    
    def insert(self, collection_name, vectors):
        self.client.insert(collection_name=collection_name, records=vectors)
    
    def search(self, collection_name, vectors, top_k):
        return self.client.search(collection_name=collection_name, query_records=vectors, top_k=top_k)
    
    def run(self):
        command = None
        while True:
            os.system('clear')
            print("1. Create collection")
            print("2. List collections")
            print("3. Insert")
            print("4. Search")
            print("5. Delete")
            print("6. Exit")
            
            if command == "1":
                collection_name = input("Enter collection name: ")
                dimension = int(input("Enter dimension: "))
                self.create_collection(collection_name, dimension)
            elif command == "2":
                collections = self.list_collections()
                print(collections)
            elif command == "3":
                collection_name = input("Enter collection name: ")
                vectors = input("Enter vectors: ")
                self.insert(collection_name, vectors)
            elif command == "4":
                collection_name = input("Enter collection name: ")
                vectors = input("Enter vectors: ")
                top_k = int(input("Enter top k: "))
                result = self.search(collection_name, vectors, top_k)
                print(result)
            elif command == "5":
                collection_name = input("Enter collection name: ")
                self.client.drop_collection(collection_name=collection_name) 
            elif command == "6":
                exit()
            else:
                pass
            command = input("Enter command: ")
command = Command()
command.run()