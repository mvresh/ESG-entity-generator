from numpy import random
from numpy.core.arrayprint import StructuredVoidFormat
from numpy.testing._private.nosetester import run_module_suite
import config
import pandas as pd
import numpy as np
import os
import shortuuid

def INITCALL():
    config.df_Region_LA_buildings = pd.read_excel('Region_LA_buildings.xlsx')
    config.dfLA = config.df_Region_LA_buildings['Local Authority'].dropna()
    config.df_Region = config.df_Region_LA_buildings['Region'].dropna()
    config.df_district_data = pd.read_excel('ONSData6DistrictLevel.xlsx')
    config.df_SIC_Codes = pd.read_csv('SIC07_CH_condensed_list_en.csv')
    

def gen_Unique_Identity():
    print('Unique ID : ',shortuuid.ShortUUID().random(length=16))

def gen_Region_LA_GeoCode(df_Region,dfLA):

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

    # random choice probability array
    prob_array_region = [
                        float(57413/1362789), 
                        float(177575/1362789), 
                        float(139401/1362789),
                        float(109150/1362789),
                        float(132905/1362789), 
                        float(134827/1362789),
                        float(203453/1362789),
                        float(193711/1362789), 
                        float(135657/1362789),
                        float(78697/1362789)
                        ]
    Final_Region = np.random.choice(list(config.Regions_and_LA.keys()), p=prob_array_region)
    print('Company Region : ' ,Final_Region)
    Final_County = np.random.choice(config.Regions_and_LA[Final_Region])
    print('Company LA / County : ',Final_County)
    Final_GeoCode = config.df_district_data['Code'].where(config.df_district_data['County']==Final_County).dropna().values
    print('Company Geographic Code : ',Final_GeoCode)

def gen_SIC_Sector_Description(df_district_data,df_SIC_Codes):
    

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
    # print(sic_range)
    sic_range = [element * 1000 for element in sic_range]
  
    sampled_sicCodes = df_SIC_Codes[df_SIC_Codes['SIC Code'].between(sic_range[0],sic_range[len(sic_range)-1]+999)]
    
    Final_sic_code = sampled_sicCodes.sample()
    
    # Company Sic code And description
    print('Company SIC Code : ',Final_sic_code['SIC Code'].values)
    print('Company Description : ',Final_sic_code['Description'].values)


gen_Unique_Identity()
INITCALL()
gen_Region_LA_GeoCode(config.df_Region,config.dfLA)
gen_SIC_Sector_Description(config.df_district_data,config.df_SIC_Codes)