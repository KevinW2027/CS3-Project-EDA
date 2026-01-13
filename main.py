import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
df = pd.read_csv('AI_Impact_on_Jobs_2030.csv')
#print(imp.info)
df = df.iloc[:, :-10]
print(df.columns)
print(df.head(8))

sns.set_theme(style='whitegrid', context='notebook')

#1 Boxplot /  Violinplot
edu_order  = sorted(df["Education_Level"].unique())
sns.violinplot(
    data=df,
    x= "Education level",
    y= "Automation Prob 2030",
    order= edu_order,
    inner= "quartile",
    cut= 0
)
