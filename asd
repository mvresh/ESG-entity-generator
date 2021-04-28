   for row in df_dict:
                if config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]] == '':
                    print('blank')
                    config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]] = row
                else:
                    print('not blank')
                    config.Regions_and_LA[list(config.Regions_and_LA)[Region_index]].append(row)