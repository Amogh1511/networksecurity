#dataclass acts like a decorator for class constructor
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    tested_file_path: str

