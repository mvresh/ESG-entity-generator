import numpy as np
import pandas as pd
# import main
import global_var

class Gas:
    def gen_Gas_structural_consumption(self): # //! Gas by Floor Area

        temp_struture_array = ['Factory','Office','Shop','Warehouse','Other']
        empty_var = []
        
        global_var.df_per_structure_Gas_consumption = pd.DataFrame(empty_var,columns= ['County', 'Structure', 'consumption_per_structure'])
        for i in global_var.df_Region_LA_buildings['Local Authority'].dropna().unique():
            temp2_df = {}
            for j in temp_struture_array:
                temp2_df['County'] = i
                temp2_df['Structure'] = j
                if j == 'Factory':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Gas'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure

                    temp2_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Office':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 11'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Gas'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp2_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 11'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()             
                
                elif  j == 'Shop':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 16'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Gas'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp2_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 16'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()
                
                elif  j == 'Warehouse':
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 21'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Gas'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp2_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 21'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()

                else :
                    percentage_of_structure =  (global_var.df_Region_LA_buildings['Unnamed: 26'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item() 
                                                / global_var.df_Region_LA_buildings['Unnamed: 31'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item())
                    total_consumption_by_any_structure = global_var.df_EG['Gas'].where(global_var.df_EG['Local Authority'] == i).dropna().item() * percentage_of_structure
                    
                    temp2_df['consumption_per_structure'] = total_consumption_by_any_structure / global_var.df_Region_LA_buildings['Unnamed: 6'].where(global_var.df_Region_LA_buildings['Local Authority']== i).dropna().item()

                global_var.df_per_structure_Gas_consumption = global_var.df_per_structure_Gas_consumption.append(temp2_df,ignore_index=True)

    
    def gen_gas_consumption(self): # //! Gas Consumption generator function
        x = global_var.df_per_structure_Gas_consumption['consumption_per_structure'][(global_var.df_per_structure_Gas_consumption['County'] == global_var.generated_data_row['Local Authority']) &
        (global_var.df_per_structure_Gas_consumption['Structure'] == global_var.generated_data_row['Structure_Type'])].values
        global_var.generated_data_row['Gas_Consumption_By_Structure(toe)'] = np.random.normal(loc=x, scale=x*10/100, size=1).item() * 85.984522785899 # for toe conversion
            
    # * * ----------------------------------------------------------------------- * * #

# EG_obj = EG()

# EG_obj.gen_electricity_structural_consumption()