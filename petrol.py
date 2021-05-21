import numpy as np
import pandas as pd
# import main
import global_var
  # AR example
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA
from random import random

# Entity_Obj = main.Entity()

class Petrol:
    
    def gen_prediction_arr_petrol(self):
        Fuel_df = pd.read_excel('source_files\Petrol_by _industry.xls')
        temp_df = Fuel_df[Fuel_df.columns.difference(['Section', 'Sector'])].dropna()
        
        for j in Fuel_df['Section'].dropna():
            prediction_temp_arr = []
            temp_arr = []
            for i in temp_df:
                temp_arr.append(Fuel_df[i].where(Fuel_df['Section']==j).dropna().item())
            
            # ? AutoRegression
            # fit model
            model = AutoReg(temp_arr, lags=1)
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item()*1000000)

            # ? Exponential Smoothing
            # fit model
            model = SimpleExpSmoothing(temp_arr)
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item()*1000000)

            # ? Auto regression with moving average
            # fit model
            model = ARIMA(temp_arr, order=(0, 0, 1))
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item()*1000000)
            
            global_var.ptrl_consumption_sector_arr[j] = prediction_temp_arr
        # print(global_var.ptrl_consumption_sector_arr)


    def gen_petrol_consumption(self): # //! Petrol Consumption generator function
        generated_LA = global_var.generated_data_row['Local Authority']
        
        x = global_var.ptrl_consumption_sector_arr[global_var.generated_data_row['Section']]
        x = np.random.choice(x)
        y = ''
        if global_var.generated_data_row['Structure_Type'] == 'Factory':
            county_consumption = x *  global_var.df_Region_LA_buildings['Unnamed: 30'].where(global_var.df_Region_LA_buildings['Local Authority']== generated_LA).dropna().item()
            overall_structure_consumption = county_consumption *  global_var.prob_array_structure[generated_LA.item()][0]
            per_structure_consumption = overall_structure_consumption / global_var.df_Region_LA_buildings['Unnamed: 6'].where(
                global_var.df_Region_LA_buildings['Local Authority'] == generated_LA).dropna().item()

        elif  global_var.generated_data_row['Structure_Type'] == 'Office':
            county_consumption = x *  global_var.df_Region_LA_buildings['Unnamed: 30'].where(global_var.df_Region_LA_buildings['Local Authority']== generated_LA).dropna().item()
            overall_structure_consumption = county_consumption *  global_var.prob_array_structure[generated_LA.item()][1]
            per_structure_consumption = overall_structure_consumption / global_var.df_Region_LA_buildings['Unnamed: 11'].where(
                global_var.df_Region_LA_buildings['Local Authority'] == generated_LA).dropna().item()

        elif  global_var.generated_data_row['Structure_Type'] == 'Shop':
            county_consumption = x *  global_var.df_Region_LA_buildings['Unnamed: 30'].where(global_var.df_Region_LA_buildings['Local Authority']== generated_LA).dropna().item()
            overall_structure_consumption = county_consumption *  global_var.prob_array_structure[generated_LA.item()][2]
            per_structure_consumption = overall_structure_consumption / global_var.df_Region_LA_buildings['Unnamed: 16'].where(
                global_var.df_Region_LA_buildings['Local Authority'] == generated_LA).dropna().item()

        elif  global_var.generated_data_row['Structure_Type'] == 'Warehouse':
            county_consumption = x *  global_var.df_Region_LA_buildings['Unnamed: 30'].where(global_var.df_Region_LA_buildings['Local Authority']== generated_LA).dropna().item()
            overall_structure_consumption = county_consumption *  global_var.prob_array_structure[generated_LA.item()][3]
            per_structure_consumption = overall_structure_consumption / global_var.df_Region_LA_buildings['Unnamed: 21'].where(
                global_var.df_Region_LA_buildings['Local Authority'] == generated_LA).dropna().item()
        else :
            county_consumption = x *  global_var.df_Region_LA_buildings['Unnamed: 30'].where(global_var.df_Region_LA_buildings['Local Authority']== generated_LA).dropna().item()
            overall_structure_consumption = county_consumption *  global_var.prob_array_structure[generated_LA.item()][4]
            per_structure_consumption = overall_structure_consumption / global_var.df_Region_LA_buildings['Unnamed: 26'].where(
                global_var.df_Region_LA_buildings['Local Authority'] == generated_LA).dropna().item()
            
        # print(np.random.normal(loc=per_structure_consumption,scale=per_structure_consumption*10/100,size=1))
        if per_structure_consumption < 0:
                global_var.generated_data_row['Petrol_Consumption_By_Sector(toe)'] = 0
        else:
            y = np.random.normal(loc=per_structure_consumption,scale=per_structure_consumption*10/100,size=1)
            global_var.generated_data_row['Petrol_Consumption_By_Sector(toe)'] = y.item()
    
    # * * ----------------------------------------------------------------------- * * #

# petrol_obj = Petrol()
# petrol_obj.gen_petrol_consumption()
