#Main imports
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig
#imports of Ingestion, Validation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation






if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed ")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validaion = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation")
        data_validation_artifact=data_validaion.initiate_data_validation()
        logging.info("Data Validation Completed ")
        print(data_validation_artifact)




    except Exception as Exp:
        raise NetworkSecurityException(Exp,sys)
