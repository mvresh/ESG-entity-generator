import numpy as np
import pandas as pd
# import main
import global_var

# enitity_ele = main.Entity()
# enitity_ele.generate_data_from_input()

class EG:
    def gen_electricity_structural_consumption(self): # //! Electricity by Floor Area

        df_EG = pd.read_excel('electricity and gas consumption by Local authority.xlsx')

        global_var.Final_dataframe = pd.read_excel('ESG-generated-data.xlsx')
        df_temp = pd.read_excel('Region_LA_buildings.xlsx')

        # print(global_var.Final_dataframe['Local Authority'].unique())

        temp_struture_array = ['Factory','Office','Shop','Warehouse','Other']
        empty_var = []
        
        # print(global_var.df_Region_LA_buildings['Local Authority'].unique())
        global_var.df_per_structure_consumption = pd.DataFrame(empty_var,columns= ['County', 'Structure', 'consumption_per_structure'])
        for i in global_var.df_Region_LA_buildings['Local Authority'].dropna().unique():
            temp_df = {}
            for j in temp_struture_array:
                temp_df['County'] = i
                temp_df['Structure'] = j
                if j == 'Factory':
                    temp_df['consumption_per_structure'] = df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item() / df_temp['Unnamed: 6'].where(df_temp['Local Authority']== i).dropna().item()
                
                elif  j == 'Office':
                    temp_df['consumption_per_structure'] = df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item() / df_temp['Unnamed: 11'].where(df_temp['Local Authority']== i).dropna().item()
                
                elif  j == 'Shop':
                    temp_df['consumption_per_structure'] = df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item() / df_temp['Unnamed: 16'].where(df_temp['Local Authority']== i).dropna().item()
                
                elif  j == 'Warehouse':
                    temp_df['consumption_per_structure'] = df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item() / df_temp['Unnamed: 21'].where(df_temp['Local Authority']== i).dropna().item()
                    
                else :
                    temp_df['consumption_per_structure'] = df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item() / df_temp['Unnamed: 26'].where(df_temp['Local Authority']== i).dropna().item()
                    
                global_var.df_per_structure_consumption = global_var.df_per_structure_consumption.append(temp_df,ignore_index=True)

        # print(global_var.df_per_structure_consumption)



        #  # Generate mean value for each structure type according to county
       
        
       
     
        

    # def percentage_dataframe(self):
    #     print()     
# EG_obj = EG()

# EG_obj.gen_electricity_structural_consumption()