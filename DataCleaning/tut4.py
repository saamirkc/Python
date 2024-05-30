#data cleaning

import numpy as np
import pandas as pd
patients=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/patients.csv')
treatments=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments.csv')
treatments_cut=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments_cut.csv')
adverse_reactions=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/adverse_reactions.csv')
patients_df=patients.copy()
treatments_df=treatments.copy()
treatments_cut_df=treatments_cut.copy()
adverse_reactions_df=adverse_reactions.copy()
print(patients_df[patients_df['address'].isnull()])
#replace all missing valuew with no data
patients_df.fillna('No data',inplace=True)
#test
print(patients_df.info())
# print(treatments)
# print(treatments_cut)

treatments_df=pd.concat([treatments_df,treatments_cut_df])
print(treatments_df)

treatments_df['hba1c_change']=treatments_df['hba1c_start']-treatments_df['hba1c_end']
print (treatments_df)

treatments_df=treatments_df.melt(id_vars= ['given_name','surname','hba1c_start','hba1c_end','hba1c_change'],var_name='type',value_name='dosage_range')
print(treatments_df)
treatments_df=treatments_df[treatments_df['dosage_range']!='-']
print(treatments_df)

treatments_df['dosage_start']= treatments_df['dosage_range'].str.split('-').str.get(0)
treatments_df['dosage_end']= treatments_df['dosage_range'].str.split('-').str.get(1)
print(treatments_df)
treatments_df.drop(columns='dosage_range',inplace=True)
print(treatments_df)

treatments_df['dosage_start']=treatments_df['dosage_start'].str.replace('u','')
treatments_df['dosage_end']=treatments_df['dosage_end'].str.replace('u','')

print (treatments_df)

# print(treatments_df.info())

treatments_df['dosage_start']=treatments_df['dosage_start'].astype('int')
treatments_df['dosage_end']=treatments_df['dosage_end'].astype('int')
print(treatments_df.info())