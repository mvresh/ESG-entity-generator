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
        coal_Fuel_df = pd.read_excel('source_files\coal_by_industry.xls')
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
            prediction_temp_arr.append(yhat.item()*1000000)

            # fit model
            model = SimpleExpSmoothing(temp_arr)
            model_fit = model.fit()
            # make prediction
            yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            prediction_temp_arr.append(yhat.item()*1000000)

            # fit model
            # model = ARIMA(temp_arr, order=(0, 0, 1))
            # model_fit = model.fit()
            # # make prediction
            # yhat = model_fit.predict(len(temp_arr), len(temp_arr))
            # prediction_temp_arr.append(yhat.item())
            
            global_var.coal_consumption_sector_arr[j] = prediction_temp_arr
        # print(global_var.coal_consumption_sector_arr)

    def gen_coal_consumption(self): # //! Coal
        generated_LA = global_var.generated_data_row['Local Authority']
        x = global_var.coal_consumption_sector_arr[global_var.generated_data_row['Section']]
        x = np.random.choice(x)
        # print(x)
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
            global_var.generated_data_row['Coal_Consumption_By_Sector(toe)'] = 0
        else:
            y = np.random.normal(loc=per_structure_consumption,scale=per_structure_consumption*10/100,size=1)
            global_var.generated_data_row['Coal_Consumption_By_Sector(toe)'] = y.item()

    # * * ----------------------------------------------------------------------- * * #



Coal_obj = Coal()
