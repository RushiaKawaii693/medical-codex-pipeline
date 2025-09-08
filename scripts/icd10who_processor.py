## import Module1_MedicalCodexes/icd/who/icd102019syst_codes.txt file as pandas df

import pandas as pd

file_path = 'input\icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

df_whose = df[[
    'icd10_code',
    'detailed_title'
]]

df_whose = df_whose.rename(columns={
    'icd10_code':'code',
    'detailed_title':'description'
})
df_whose['last_updatede'] ='2025-09-07'

output_path = 'output/icd10whose.csv'
df_whose.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())

