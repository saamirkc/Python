import numpy as np
import pandas as pd
patients=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/patients.csv')
treatments=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments.csv')
treatments_cut=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments_cut.csv')
adverse_reactions=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/adverse_reactions.csv')

patients.info()
print(patients[patients['address'].isnull()])
print(patients.duplicated().sum())
print(treatments)
print (treatments.describe())