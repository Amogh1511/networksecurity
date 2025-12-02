from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

#configuration of the Data Ingestion Config

import os
import sys
import pymongo
from pymongo import MongoClient
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split
from networksecurity.entity.artifect_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataIngestionConfig

# dotenv read from .env file and fetches value Ex. mongo_db_key
import dotenv
dotenv.load_dotenv()

url=os.getenv("mongo_db_key")

#1. Data Ingestion Config
class DataIngestion:
     #Initializing the DataIngestionConfig to know the file and folder paths 
     def __init__(self,data_ingestion_config:DataIngestionConfig):
            try:
                self.data_ingestion_config=data_ingestion_config

            except Exception as Exp:
                raise NetworkSecurityException(Exp,sys)


#1. - Export data as dataframe from MongoDB Collection
     def export_dataframe(self):
         try:
              #DataBase name from which data needs to be retrieved 
              database_name=self.data_ingestion_config.database_name
              #Data Ingestion related constant start with DATA_INGESTION VAR NAME
              collection_name=self.data_ingestion_config.collection_name
              #Connect to MongoDB
              self.mongo_client=pymongo.MongoClient(url)
              #setup database - which i setup in mongo (database name - iamamogh) & (collection Folder name - NetworkData)
              collection=self.mongo_client[database_name][collection_name]
              #Retrieving and creating dataframe from colection data in list form
              df=pd.DataFrame(list(collection.find()))
              #Remoing the "_id" column generated in MongoDB
              if "_id" in df.columns.to_list():
                   #drop "_id" column
                   df=df.drop(columns=["_id"],axis=1)
               #replacing empty rows with nan values
              df.replace({"na":np.nan},inplace=True)
              #return data
              return df
         except Exception as Exp:
              raise NetworkSecurityException


#2. - Exporting data from MongoDB to feature store folder
     def export_data_to_feature_store(self,dataframe:pd.DataFrame):
         try:
              #Feature store file path using 
              feature_store_file_path=self.data_ingestion_config.feature_store_file_path
              #creating folder
              dir_path = os.path.dirname(feature_store_file_path)
              os.makedirs(dir_path,exist_ok=True)
              #To store exported data as raw.csv
              dataframe.to_csv(feature_store_file_path,index=False, header=True)
              return dataframe
         except Exception as Exp:
              raise NetworkSecurityException(Exp,sys)
         

#3. - Spliting data as train and test     
     def split_data_to_train_test(self,dataframe: pd.DataFrame):
          try:
               trainset,testset = train_test_split(
                    dataframe,test_size=self.data_ingestion_config.train_test_split_ration
               )
               logging.info("""Performed train test split on the dataframe
                            Exited split_data_as_train_test method of data_ingestion""")
               dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
               os.makedirs(dir_path,exist_ok=True)
               dir_path=os.path.dirname(self.data_ingestion_config.testing_file_path)
               os.makedirs(dir_path,exist_ok=True)
               logging.info("Exporting train test file path")

               trainset.to_csv(
                    self.data_ingestion_config.training_file_path,index=False,header=True
               )
               testset.to_csv(
                    self.data_ingestion_config.testing_file_path ,index=False,header=True
               )

          except Exception as Exp:
               raise NetworkSecurityException
         
#Final -  Initiate Data Ingestion
     def initiate_data_ingestion(self):
         try:
              #reading data from MongoDB
              dataframe=self.export_dataframe()
              dataframe=self.export_data_to_feature_store(dataframe)
              self.split_data_to_train_test(dataframe)

              dataingestionartifact=DataIngestionArtifact(
                   trained_file_path=self.data_ingestion_config.training_file_path, 
                   tested_file_path=self.data_ingestion_config.testing_file_path
               )
              return dataingestionartifact
         except Exception as Exp:
                raise NetworkSecurityException(Exp,sys)

         