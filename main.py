#Main imports
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

#Training Pipeline
from networksecurity.entity.config_entity import TrainingPipelineConfig

#imports of Ingestion, Validation, Transformation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation





if __name__ == "__main__":
    try:
        #training
        trainingpipelineconfig=TrainingPipelineConfig()
        
        #data ingestion
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed ")
        print(dataingestionartifact)
        
        #data validation
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validaion = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the Data Validation")
        datavalidationartifact=data_validaion.initiate_data_validation()
        logging.info("Data Validation Completed ")
        print(datavalidationartifact)

        #data transformation
        datatransformationconfig=DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(datavalidationartifact,datatransformationconfig)
        logging.info("Initiate the data Transformation")
        datatransformationartifact=data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)

    except Exception as Exp:
        raise NetworkSecurityException(Exp,sys)
