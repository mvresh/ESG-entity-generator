import numpy as np
import pandas as pd
# import main
import global_var

class Region_County:
    
    def dictionary_Region_LA(self,df_Region,dfLA): # //! Region and County Dictionary Creation
        for Region_row in df_Region:
            global_var.Regions_and_LA[Region_row] = []

        for Region_index in range(len(df_Region.index)+1):
            
            if (Region_index+1 <= len(df_Region.index)):
                # print("START loc :", df_Region.index[Region_index])
                # print("END loc :" ,df_Region.index[Region_index+1])
                if (Region_index+1 != len(df_Region.index)):
                    df_dict = dfLA.loc[df_Region.index[Region_index]:df_Region.index[Region_index+1]]
                    for row in df_dict:
                        if global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] == '':
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] = row
                        else:
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]].append(row)
                else:
                    df_dict = dfLA.loc[df_Region.index[Region_index]:global_var.df_Region_LA_buildings.index[-1]]
                    for row in df_dict:
                        if global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] == '':
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] = row
                        else:
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]].append(row)
    
    # * * ----------------------------------------------------------------------- * * #

    def gen_Region_LA_GeoCode(self): # //! Region, Local Authority and Geographic Code

        Final_Region = np.random.choice(list(global_var.Regions_and_LA.keys()), p=global_var.prob_array_region)
        # print('Company Region : ' ,Final_Region)
        # Append Final_Region to Data Row
        global_var.generated_data_row['Region'] = Final_Region

        Final_County = np.random.choice(global_var.Regions_and_LA[Final_Region])
        # print('Company LA / County : ',Final_County)
        # Append Final_Region to Data Row
        global_var.generated_data_row['Local Authority'] = Final_County

        Final_GeoCode = global_var.df_district_data['Code'].where(global_var.df_district_data['County']==Final_County).dropna().item()
        # print('Company Geographic Code : ',Final_GeoCode)
        # Append Final_Region to Data Row
        global_var.generated_data_row['Geographic Code'] = Final_GeoCode
  
    # * * ----------------------------------------------------------------------- * * #
