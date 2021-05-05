import numpy as np
import pandas as pd
# import main
import global_var

class Strucutre:
    def gen_structure(self): # //! Struture Type
        Final_Structure = np.random.choice(['Factory','Office','Shop','Warehouse','Other'], p=global_var.prob_array_structure[global_var.generated_data_row['Local Authority'].item()])
        # Append Final_Structure to Data Row
        global_var.generated_data_row['Structure_Type'] = Final_Structure 

    # * * ----------------------------------------------------------------------- * * #
    

    def probability_array_structure(self): # //! structure type Probabiltiy Dictionary Creation 
        Local_Authority = global_var.df_Region_LA_buildings['Local Authority'].dropna().values
        for i in Local_Authority:
            Total_numberofbuildings = global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 31'].item()
            per_structure_count = [global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 6'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 11'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 16'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 21'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Local Authority'] == i]['Unnamed: 26'].item()]
            # print(global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == 'North East'][['Unnamed: 6','Unnamed: 11','Unnamed: 16','Unnamed: 21','Unnamed: 26','Unnamed: 31']])
            global_var.prob_array_structure[i] =  [float(per_structure_count[0]/Total_numberofbuildings), 
                            float(per_structure_count[1]/Total_numberofbuildings), 
                            float(per_structure_count[2]/Total_numberofbuildings),
                            float(per_structure_count[3]/Total_numberofbuildings),
                            float(per_structure_count[4]/Total_numberofbuildings)]
        # df = pd.DataFrame(data= global_var.prob_array_structure)
        # df.to_excel('probability_array_structure.xlsx')
    
    # * * ----------------------------------------------------------------------- * * #

  