##Pushing data to MongoDB from local --> to MongoDB Database via ETL 
import os
import sys
import json

import pandas as pd
import numpy as numpy
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# dotenv read from .env file and fetches value Ex. mongo_db_key
from dotenv import load_dotenv
load_dotenv()
#assign to a variable
mongo_uri = os.getenv("mongo_db_key")
print(mongo_uri)

#To make HTTP request safe or to make API calls we use certifi library and make sure to avoid errors
# Connecting to a trusted, secure website, and protect network security
#importing certifi for internet safety 
import certifi
ca=certifi.where()


#Constructing an object networkextract for initializing
# It reads CSV → converts to JSON → inserts into MongoDB
class uploadingnetworkdata():
    def __init__(self):
        try:
            pass
        except Exception as exp:
            raise NetworkSecurityException(exp,sys)
        

    #Convert from CSV --> to JSON
    def csv_to_json(self, file_path):
        try:
            #read csv file
            data=pd.read_csv(file_path)
            #reset index
            data.reset_index(drop=True,inplace=True)
            # To convert each CSV row into a JSON-like Python dict to insert into MongoDB
            # data.T.to_json() → converts CSV to JSON after transposing.
            #json.loads() → loads that JSON as a dict.
            #.values() → takes only the row values.
            # list() → returns in list
            records=list(json.loads(data.T.to_json()).values())
            
            return records
        
        except Exception as exp:
            raise NetworkSecurityException(exp,sys)
        
    def insert_data_mongo(self, records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            #Connect to MongoDB
            self.mongo_client=pymongo.MongoClient(mongo_uri,tlsCAFile=ca)
            #setup database - which i setup in mongo (database name - iamamogh)
            self.database=self.mongo_client[self.database]
            #takes all data as collection (data)
            self.collection=self.database[self.collection]
            #insert_many() returns a result 
            result=self.collection.insert_many(self.records)
            logging.info("data inserted")
            #where ids are generated in mongo for every row
            #and it will return results of ids of each data uploaded in mongo for verification 
            return result.inserted_ids

        except Exception as exp:
            raise NetworkSecurityException(exp,sys)

if __name__=="__main__":
    #file path of my data in local
    FILE_PATH=r"D:\\MyProjects\\networksecurity\\network_data\\phisingData.csv"
    #database name I created in mongo
    DATABASE="iamamogh"
    #NetworkData is just a collection name storing in Mongo (like a folder name)
    # and phisingdata.csv file will be inside the networksecurity folder
    COLLECTION="NetworkData"
    #initialize the class
    NETWORK=uploadingnetworkdata()
    #reading the file path and convert data from csv -> json
    # data are called recordsin mongo, and they are creacted 
    RECORDS=NETWORK.csv_to_json(file_path=FILE_PATH)
    #Insert data to mongo by taking Records(data),database(database name), Collection(folder name)
    inserted_ids=NETWORK.insert_data_mongo(RECORDS,DATABASE,COLLECTION)
    #returns the list of data that were uploaded
    #If they are uploaded then it returns row data by returning the ids as verified
    print(len(inserted_ids))

