import pandas as pd
import numpy as np
import pandas_profiling as pp
data=pd.read_csv('Dataset.csv')

print('----------------------------')
print(data.describe())
print('-----------------------------')
print(data.info())
print('-----------------------------')
profilereport=pp.ProfileReport(data)
profilereport.to_file('index.html')