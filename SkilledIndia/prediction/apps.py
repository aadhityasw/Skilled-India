from django.apps import AppConfig
import pickle

class PredictionConfig(AppConfig):
    name = 'prediction'
    budget_predictor = pickle.load(open('prediction/model/Budget_Predictor.pickle', 'rb'))
    duration_predictor = pickle.load(open('prediction/model/Duration_Predictor.pickle', 'rb'))
    skilled_workforce_predictor = pickle.load(open('prediction/model/Skilled_Workforce_Predictor.pickle', 'rb'))
    unskilled_workforce_predictor = pickle.load(open('prediction/model/Unskilled_Workforce_Predictor.pickle', 'rb'))