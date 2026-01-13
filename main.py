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
edu_order = sorted(df["Education_Level"].unique())

sns.boxplot(
    data=df,
    x="Education_Level",
    y="Automation_Probability_2030",
    order=edu_order
)
plt.title("Automation Probability by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Automation Probability (2030)")
plt.savefig("box_automation_by_education.png", dpi=300)
plt.show()