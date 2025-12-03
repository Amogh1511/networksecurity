#BAsically to create a specific file to create network data model
# #this will return the model pickle processing file 
from networksecurity.constants.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import sys
import os

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class Network:
    def __init__(self,preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model= model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    #transform on any new data we are going to predict
    def predict(self,x):
        try:
            x_transform=self.preprocessor.transform(x)
            y_hat=self.model.predict(x_transform)
            return y_hat
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)







