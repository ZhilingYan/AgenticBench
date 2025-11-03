import pandas as pd
from statsmodels.stats.proportion import proportion_confint

"""
agree/disagree & call_agent 
"""

df = pd.read_excel('data.xlsx')
col5 = df.iloc[:, 4]
result = col5.value_counts()
print(result)

count = result.iloc[0]
total = len(col5)
mean = count / total
lower, upper = proportion_confint(count, total, alpha=0.05, method='normal')
print(f"mean: {mean:.4f}, 95% CI: [{lower:.4f}, {upper:.4f}]")


df_task = df.groupby('medical_task')
for task, group in df_task:
    counts = group.iloc[:, 4].value_counts()
    total = len(group)
    for value, count in counts.items():
        if value == 0:
            continue
        mean = count / total
        lower, upper = proportion_confint(count, total, alpha=0.05, method='normal')
        print(f"Task: {task}, Value: {value}")
        print(f"Count: {count}, Total: {total}")
        print(f"mean: {mean:.4f}, 95% CI: [{lower:.4f}, {upper:.4f}]")


col_last = df.iloc[:, -1]
result = col_last.value_counts()
print(result)
for value, count in result.items():
    df_value = df[df.iloc[:, -1] == value]
    counts = df_value.iloc[:, 4].value_counts()
    total = len(df_value)
    for value, count in counts.items():
        if value == 0:
            continue
        mean = count / total
        lower, upper = proportion_confint(count, total, alpha=0.05, method='normal')
        print(f"Value: {value}, Count: {count}, Total: {total}, Mean: {mean:.4f}, 95% CI: [{lower:.4f}, {upper:.4f}]")

df_task = df.groupby('medical_task')
for task, group in df_task:
    counts = group.iloc[:, -1].value_counts()
    total = len(group)
    for value, count in counts.items():
        if value == 0:
            continue
        mean = count / total
        print(f"Task: {task}, Value: {value}, Count: {count}, Total: {total}, Mean: {mean:.4f}")