import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import numpy as np
import dill
import pickle
import sys
import os


#read yaml file
#return in dict form -> because we are reading in schema
# Because it was already in key-value pairs
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as ex:
        raise NetworkSecurityException(ex,sys)
    

def write_yaml_file(file_path: str, data:object, replace= True) -> None:
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(data,file)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    




