import numpy as np
import pandas as pd
# import main
import global_var
  # AR example
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA
from random import random



class NG:
    def gen_prediction_arr_NG(self):
        print()
        NG_Fuel_df = pd.read_excel('Natural_Gas_by_industry.xlsx')
        temp_df = NG_Fuel_df[NG_Fuel_df.columns.difference(['Section', 'Sector'])].dropna()
        
        
        for j in NG_Fuel_df['Section'].dropna():
            prediction_temp_arr = []
            temp_arr = []
            for i in temp_df:
                temp_arr.append(NG_Fuel_df[i].where(NG_Fuel_df['Section']==j).dropna().item())
            
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
            model = ARIMA(temp_arr, order=(0, 0, 1))
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item())
            
            global_var.NG_consumption_sector_arr[j] = prediction_temp_arr
        # print(global_var.NG_consumption_sector_arr)


NG_obj = NG()