from numpy import random
from numpy.core.arrayprint import StructuredVoidFormat
from numpy.testing._private.nosetester import run_module_suite
import global_var
import pandas as pd
import numpy as np
import os
import shortuuid
# ? Library for GUI
from appJar import gui
# ? For Progressbar
from tqdm.auto import tqdm
import time

class Entity:
    def __init__(self):
        self.initial_data_loading()

    # Function to load all the dataset files
    def initial_data_loading(self):  
        print('initial data loading...')
        global_var.df_Region_LA_buildings = pd.read_excel('Region_LA_buildings.xlsx')
        global_var.dfLA = global_var.df_Region_LA_buildings['Local Authority'].dropna()
        global_var.df_Region = global_var.df_Region_LA_buildings['Region'].dropna()
        global_var.df_district_data = pd.read_excel('ONSData6DistrictLevel.xlsx')
        global_var.df_SIC_Codes = pd.read_csv('SIC07_CH_condensed_list_en.csv')
        self.dictionary_Region_LA(global_var.df_Region,global_var.dfLA)
        self.probability_array_all()

        empty_var = []
        global_var.Final_dataframe = pd.DataFrame(empty_var, columns = ['Unique ID', 'Region','Local Authority','Geographic Code','Sector','SIC Code','Description'])
        print('initial data loaded successfully.')
    
    # * * ----------------------------------------------------------------------- * * #

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

    def probability_array_all(self): # //! Probabiltiy Dictionary Creation
        region = global_var.df_Region_LA_buildings['Region'].dropna().values
        for i in region:
            Total_numberofbuildings = global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 31'].item()
            per_structure_count = [global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 6'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 11'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 16'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 21'].item(),
                                    global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == i]['Unnamed: 26'].item()]

            # print(global_var.df_Region_LA_buildings[global_var.df_Region_LA_buildings['Region'] == 'North East'][['Unnamed: 6','Unnamed: 11','Unnamed: 16','Unnamed: 21','Unnamed: 26','Unnamed: 31']])
            global_var.prob_array_structure[i] =  [float(per_structure_count[0]/Total_numberofbuildings), 
                            float(per_structure_count[1]/Total_numberofbuildings), 
                            float(per_structure_count[2]/Total_numberofbuildings),
                            float(per_structure_count[3]/Total_numberofbuildings),
                            float(per_structure_count[4]/Total_numberofbuildings)]

    # * * ----------------------------------------------------------------------- * * #

    def generate_data_from_input(self): # //! MAiN Generator Function
        # create a GUI variable called app
        app = gui()
        app.addLabelEntry("Enter Number of Records Required")
        def press(button):
            val = app.getEntry("Enter Number of Records Required")
            app.stop()           
            for i in tqdm(range(int(val))):
                Entity_Obj.gen_Unique_Identity()
                Entity_Obj.gen_Region_LA_GeoCode()
                Entity_Obj.gen_SIC_Sector_Description(global_var.df_district_data,global_var.df_SIC_Codes)
                Entity_Obj.gen_structure()
                # Create the pandas DataFrame
                global_var.Final_dataframe = global_var.Final_dataframe.append(global_var.generated_data_row, ignore_index=True)
            
                #Writing Dataframe into Excel file
                global_var.Final_dataframe.to_excel('ESG-generated-data.xlsx')
                print("",end = '\r')

            # for i in range(int(val)):

            #     print('Number of Records Generated : ',i,'\n')
            #     Entity_Obj.gen_Unique_Identity()
            #     Entity_Obj.gen_Region_LA_GeoCode()
            #     Entity_Obj.gen_SIC_Sector_Description(global_var.df_district_data,global_var.df_SIC_Codes)
            #     Entity_Obj.gen_structure()
            #     # Create the pandas DataFrame
            #     global_var.Final_dataframe = global_var.Final_dataframe.append(global_var.generated_data_row, ignore_index=True)
            
            # #Writing Dataframe into Excel file
            # print('Writing to Excel')
            # global_var.Final_dataframe.to_excel('ESG-generated-data.xlsx')
            
        app.addButtons(["Submit"], press)
        app.go()
    
    # * * ----------------------------------------------------------------------- * * #

    def gen_Unique_Identity(self): # //! Unique ID
        UUID = shortuuid.ShortUUID().random(length=16)
        # print('Unique ID : ',UUID)
        global_var.generated_data_row['Unique ID'] = UUID
    
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

    def gen_SIC_Sector_Description(self,df_district_data,df_SIC_Codes): # //! SIC Code, Sector and Description
        

        row = df_district_data[df_district_data['County'] == global_var.generated_data_row['Local Authority']]
        
                #init probability array
        probabilityArraySIC = [float(row[row.keys()[10]]/row['Total']), 
                            float(row[row.keys()[11]]/row['Total']), 
                            float(row[row.keys()[12]]/row['Total']), 
                            float(row[row.keys()[13]]/row['Total']), 
                            float(row[row.keys()[14]]/row['Total']), 
                            float(row[row.keys()[15]]/row['Total']), 
                            float(row[row.keys()[16]]/row['Total']), 
                            float(row[row.keys()[17]]/row['Total']), 
                            float(row[row.keys()[18]]/row['Total']), 
                            float(row[row.keys()[19]]/row['Total']), 
                            float(row[row.keys()[20]]/row['Total']), 
                            float(row[row.keys()[21]]/row['Total']), 
                            float(row[row.keys()[22]]/row['Total']), 
                            float(row[row.keys()[23]]/row['Total']), 
                            float(row[row.keys()[24]]/row['Total']), 
                            float(row[row.keys()[25]]/row['Total']), 
                            float(row[row.keys()[26]]/row['Total'])]

        #init sic list
        listOfSICS = list(row.keys()[10:27])

        #SIC selected according to row input (row was selected by location)
        sic_range = np.random.choice(listOfSICS, p=probabilityArraySIC)
        # Company Sector
        Final_Sector = sic_range.split(':')[1]
        # print('Company Sector : ',Final_Sector)
        global_var.generated_data_row['Sector'] = Final_Sector
        
        if '-' in sic_range.split(':')[0]:
        # creating an array of sic code to search into sic code list
            sic_range = list(range(
                int(sic_range.split(':')[0].split('-')[0]),
                int(sic_range.split(':')[0].split('-')[1])
                ))
        else:
            sic_range = [int(sic_range.split(':')[0])]
        

        sic_range = [element * 1000 for element in sic_range]
        if len(sic_range) > 1:
            sampled_sicCodes = df_SIC_Codes[df_SIC_Codes['SIC Code'].between(sic_range[0],sic_range[len(sic_range)-1]+999)]
        else:
            sampled_sicCodes = df_SIC_Codes[df_SIC_Codes['SIC Code'].between(sic_range[0],sic_range[0]+999)]

        Final_sic_code = sampled_sicCodes.sample()
        
        # Company Sic code And description
        # print('Company SIC Code : ',Final_sic_code['SIC Code'].values)
        global_var.generated_data_row['SIC Code'] = Final_sic_code['SIC Code'].item()

        # print('Company Description : ',Final_sic_code['Description'].values)
        global_var.generated_data_row['Description'] =  Final_sic_code['Description'].item()
    
    # * * ----------------------------------------------------------------------- * * #
    
    def gen_structure(self): # //! Struture Type
        Final_Structure = np.random.choice(['Factory','Office','Shop','Warehouse','Other'], p=global_var.prob_array_structure[global_var.generated_data_row['Region'].item()])
        # Append Final_Structure to Data Row
        global_var.generated_data_row['Structure_Type'] = Final_Structure 

    # * * ----------------------------------------------------------------------- * * #
  
# Creating Class object for Entity ... Init will be called
Entity_Obj = Entity()

# Calling Data generate funtion from class object
Entity_Obj.generate_data_from_input()





