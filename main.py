from numpy import random
from numpy.core.arrayprint import StructuredVoidFormat
from numpy.testing._private.nosetester import run_module_suite
import config
import pandas as pd
import numpy as np
import os
import shortuuid

def INITCALL():
    df_Region_LA_buildings = pd.read_excel('Region_LA_buildings.xlsx')
    df_district_data = pd.read_excel('ONSData6DistrictLevel.xlsx')
    df_SIC_Codes = pd.read_csv('SIC07_CH_condensed_list_en.csv')
    
    dfLA = df_Region_LA_buildings['Local Authority'].dropna()
    df_Region = df_Region_LA_buildings['Region'].dropna()
    # dict_gen_Region_LA(df_Region,dfLA)


def gen_Unique_Identity():
    print('Unique ID : ',shortuuid.ShortUUID().random(length=10))

def gen_Region_LA(df_Region,dfLA):
    
    for Region_row in df_Region:
        config.Regions_and_LA[Region_row] = []
    
    for Region_index in range(len(df_Region.index)):
        if (Region_index+1 < len(df_Region.index)):
            # print("START loc :", df_Region.index[Region_index])
            # print("END loc :" ,df_Region.index[Region_index+1])
            df_dict = dfLA.loc[df_Region.index[Region_index]:df_Region.index[Region_index+1]]
            for row in df_dict:
                if config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]] == '':
                    config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]] = row
                else:
                    config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]].append(row)

def gen_SIC_Sector_Description():
    df_district_data = pd.read_excel('ONSData6DistrictLevel.xlsx')
    df_SIC_Codes = pd.read_csv('SIC07_CH_condensed_list_en.csv')


    row = df_district_data[df_district_data['County'] == 'County Durham']
    
    #init probability array
    probabilityArray = [float(row[row.keys()[10]]/row['Total']), 
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
    sic_range = np.random.choice(listOfSICS, p=probabilityArray)

    # Company Sector
    print('Company Sector : ',sic_range.split(':')[1])

    # creating an array of sic code to search into sic code list
    sic_range = list(range(
        int(sic_range.split(':')[0].split('-')[0]),
        int(sic_range.split(':')[0].split('-')[1])
        ))
    print(sic_range)
    sic_range = [element * 1000 for element in sic_range]
  
    sampled_sicCodes = df_SIC_Codes[df_SIC_Codes['SIC Code'].between(sic_range[0],sic_range[len(sic_range)-1]+999)]
    
    Final_sic_code = sampled_sicCodes.sample()
    
    # Company Sic code And description
    print('Company Final_sic_code : ',Final_sic_code['SIC Code'].values)
    print('Company Description : ',Final_sic_code['Description'].values)

gen_SIC_Sector_Description()
