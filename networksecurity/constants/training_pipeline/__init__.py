import os
import numpy as np

#Creating directory folder to store splited and feature store preprocessed data 
ARTIFACT_DIR:str = "Artifacts"

#Data directory file name
FILE_NAME:str ="phisingData.csv"

#Defining common constants variable for training pipeline

#Pipeline name to github 
PIPELINE_NAME:str = "NetworkSecurity"

#Dataset Target column [Y - Column]
TARGET_COLUMN ="Result"

#train and test file names
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

#Schema file Path
SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

#--------------------------------------------------- Data Ingestion ---------------------------------------------------------------

#Data Ingestion related constant start with DATA_INGESTION VAR NAME
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"

#DataBase name from which data needs to be retrieved 
DATA_INGESTION_DATABASE_NAME: str = "iamamogh"

#The Data preprocessed after Train-Test split are stored in this folder 
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

#data ingested from Mongo and stored in feture store data folder as raw.csv
DATA_INGESTION_FEATURE_STORE_DATA: str = "feature_store"

#Train-Test split folder name where data stored in folder as train.csv and test.csv
DATA_INGESTION_INGESTED_DIR: str = "ingested"

#Train-Test split ratio used white spliting the data 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

#----------------------------------------------------Data Validation -----------------------------------------------------------------

#data Validation related constant starts with Data Validation Var Name

#The Data ingested after Train-Test split are stored in this folder
DATA_VALIDATION_DIR_NAME: str= "data_validation"

#data ingestion valid data will be stored here
DATA_VALIDATION_VALID_DIR: str= "validation"

#data ingestion invalid data will be stored here
DATA_VALIDATION_INVALID_DIR: str= "invalid"

#data validation drift report will be stored here
DATA_VALIDATION_DRIFT_REPORT_DIR: str= "drift_report"

#data validation drift report file name
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str= "report.yaml"

#----------------------------------------------------Data Transformation---------------------------------------------------------------

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"


#for KNN imputer class to replace NaN values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

#----------------------------------------------------Model Trainer---------------------------------------------------------------------


MODEL_TRAINER_DIR_NAME: str="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OF_UF_THRESHOLD: float= 0.05


#----------------------------------------------------Save Model---------------------------------------------------------------------

SAVED_MODEL_DIR=os.path.join("saved_models")
MODEL_FILE_NAME="model.pkl"






