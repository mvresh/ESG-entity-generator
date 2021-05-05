import numpy as np
import pandas as pd
# import main
import global_var

class SIC:
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

        # Company Sic Group
        Final_SicGroup = sic_range.split(':')[0]
        global_var.generated_data_row['SIC Group'] = Final_SicGroup
        
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
        # TODO: global_var.generated_data_row['SIC Code'] = Final_sic_code['SIC Code'].item()

        # print('Company Section : ',Final_sic_code['Section'].values)
        global_var.generated_data_row['Section'] =  Final_sic_code['Section'].item()

        # print('Company Description : ',Final_sic_code['Description'].values)
         # TODO: global_var.generated_data_row['Description'] =  Final_sic_code['Description'].item()
    
    # * * ----------------------------------------------------------------------- * * #
    

              