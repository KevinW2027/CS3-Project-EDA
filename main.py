import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
df = pd.read_csv('AI_Impact_on_Jobs_2030.csv')
#print(imp.info)
df = df.iloc[:, :-10]
#print(df.columns)
#print(df.head(8))
'''job_counts_df = df["Job_Title"].value_counts().reset_index()
job_counts_df.columns = ["Job_Title", "Count"]
print(job_counts_df)'''

se_df = df[df["Job_Title"] == "Software Engineer"]

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
plt.close()

#2
sns.scatterplot(
    data=se_df,
    x="AI_Exposure_Index",
    y="Automation_Probability_2030",
    hue="Risk_Category",
    alpha=0.7
)

sns.regplot(
    data=se_df,
    x="AI_Exposure_Index",
    y="Automation_Probability_2030",
    scatter=False,
    color="black",
    line_kws={"linestyle": "--"}
)

plt.title("AI Exposure vs Automation Probability")
plt.xlabel("AI Exposure Index")
plt.ylabel("Automation Probability (2030)")
plt.legend(title="Risk Category")
plt.savefig("AI Exposure vs Automation Probability.png", dpi=300)
plt.close()

#3
sns.scatterplot(
    data=df,
    x="Average_Salary",
    y="Automation_Probability_2030",
    hue="Education_Level",
    alpha=0.7
)

plt.title("Average Salary vs Automation Probability")
plt.xlabel("Average Salary")
plt.ylabel("Automation Probability (2030)")
plt.legend(title="Education Level")
plt.savefig("Average Salary vs Automation Probability.png", dpi=300)
plt.close()
