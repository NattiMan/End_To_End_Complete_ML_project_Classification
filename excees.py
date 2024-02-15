from pymongo import MongoClient

try:
    # Connect to the MongoDB server running on localhost
    client = MongoClient('mongodb://localhost:27017')
    
    # Check if the connection was successful
    if client.server_info():
        print("Successfully connected to MongoDB")
        
        # Access a specific database
        db = client['classification_data_source']
        
        # Access a specific collection within the database
        collection = db['train_database']
        
        # Insert a document into the collection
        result = collection.insert_one({'name': 'John', 'age': 30})
        print("Inserted document ID:", result.inserted_id)
        
        # Find all documents in the collection
        documents = collection.find()
        print("Found documents:")
        for doc in documents:
            print(doc)
            
    else:
        print("Failed to connect to MongoDB")
        
except Exception as e:
    print("An error occurred:", e)
