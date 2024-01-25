from pymongo import MongoClient


def store_data(data_to_store):
# Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['pdftask']
    collection = db['extracted_json_files']
    data = data_to_store

    # Inserting data into MongoDB
    collection.insert_one(data)

    # Close MongoDB connection
    client.close()
