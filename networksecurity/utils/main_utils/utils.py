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
    

def save_np_array_data(file_path: str, array: np.array):
    #Save np array data to file
    #file_path - loaction of the file to save
    #array - save data in form of np.array
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, "wb") as file:
            np.save(file,array)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
#save pickle file
def save_pickle_object(file_path: str, obj:object) -> None:
    try:
        logging.info("Entered the save pickle object of utils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file:
            pickle.dump(obj,file)
        logging.info("Exited the save pickle object method")    
    except Exception as ex:
        raise NetworkSecurityException(ex,sys)


