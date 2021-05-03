Execute 'pip install shortuuid'
Execute 'pip install appJar'
Execute 'python main.py'
// Then //
Enter Number of Records required.












['Region' 'Local Authority' 'Geographic Code' 'Unnamed: 3' 'Factories'
 'Unnamed: 5' 'Unnamed: 6' 'Unnamed: 7' 'Unnamed: 8' 'Offices'
 'Unnamed: 10' 'Unnamed: 11' 'Unnamed: 12' 'Unnamed: 13' 'Shops'
 'Unnamed: 15' 'Unnamed: 16' 'Unnamed: 17' 'Unnamed: 18' 'Warehouses'
 'Unnamed: 20' 'Unnamed: 21' 'Unnamed: 22' 'Unnamed: 23'
 'All other sectors' 'Unnamed: 25' 'Unnamed: 26' 'Unnamed: 27'
 'Unnamed: 28' 'Total' 'Unnamed: 30' 'Unnamed: 31' 'Unnamed: 32']


   # percentage_data = {
        # 'Factory': 
        # global_var.df_Region_LA_buildings['Factories'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        # global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        # 'Office': 
        # global_var.df_Region_LA_buildings['Offices'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        # global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        # 'Shop' : 
        # global_var.df_Region_LA_buildings['Shops'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        # global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        # 'Warehouse': 
        # global_var.df_Region_LA_buildings['Warehouses'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        # global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values,
        
        # 'Other': 
        # global_var.df_Region_LA_buildings['All other sectors'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna()/
        # global_var.df_Region_LA_buildings['Total'].where(global_var.df_Region_LA_buildings['Local Authority'].notnull()).dropna().values}

        # df_structre_percentages = pd.DataFrame(percentage_data)
        # df_structre_percentages = pd.concat([df_structre_percentages, global_var.df_Region_LA_buildings['Local Authority'].dropna()], axis=1)