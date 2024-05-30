import numpy as np
import pandas as pd
patients=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/patients.csv')
treatments=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments.csv')
treatments_cut=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/treatments_cut.csv')
adverse_reactions=pd.read_csv('/home/cr7karki/Downloads/samir/Python/DataCleaning/data-wrangling/adverse_reactions.csv')


with pd.ExcelWriter('clinical_trials.xlsx') as writer:
    patients.to_excel(writer,sheet_name='patients')
    treatments.to_excel(writer,sheet_name='treatments')
    treatments_cut.to_excel(writer,sheet_name='treatments_cut')
    adverse_reactions.to_excel(writer,sheet_name='adverse_reactions')
