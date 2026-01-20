import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
import kagglehub

df = pd.read_csv('Social Media Addiction in Students.csv')
print(df.columns)
# -----------------------
# Global style
# -----------------------
sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (8, 5)

# Load your dataset
# df = pd.read_csv("social_media_addiction.csv")

# -----------------------
# Question 1: Age vs Addiction Score
# -----------------------
plt.figure()
sns.scatterplot(
    data=df,
    x="Age",
    y="Addicted_Score",
    hue="Gender",
    alpha=0.7
)
sns.regplot(
    data=df,
    x="Age",
    y="Addicted_Score",
    scatter=False,
    color="black",
    line_kws={"linestyle": "--"}
)
plt.title("Age vs Social Media Addiction Score")
plt.xlabel("Age")
plt.ylabel("Addicted Score")
plt.tight_layout()
plt.savefig("scatter_age_addiction.png", dpi=300)
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

# -----------------------
# Question 4: Sleep vs Mental Health
# -----------------------
plt.figure()
sns.scatterplot(
    data=df,
    x="Sleep_Hours_Per_Night",
    y="Mental_Health_Score",
    size="Avg_Daily_Usage_Hours",
    hue="Avg_Daily_Usage_Hours",
    alpha=0.7,
    palette="viridis"
)
plt.title("Sleep & Social Media Usage vs Mental Health")
plt.xlabel("Sleep Hours per Night")
plt.ylabel("Mental Health Score")
plt.legend(title="Avg Daily Usage Hours", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("scatter_sleep_mentalhealth.png", dpi=300)
plt.close()

# -----------------------
# Question 5: Most Used Platform
# -----------------------
plt.figure()
sns.boxplot(
    data=df,
    x="Most_Used_Platform",
    y="Addicted_Score"
)
plt.title("Addiction Score by Most Used Platform")
plt.xlabel("Most Used Platform")
plt.ylabel("Addicted Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("box_platform_addiction.png", dpi=300)
plt.close()


