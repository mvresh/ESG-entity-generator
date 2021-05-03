import numpy as np
import pandas as pd
import main
import global_var

enitity_ele = main.Entity()
# enitity_ele.generate_data_from_input()

class EG:
    def gen_ele_gas_by_floorArea(self): # //! Electricity by Floor Area

        df_EG = pd.read_excel('electricity and gas consumption by Local authority.xlsx')
        df_electricity_by_LA = df_EG['Electricity'].where(df_EG['Local Authority'].notnull()).dropna()

        percentage_data = {
        'Factory': 
        global_var.df_Region_LA_buildings['Factories'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        'Office': 
        global_var.df_Region_LA_buildings['Offices'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        'Shop' : 
        global_var.df_Region_LA_buildings['Shops'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        'Warehouse': 
        global_var.df_Region_LA_buildings['Warehouses'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        'Other': 
        global_var.df_Region_LA_buildings['All other sectors'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values}

        df_structre_percentages = pd.DataFrame(percentage_data)
        df_structre_percentages = pd.concat([df_structre_percentages, global_var.df_Region_LA_buildings['Local Authority'].dropna()], axis=1)

         # Generate mean value for each structure type according to county
       

        # print(np.random.normal(loc=Mean_consumption_floorArea, scale=Mean_consumption_floorArea / 15, size=(100)))
       
        # global_var.Final_dataframe = global_var.Final_dataframe.sort_values(['Region', 'Local Authority'], ascending=[True, True])
        global_var.Final_dataframe = pd.read_excel('ESG-generated-data.xlsx')
        
        for j in global_var.Final_dataframe['Structure_Type'].where(global_var.Final_dataframe['Local Authority'] == 'Blaby').dropna(): 
                print(j)

        # for i in global_var.Final_dataframe['Local Authority'].unique():
            # print(i)
        #     LAcount = np.count_nonzero(global_var.Final_dataframe['Local Authority'] == i)
        #     for j in global_var.Final_dataframe['Structure_Type'].where(global_var.Final_dataframe['Local Authority'] == i).dropna(): 
        #         print(j)
        #         print(df_structre_percentages[j].where(df_structre_percentages['Local Authority'] == i).dropna().item())
        #         Mean_consumption_floorArea = (df_structre_percentages[j].where(df_structre_percentages['Local Authority'] == i).dropna().item() * 
        #         df_EG['Electricity'].where(df_EG['Local Authority'] == i).dropna().item())
        #         global_var.consumption_array.append(np.random.normal(loc=Mean_consumption_floorArea, scale=Mean_consumption_floorArea / LAcount, size=(LAcount)))


        # global_var.Final_dataframe = pd.concat([global_var.Final_dataframe, pd.DataFrame(global_var.consumption_array)], axis=1)
        # global_var.Final_dataframe.to_excel('ESG-generated-data.xlsx')
        # # Generate Normal distribution for 
        # 

    def percentage_dataframe(self):
        print()     
EG_obj = EG()

EG_obj.gen_ele_gas_by_floorArea()