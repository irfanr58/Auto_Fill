import pandas as pd
import os

df_main   = pd.read_excel('main_dataset_practice.xlsx', sheet_name='Main')
df_lookup = pd.read_excel('reference_table_practice.xlsx', sheet_name='Reference')

# build dict: { company_name → country }
lookup_dict_country = dict(zip(df_lookup['company_name'], df_lookup['country'], ))
lookup_dict_year = dict(zip(df_lookup['company_name'], df_lookup['year_founded'], ))


# map values; unmatched keys become NaN
df_main['country'] = df_main['company_name'].map(lookup_dict_country)
df_main['year_founded'] = df_main['company_name'].map(lookup_dict_year)

df_filled = df_main.copy()

output_file = 'df_filled.xlsx'
df_filled.to_excel(output_file, index=False)

# open the file on Windows
os.startfile(output_file)

