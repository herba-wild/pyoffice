import numpy as np
import pandas as pd

year=2024
data=pd.read_excel('{0}.xls'.format(year))
print(data)
data=data.drop([0,1,3,4,5,6,7,8])
print(data)
data=data.drop('Unnamed: 1',axis=1)
print(data)
data.to_excel('{0}.xlsx'.format(year),index=False)