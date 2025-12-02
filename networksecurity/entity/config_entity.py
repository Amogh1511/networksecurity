from datetime import datetime
import os
from networksecurity.constants import training_pipeline

#Data directory file name
print(training_pipeline.FILE_NAME)
#Creating directory folder to store splited and feature store preprocessed data 
print(training_pipeline.ARTIFACT_DIR)

#Training Pipeline Config
'''
    It creates a unique artifact folder using the current timestamp.
    Example: artifacts/02_15_2025_18_30_22/

    So every pipeline run gets its own separate folder → no overwriting, easy tracking.

    Used whenever a new ML pipeline run starts to save raw, train, test, model files cleanly.
'''
class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        #tampstamp parameter
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        #pipeline name to github 
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        #Creating directory folder to store splited and feature store preprocessed data 
        self.artifect_name=training_pipeline.ARTIFACT_DIR
        #Creating file path Artifact 
        self.artifect_dir=os.path.join(self.artifect_name,timestamp)
        self.timestamp: str=timestamp

#DataIngestion Config
'''
    This class builds all file paths, folder names, collection name, database name
    and split ratio using constants from training_pipeline.
    
    To keep all Data Ingestion settings (paths, names, ratios) in one clean config object.
    
    Used before ingestion starts—so your pipeline knows where to save raw data, 
    where to save train/test, and which Mongo DB/collection to read from.
'''
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        #The Data preprocessed after Train-Test split are stored in this folder 
        self.data_ingestion_dir: str= os.path.join(
            training_pipeline_config.artifect_dir,training_pipeline.DATA_INGESTION_DIR_NAME
             )
        
        #data ingested from Mongo and stored in feture store data folder as raw.csv
        self.feature_store_file_path: str= os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DATA
                                    ,training_pipeline.FILE_NAME
             )
        
        #Train-Test split folder name where data stored in folder as train.csv and test.csv
        self.training_file_path: str= os.path.join(
            self.data_ingestion_dir ,training_pipeline.DATA_INGESTION_INGESTED_DIR
                                    ,training_pipeline.TRAIN_FILE_NAME
             )
        
        #Train-Test split folder name where data stored in folder as train.csv and test.csv
        self.testing_file_path: str= os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR
                                   ,training_pipeline.TEST_FILE_NAME
             )
        
        #Train-Test split ratio used white spliting the data 
        self.train_test_split_ration: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION

        #Data Ingestion related constant start with DATA_INGESTION VAR NAME
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME

        #DataBase name from which data needs to be retrieved 
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifect_dir,
                   training_pipeline.DATA_VALIDATION_DIR_NAME)
        
        self.valid_data_dir: str = os.path.join(self.data_validation_dir,
                    training_pipeline.DATA_VALIDATION_VALID_DIR)
        
        self.invalid_dir: str = os.path.join(self.data_validation_dir,
                    training_pipeline.DATA_VALIDATION_INVALID_DIR)
        
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir,
                    training_pipeline.TRAIN_FILE_NAME)
        
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir,
                    training_pipeline.TEST_FILE_NAME)
        
        self.invalid_train_file_path: str = os.path.join(self.invalid_dir,
                    training_pipeline.TRAIN_FILE_NAME)
        
        self.invalid_test_file_path: str = os.path.join(self.invalid_dir,
                    training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
                    self.data_validation_dir,
                    training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
                    training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)










