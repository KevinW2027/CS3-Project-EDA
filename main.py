import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 

df = pd.read_csv('Social Media Addiction in Students.csv')
# print(df.columns)
# -----------------------
# Global style
# -----------------------
sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (8, 5)

# -----------------------
# Question 1: Age vs Addiction Score
# -----------------------
plt.figure()

# Scatter points
sns.scatterplot(
    data=df,
    x="Age",
    y="Addicted_Score",
    hue="Gender",
    palette={"Male": "tab:blue", "Female": "tab:orange"},
    alpha=0.6
)

# Regression line for Male (blue)
sns.regplot(
    data=df[df["Gender"] == "Male"],
    x="Age",
    y="Addicted_Score",
    scatter=False,
    color="tab:blue",
    line_kws={"linestyle": "--"}
)

# Regression line for Female (orange)
sns.regplot(
    data=df[df["Gender"] == "Female"],
    x="Age",
    y="Addicted_Score",
    scatter=False,
    color="tab:orange"
)

plt.title("Age vs Social Media Addiction by Gender")
plt.xlabel("Age")
plt.ylabel("Addicted Score")
plt.legend(title="Gender")
plt.tight_layout()
plt.savefig("age_addiction_gender_regression.png", dpi=300)
plt.close()


# -----------------------
# Question 2: Gender Differences
# -----------------------
plt.figure()
sns.violinplot(
    data=df,
    x="Gender",
    y="Addicted_Score",
    inner="quartile"
)
plt.title("Social Media Addiction by Gender")
plt.xlabel("Gender")
plt.ylabel("Addicted Score")
plt.tight_layout()
plt.savefig("violin_gender_addiction.png", dpi=300)
plt.close()
'''
# -----------------------
# Question 3: Academic Performance
# -----------------------
# Question 3: Academic Level vs Addiction Score
plt.figure()
sns.boxplot(
    data=df,
    x="Academic_Level",
    y="Addicted_Score"
)
plt.title("Social Media Addiction Score by Academic Level")
plt.xlabel("Academic Level")
plt.ylabel("Addicted Score")
plt.tight_layout()
plt.savefig("box_academiclevel_addiction.png", dpi=300)
plt.close()
'''
# -----------------------
# Question 4: Sleep vs Mental Health
# -----------------------
# Create usage bins
df["Usage_Level"] = pd.cut(
    df["Avg_Daily_Usage_Hours"],
    bins=[2, 4, 6, 8],
    labels=["Low Usage", "Medium Usage", "High Usage"]
)

# Create sleep bins
df["Sleep_Level"] = pd.cut(
    df["Sleep_Hours_Per_Night"],
    bins=[3, 5, 7, 9],
    labels=["Low Sleep", "Medium Sleep", "High Sleep"]
)

# Create pivot table (mean mental health score)
heatmap_data = df.pivot_table(
    values="Mental_Health_Score",
    index="Sleep_Level",
    columns="Usage_Level",
    aggfunc="mean",
    observed=False
)

plt.figure()
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Average Mental Health Score by Sleep and Social Media Usage")
plt.xlabel("Social Media Usage Level")
plt.ylabel("Sleep Level")
plt.tight_layout()
plt.savefig("heatmap_mentalhealth_sleep_usage.png", dpi=300)
plt.show()
plt.close()

# -----------------------
# Question 5: Most Used Platform
# -----------------------
filtered_df = df[~df["Most_Used_Platform"].isin(
    ["Twitter", "Facebook", "LinkedIn"]
)]

plt.figure()
sns.boxplot(
    data=filtered_df,
    x="Most_Used_Platform",
    y="Addicted_Score"
)

plt.title("Addiction Score by Social Media Platform (Filtered)")
plt.xlabel("Most Used Platform")
plt.ylabel("Addicted Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("box_platform_addiction_filtered.png", dpi=300)
plt.close()



