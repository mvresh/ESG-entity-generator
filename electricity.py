import numpy as np
import pandas as pd
# import main
import global_var

# enitity_ele = main.Entity()
# enitity_ele.generate_data_from_input()

class EG:
    def gen_electricity_structural_consumption(self): # //! Electricity by Floor Area

        temp_struture_array = ['Factory','Office','Shop','Warehouse','Other']
        empty_var = []
        
        global_var.df_per_structure_consumption = pd.DataFrame(empty_var,columns= ['County', 'Structure', 'consumption_per_structure'])
        for i in global_var.df_Region_LA_buildings['Local Authority'].dropna().unique():
            temp_df = {}
            for j in temp_struture_array:
                temp_df['County'] = i
                temp_df['Structure'] = j
                if j == 'Factory':
                    temp_df['consumption_per_structure'] = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() / global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Office':
                    temp_df['consumption_per_structure'] = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() / global_var.df_Region_LA_buildings['Unnamed: 11'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Shop':
                    temp_df['consumption_per_structure'] = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() / global_var.df_Region_LA_buildings['Unnamed: 16'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Warehouse':
                    temp_df['consumption_per_structure'] = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() / global_var.df_Region_LA_buildings['Unnamed: 21'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                    
                else :
                    temp_df['consumption_per_structure'] = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() / global_var.df_Region_LA_buildings['Unnamed: 26'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                    
                global_var.df_per_structure_consumption = global_var.df_per_structure_consumption.append(temp_df,ignore_index=True)



# EG_obj = EG()

# EG_obj.gen_electricity_structural_consumption()