import os
import sys
import json

import certifi
import pandas as pd
import numpy as np

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri)
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = MongoClient(uri)
            
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == '__main__':
    FILE_PATH = 'Network_Data/phisingData.csv'
    DATABASE = 'default'
    COLLECTION = 'NetworkData'
    
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_converter(file_path=FILE_PATH)
    no_of_records = network_obj.insert_data_mongodb(records=records,collection=COLLECTION,database=DATABASE)
    print(no_of_records)
