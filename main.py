import pandas as pd
from matplotlib import pyplot as plt

imp = pd.read_csv('AI_Impact_on_Jobs_2030.csv')
#print(imp.info)
imp = imp.iloc[:, :-10]
print(imp.columns)
print(imp.head(8))