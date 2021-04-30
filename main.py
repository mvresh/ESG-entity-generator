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
        empty_var = []
        global_var.Final_dataframe = pd.DataFrame(empty_var, columns = ['Unique ID', 'Region','Local Authority','Geographic Code','Sector','SIC Code','Description'])
        print('initial data loaded successfully.')
    
    # * * ----------------------------------------------------------------------- * * #

    # Function to generate Dictionary for Region and Local authority   
    def dictionary_Region_LA(self,df_Region,dfLA): # //! Dictionary
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
                    df_dict = dfLA.loc[df_Region.index[Region_index]:368]
                    for row in df_dict:
                        if global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] == '':
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]] = row
                        else:
                            global_var.Regions_and_LA[list(global_var.Regions_and_LA)[Region_index]].append(row)
    
    # * * ----------------------------------------------------------------------- * * #

    # Function to generate data from the GUI user input
    def generate_data_from_input(self): # //! MAiN Function
        # create a GUI variable called app
        app = gui()
        app.addLabelEntry("Enter Number of Records Required")
        def press(button):
            val = app.getEntry("Enter Number of Records Required")
            app.stop()
            for i in range(int(val)):
                print(i,'-Records Generated')
                Entity_Obj.gen_Unique_Identity()
                Entity_Obj.gen_Region_LA_GeoCode()
                Entity_Obj.gen_SIC_Sector_Description(global_var.df_district_data,global_var.df_SIC_Codes)
                # Create the pandas DataFrame
                global_var.Final_dataframe = global_var.Final_dataframe.append(global_var.generated_data_row, ignore_index=True)
            
            #Writing Dataframe into Excel file
            print('Writing to Excel')
            global_var.Final_dataframe.to_excel('ESG-generated-data.xlsx')
            
        app.addButtons(["Submit"], press)
        app.go()
    
    # * * ----------------------------------------------------------------------- * * #

    # Function to generate Unique ID-16 digit hex Number   
    def gen_Unique_Identity(self):
        UUID = shortuuid.ShortUUID().random(length=16)
        # print('Unique ID : ',UUID)
        global_var.generated_data_row['Unique ID'] = UUID
    
    # * * ----------------------------------------------------------------------- * * #

    # Function to generate Region, Local Authority and Geographic code
    def gen_Region_LA_GeoCode(self):

        
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

    # Function to generate SIC code, Company Sector and Description
    def gen_SIC_Sector_Description(self,df_district_data,df_SIC_Codes):
        

        row = df_district_data[df_district_data['County'] == 'County Durham']
        
    

        #init sic list
        listOfSICS = list(row.keys()[10:27])

        #SIC selected according to row input (row was selected by location)
        sic_range = np.random.choice(listOfSICS, p=global_var.probabilityArraySIC)
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

    # Function to generate Structure type
    def gen_structure(self):
        print('Structure Generating')

# Creating Class object for Entity ... Init will be called
Entity_Obj = Entity()

# # Calling Data generate funtion from class object
# Entity_Obj.generate_data_from_input()


# Function to generate Structure type
def gen_structure():
    print('Structure Generating')

gen_structure()