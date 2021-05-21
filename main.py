from numpy import random
from numpy.core.arrayprint import StructuredVoidFormat, printoptions
from numpy.testing._private.nosetester import run_module_suite

import pandas as pd
import numpy as np

import Region_County
import structure
import SIC
import global_var
import petrol
import natural_gas
import coal
import electricity
import gas

import os
import shortuuid
# ? Library for GUI
from appJar import gui
# ? For Progressbar
from tqdm.auto import tqdm
import time
import matplotlib.pyplot as plt

Region_County_obj = Region_County.Region_County()
ptrl_obj = petrol.Petrol()
NG_obj = natural_gas.NG()
coal_obj = coal.Coal()
ele_obj = electricity.EG()
gas_obj = gas.Gas()
structure_obj = structure.Strucutre()
SIC_obj = SIC.SIC()

class Entity:
    def __init__(self):
        self.initial_data_loading()

    # Function to load all the dataset files
    def initial_data_loading(self):  
        print('initial data loading...')
        global_var.df_Region_LA_buildings = pd.read_excel('source_files\\Region_LA_buildings.xlsx')
        global_var.dfLA = global_var.df_Region_LA_buildings['Local Authority'].dropna()
        global_var.df_Region = global_var.df_Region_LA_buildings['Region'].dropna()
        global_var.df_district_data = pd.read_excel('source_files\\ONSData6DistrictLevel.xlsx')
        global_var.df_SIC_Codes = pd.read_csv('source_files\\SIC07_CH_condensed_list_en.csv')
        global_var.df_EG = pd.read_excel('source_files\\electricity and gas consumption by Local authority.xlsx')

        Region_County_obj.dictionary_Region_LA(global_var.df_Region,global_var.dfLA)
        ptrl_obj.gen_prediction_arr_petrol()
        NG_obj.gen_prediction_arr_NG()
        coal_obj.gen_prediction_arr_coal()
        ele_obj.gen_electricity_structural_consumption()
        gas_obj.gen_Gas_structural_consumption()
        structure_obj.probability_array_structure()

        empty_var = []
        global_var.Final_dataframe = pd.DataFrame(empty_var, columns = ['Unique ID',
        'Region',
        'Local Authority',
        'Geographic Code',
        'Section',
        'SIC Group',
        'Sector',
        'Structure_Type',
        'Petrol_Consumption_By_Sector(toe)',
        'NG_Consumption_By_Sector(toe)',
        'Coal_Consumption_By_Sector(toe)',
        'Electricity_Consumption_By_Structure',
        'Gas_Consumption_By_Structure'])

        print('Initial data loaded successfully.')
    
    # * * ----------------------------------------------------------------------- * * #

    def generate_data_from_input(self): # //! MAiN Generator Function
        # create a GUI variable called app
        app = gui()
        app.addLabelEntry("Enter Number of Records Required")
        def press(button):
            val = app.getEntry("Enter Number of Records Required")
            app.stop()           
            for i in tqdm(range(int(val))):
                self.gen_Unique_Identity()
                Region_County_obj.gen_Region_LA_GeoCode() #  //! Generate Region and County(Local Authority)
                SIC_obj.gen_SIC_Sector_Description(global_var.df_district_data,global_var.df_SIC_Codes)
                structure_obj.gen_structure() 
                
                ptrl_obj.gen_petrol_consumption()
                NG_obj.gen_NG_consumption()
                coal_obj.gen_coal_consumption()
                
                ele_obj.gen_electricity_consumption()
                gas_obj.gen_gas_consumption()
                
                # Create the pandas DataFrame
                global_var.Final_dataframe = global_var.Final_dataframe.append(global_var.generated_data_row, ignore_index=True)
            
                print("",end = '\r')

            #Writing Dataframe into Excel file
            global_var.Final_dataframe.to_excel('Generated_data\ESG-generated-data.xlsx')
            
           
        app.addButtons(["Submit"], press)
        app.go()
    
    # * * ----------------------------------------------------------------------- * * #

    def gen_Unique_Identity(self): # //! Unique ID
        UUID = shortuuid.ShortUUID().random(length=16)
        # print('Unique ID : ',UUID)
        global_var.generated_data_row['Unique ID'] = UUID
    
    # * * ----------------------------------------------------------------------- * * #

# Creating Class object for Entity ... Init will be called
Entity_Obj = Entity()

# Calling Data generate funtion from class object
Entity_Obj.generate_data_from_input()







