import numpy as np
import pandas as pd
# import main
import global_var
  # AR example
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA
from random import random

class Coal:
    def gen_prediction_arr_coal(self):
        print()
        coal_Fuel_df = pd.read_excel('coal_by_industry.xls')
        temp_df = coal_Fuel_df[coal_Fuel_df.columns.difference(['Section', 'Sector'])].dropna()
        
        
        for j in coal_Fuel_df['Section'].dropna():
            prediction_temp_arr = []
            temp_arr = []
            for i in temp_df:
                temp_arr.append(coal_Fuel_df[i].where(coal_Fuel_df['Section']==j).dropna().item())
            
            # fit model
            model = AutoReg(temp_arr, lags=1)
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item())

            # fit model
            model = SimpleExpSmoothing(temp_arr)
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item())

            # fit model
            # model = ARIMA(temp_arr, order=(0, 0, 1))
            # model_fit = model.fit()
            # # make prediction
            # yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            # prediction_temp_arr.append(yhat.item())
            
            global_var.coal_consumption_sector_arr[j] = prediction_temp_arr
        # print(global_var.coal_consumption_sector_arr)



Coal_obj = Coal()
