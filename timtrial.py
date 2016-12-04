import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.style.use('ggplot')
#matplotlib inline
from sklearn.linear_model.logistic import LogisticRegression
def get_admission():
        admission_df = pd.read_csv("/Users/FaisalAmeen/Desktop/mimic3/demo/ADMISSIONS.csv", sep=',',header=0)
        return admission_df \
            .drop('ROW_ID', 1) \
            .drop('SUBJECT_ID', 1) \
            .drop('ADMISSION_LOCATION', 1) \
            .drop('DISCHARGE_LOCATION', 1) \
            .drop('INSURANCE', 1) \
            .drop('LANGUAGE', 1) \
            .drop('RELIGION', 1) \
            .drop('MARITAL_STATUS', 1) \
            .drop('ETHNICITY', 1) \
            .drop('EDREGTIME', 1) \
            .drop('EDOUTTIME', 1) \
            .drop('HAS_CHARTEVENTS_DATA', 1)

def get_chartevents():
        chartevents_df = pd.read_csv("/Users/FaisalAmeen/Desktop/mimic3/demo/CHARTEVENTS.csv", sep=',',header=0)
        return chartevents_df \
            .drop('ROW_ID', 1) \
            .drop('SUBJECT_ID', 1) \
            .drop('ICUSTAY_ID', 1) \
            .drop('CHARTTIME', 1) \
            .drop('STORETIME', 1) \
            .drop('CGID', 1) \
            .drop('VALUE', 1) \
            .drop('VALUEUOM', 1) \
            .drop('WARNING', 1) \
            .drop('ERROR', 1) \
            .drop('RESULTSTATUS', 1) \
            .drop('STOPPED', 1)

admission_df=get_admission()
chartevents_df=get_chartevents()
#vitals_labs = pd.merge(vitals_train,labs_train, left_index=True,right_index=True, how='outer')
vitals_labs_icu = admission_df[admission_df['HOSPITAL_EXPIRE_FLAG'] == 1 ]
vitals_labs_icu = vitals_labs_icu[vitals_labs_icu['DIAGNOSIS'] == 'SEPSIS']
print vitals_labs_icu

hospital_ids = vitals_labs_icu['HADM_ID']
print hospital_ids

for i in hospital_ids:
	chartevents_hadmi=chartevents_df[chartevents_df['HADM_ID'] == i]
print chartevents_hadmi
