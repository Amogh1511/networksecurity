#dataclass acts like a decorator for class constructor
from dataclasses import dataclass

@dataclass
#data class skips the construction part and makes easy to construct easy way 
#Skips __init__ part and build directly and works as a decorator 
class DataIngestionArtifact:
    trained_file_path:str
    tested_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str