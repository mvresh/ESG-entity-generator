import numpy as np
import pandas as pd
# import main
import global_var
  # AR example
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA
from random import random

# enitity_ele = main.Entity()

class Petrol:
    def gen_petrol_consumption(self):
        
        global_var.Final_dataframe = pd.read_excel('ESG-generated-data.xlsx')

        for i in global_var.Final_dataframe['Section']:
            print()



    def gen_prediction_arr_petrol(self):
        Fuel_df = pd.read_excel('fuel_by _industry.xls')

        temp_df = Fuel_df[Fuel_df.columns.difference(['Section', 'Sector'])].dropna()
        
        
        for j in Fuel_df['Section'].dropna():
            prediction_temp_arr = []
            temp_arr = []
            for i in temp_df:
                temp_arr.append(Fuel_df[i].where(Fuel_df['Section']==j).dropna().item())
            
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
            
            global_var.ptrl_consumption_sector_arr[j] = prediction_temp_arr
            # print(np.random.choice(global_var.ptrl_consumption_sector_arr[j]))
        print(global_var.ptrl_consumption_sector_arr)



petrol_obj = Petrol()

petrol_obj.gen_petrol_consumption()