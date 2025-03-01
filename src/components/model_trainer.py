import os 
import sys 
from dataclasses import dataclass 
from catboost import CatBoostRegressor 
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score 
from sklearn.tree import DecisionTreeRegressor
from src.exception import CustomException 
from src.logger import logging
from sklearn.neighbors import KNeighborsRegressor
from src.utils import save_object, eval_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def inititate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, Y_train, X_test, Y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "K-Neighbours Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Cat Boost Regressor": CatBoostRegressor(),
                "Ada Boost Regressor": AdaBoostRegressor()
            }
        
            model_report:dict = eval_model(X_train= X_train, Y_train = Y_train, X_test = X_test, Y_test = Y_test, models = models)


            best_Score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_Score)
            ]

            best_model = models[best_model_name]

            if best_Score < 0.6:
                raise CustomException("No best model Found")
            else:
                logging.info("Best model found")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2_sq = r2_score(Y_test, predicted)

            return r2_sq

        except Exception as e:
            raise CustomException(e, sys)