import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('enrichment/example_data/patients.csv')
patients

medications = pd.read_csv('enrichment/example_data/medications.csv')

patients.columns
medications.columns

patients['Id']
medications['PATIENT']

########################
### Medications table will merge with patients table in order to enrich it
########################

df_patients_small = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]
print(df_patients_small.sample(10).to_markdown())

df_medications_small = medications[['PATIENT', 'CODE', 'DESCRIPTION', 'BASE_COST', 'PAYER']]
print(df_medications_small.sample(10).to_markdown())

combined_df = df_medications_small.merge(df_patients_small, how='left', left_on='PATIENT', right_on='Id')

### Alternative combined
comdined_df = pd.merge(df_medications_small, df_patients_small, how='left', left_on='PATIENT', right_on='Id')

### Save to csv
combined_df.to_csv('enrichment/example_data/combined.csv')
combined_df.shape

payers_df = pd.read_csv('enrichment/example_data/payers.csv')

######
med_df = medications[['PATIENT', 'PAYER', 'CODE']]

pay_df = payers_df[['Id', 'CITY']]
pay_df = pay_df.rename(columns={'CITY' : 'CITY_PAYER'}, inplace=True)

pat_df = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]


############### Merge between med_df and pay_df
med_pay_df = med_df.merge(pay_df, how='left', left_on='PAYER', right_on='Id')




# patients_payers = payers_df[['NAME', 'Id', 'AMOUNT_COVERED']]

# patients_payers = df_patients_small.merge(payers_df_small, how='left')



########################
### merge examples 
# add medications to patients
########################
patients_simple = patients[['Id', 'SSN']]
medications_simple = medications[['PATIENT', 'DESCRIPTION']]

patients_medications = patients_simple.merge(medications_simple, 
            how='left', 
            left_on='Id', right_on='PATIENT')

print(patients_medications.head(5).to_markdown())

patients_medications = patients_medications.drop(columns=['PATIENT'])

########################
### concat examples 
########################

patient_sample_1 = patients.sample(n=10)
patient_sample_2 = patients.sample(n=10)

patients_s1_s2_concat = pd.concat([patient_sample_1, patient_sample_2])