import os
import sys
import json

import pandas as pd
import numpy as numpy
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()
mongo_uri = os.getenv("mongo_db_key")
#print(mongo_uri)

import certifi
ca=certifi.where()

class networkdataextract():
    def __init__(self):
        try:
            pass
        except Exception as exp:
            raise NetworkSecurityException(exp,sys)
        

    #Convert from CSV --> to JSON
    def csv_to_json(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list[any](json.loads(data.T.to_json()).values())
            
            return records
        
        except Exception as exp:
            raise NetworkSecurityException(exp,sys)
        
    def insert_data_mongo(self, records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            #Connect to MongoDB
            self.mongo_client=pymongo.MongoClient(mongo_uri)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            result=self.collection.insert_many(self.records)

            return result.inserted_ids

        except Exception as exp:
            raise NetworkSecurityException(exp,sys)

if __name__=="__main__":
    FILE_PATH="D:\\networksecurity\\network_data\\phisingData.csv"
    DATABASE="iamamogh"
    COLLECTION="NetworkData"
    NETWORK=networkdataextract()
    RECORDS=NETWORK.csv_to_json(file_path=FILE_PATH)
    inserted_ids=NETWORK.insert_data_mongo(RECORDS,DATABASE,COLLECTION)
    print(len(inserted_ids))


