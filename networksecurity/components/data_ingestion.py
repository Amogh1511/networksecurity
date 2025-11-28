from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

#configuration of the Data Ingestion Config
from networksecurity.entity.config_entity import DataIngestionConfig
import os
import sys
import pymongo
from pymongo import MongoClient
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split
from networksecurity.entity.artifect_entity import DataIngestionArtifact
import dotenv
dotenv.load_dotenv()

url=os.getenv("mongo_db_key")

#1. Data Ingestion Config
class DataIngestion:
     def __init__(self,data_ingestion_config:DataIngestionConfig):
            try:
                self.data_ingestion_config=data_ingestion_config
            except Exception as Exp:
                raise NetworkSecurityException(Exp,sys)
    #Export data as dataframe from MongoDB Collection
     def export_dataframe(self):
         try:
              database_name=self.data_ingestion_config.database_name
              collection_name=self.data_ingestion_config.collection_name
              self.mongo_client=pymongo.MongoClient(url)
              collection=self.mongo_client[database_name][collection_name]

              df=pd.DataFrame(list(collection.find()))
              if "_id" in df.columns.to_list():
                   df=df.drop(columns=["_id"],axis=1)
              df.replace({"na":np.nan},inplace=True)
              return df
         except Exception as Exp:
              raise NetworkSecurityException
         
#Export data from MongoDB ti feature store
     def export_data_to_feature_store(self,dataframe:pd.DataFrame):
         try:
              feature_store_file_path=self.data_ingestion_config.feature_store_file_path
              #creating folder
              dir_path = os.path.dirname(feature_store_file_path)
              os.makedirs(dir_path,exist_ok=True)
              dataframe.to_csv(feature_store_file_path,index=False, header=True)
              return dataframe
         except Exception as Exp:
              raise NetworkSecurityException(Exp,sys)
     
     def split_data_to_train_test(self,dataframe: pd.DataFrame):
          try:
               trainset,testset = train_test_split(
                    dataframe,test_size=self.data_ingestion_config.train_test_split_ration
               )
               logging.info("""Performed train test split on the dataframe
                            Exited split_data_as_train_test method of data_ingestion""")
               dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
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
         
#2. Initiate Data Ingestion
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

         














