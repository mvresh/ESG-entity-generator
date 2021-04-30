# Dictionaries 
Regions_and_LA = { }

# Dataframes
df_Region_LA_buildings = ''
df_district_data = ''
df_SIC_Codes = ''
dfLA = ''
df_Region = ''

# Generated Data Row
generated_data_row = {}

# Final DataFrame
Final_dataframe = ''

# Probability Arrays
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