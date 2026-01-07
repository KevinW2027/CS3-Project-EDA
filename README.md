# EDA Project

Link to dataset:
[AI impact on jobs by 2030](https://www.kaggle.com/datasets/khushikyad001/ai-impact-on-jobs-2030)

* Column 1: description of column

'Job_Title', 'Average_Salary', 'Years_Experience', 'Education_Level',
       'AI_Exposure_Index', 'Tech_Growth_Factor',
       'Automation_Probability_2030', 'Risk_Category'

## Hypotheses/Questions 

1. Jobs requiring higher education have lower automation probability. 
2. Higher AI exposure reduces automation risk.
3. Higher-paying jobs have lower automation probability.
4. Jobs in high-tech-growth fields with high AI exposure are at higher risk if automation probability is strong.
5. Jobs requiring more experience are less likely to be automated.
6. Jobs with higher AI exposure tend to have higher salaries.
7. Jobs in industries with rapid tech growth are at higher automation risk, especially if AI exposure is low.



## Visualization Plan

1. Boxplot of Automation_Probability_2030 grouped by Education_Level.
2. Scatter plot of AI_Exposure_Index vs Automation_Probability_2030, colored by Risk_Category
3. Scatter plot of Average_Salary vs Automation_Probability_2030
4. Bubble chart: Job_Title on x-axis, Automation_Probability_2030 on y-axis, bubble size = Tech_Growth_Factor.
5. Clustered bar chart showing average Automation_Probability_2030 for each Job_Title across low, medium, and high Tech_Growth_Factor.

https://python-graph-gallery.com/boxplot/