from pymongo import MongoClient
import csv
import pandas as pd

#  FOR THE PURPOSE OF PRACTICE I HAVE UPLOADED THIS CSV FILE TO THE MONGODB
# client = MongoClient('mongodb://localhost:27017/')

# db = client['classification_task_db']

# collection = db['training_collection']

# csv_file_kaggle = 'data/kaggleDataForClassificationtask.csv'

# with open (csv_file_kaggle, 'r') as source:
#     reader = csv.DictReader(source)
#     for row in reader:
#         collection.insert_one(row)

#  CONTINUING FROM THIS I WILL IMPORT THE MONGODB DATA AS A DATAFRAME AND EVERYTHING WILL BE THE SAME LIKE DATAINGESTION FROM CSV FILE


client = MongoClient('mongodb://localhost:27017/')

db = client['classification_task_db']

collection = db['training_collection']

cursor = collection.find()

data = list(cursor)

df = pd.DataFrame(data)

print(df.head(10))

df.to_csv('data_from_mongodb.csv')
