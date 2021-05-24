import numpy as np
import pandas as pd
# import main
import global_var

# enitity_ele = main.Entity()
# enitity_ele.generate_data_from_input()

class EG:
    def gen_electricity_structural_consumption(self): # //! Electricity by Floor Area Dataframe

        temp_struture_array = ['Factory','Office','Shop','Warehouse','Other']
        empty_var = []
        
        global_var.df_per_structure_consumption = pd.DataFrame(empty_var,columns= ['County', 'Structure', 'consumption_per_structure'])
        for i in global_var.df_Region_LA_buildings['Local Authority'].dropna().unique():
            temp_df = {}
            for j in temp_struture_array:
                temp_df['County'] = i
                temp_df['Structure'] = j
                if j == 'Factory':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure

                    temp_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Office':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 11'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 11'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()             
                
                elif  j == 'Shop':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 16'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 16'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Warehouse':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 21'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 21'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()

                else :
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 26'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Electricity'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()

                global_var.df_per_structure_consumption = global_var.df_per_structure_consumption.append(temp_df,ignore_index=True)

        
        # global_var.df_per_structure_consumption.to_excel('per_structure_consumption.xlsx')

    def gen_electricity_consumption(self): # //! Electricity Consumption generator function
        x = global_var.df_per_structure_consumption['consumption_per_structure'][(global_var.df_per_structure_consumption['County'] == global_var.generated_data_row['Local Authority']) &
                                                                              (global_var.df_per_structure_consumption['Structure'] == global_var.generated_data_row['Structure_Type'])].values
                                                                   
        global_var.generated_data_row['Electricity_Consumption_By_Structure(toe)'] = np.random.normal(loc=x, scale=x*10/100, size=1).item()  * 85.984522785899 # for toe conversion
            
    # * * ----------------------------------------------------------------------- * * #
# EG_obj = EG()

# EG_obj.gen_electricity_structural_consumption()