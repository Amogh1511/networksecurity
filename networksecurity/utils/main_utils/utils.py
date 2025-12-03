import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import numpy as np
import pickle
import sys
import os
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

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


def save_object(file_path: str, obj: object)-> None:
    try:
        logging.info("Entered the save object method of main utils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Exited the save object method of main utils class")
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def load_object(file_path: str) ->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open (file_path,"rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e,sys)

def load_np_arry_data(file_path:str) -> np.array:
    #Load np array data from file
    # File_path: str loaction of the file to load
    #returns np.arry data loaded
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report ={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]

            gridsearch=GridSearchCV(model,para,cv=3)
            gridsearch.fit(X_train,y_train)

            model.set_params(**gridsearch.best_params_)
            model.fit(X_train,y_train)

            #train Model
            #model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            print("Model:", list(models.keys())[i])
            print("Pred shape:", y_test_pred.shape)

            #train model score
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report



    except Exception as e:
        raise NetworkSecurityException(e,sys)





