import os
import sys 
import numpy as np
import pandas as pd 
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    

def eval_model(X_train, Y_train, X_test,Y_test, models):
    try :
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, Y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            model_train_r2 = r2_score(Y_train, y_train_pred)
            model_test_r2 = r2_score(Y_test, y_test_pred)

            report[list(models.keys())[i]] = model_test_r2

            return report
    except Exception as e:
        raise CustomException(e, sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)

