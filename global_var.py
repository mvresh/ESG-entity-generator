# Dictionaries 
Regions_and_LA = { }

# Dataframes
df_Region_LA_buildings = ''
df_district_data = ''
df_SIC_Codes = ''
dfLA = ''
df_Region = ''
df_per_structure_consumption = ''
df_per_structure_Gas_consumption = ''
df_EG = ''
df_petrol_consumption_per_county = ''

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

prob_array_structure = {}

prob_array_county = {}

# Consumption by floor area array
consumption_array = []

# Petrol consumption predicted value array
ptrl_consumption_sector_arr = {}
NG_consumption_sector_arr = {}
coal_consumption_sector_arr = {}