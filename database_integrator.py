from pymongo import MongoClient
import pandas as pd
import csv


def store_data(data_to_store):
# Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['pdftask']
    collection = db['extracted_json_files']
    data = data_to_store

    # Inserting data into MongoDB
    collection.insert_one(data)

    client.close()


def retrieve_and_save_csv():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['pdftask']
    collection = db['extracted_json_files']

    cursor = collection.find()

    for data in cursor:
        data.pop('_id')

        csv_filename = 'mydict_data.csv'

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Reference no', 'Name', 'Link', 'Abstract'])

            for key, value in data.items():
                csv_writer.writerow([value['Reference no'], value['Name'], value['ResearchGate link'], value['Abstract']])

        print(f"Data saved to {csv_filename} successfully.")

