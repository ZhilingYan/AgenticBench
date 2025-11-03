import pandas as pd
from scipy.stats import mannwhitneyu, wilcoxon

"""
Mann-Whitney U test for non-paired data
"""
df = pd.read_excel('data.xlsx')
agree_scores = []
disagree_scores = []
for _, row in df.iterrows():
    if row.iloc[1] == 1:
        score = 3
    elif row.iloc[2] == 1:
        score = 2
    elif row.iloc[3] == 1:
        score = 1
    else:
        continue
    if row.iloc[4] == 1:
        agree_scores.append(score)
    else:
        disagree_scores.append(score)

stat, p = mannwhitneyu(agree_scores, disagree_scores, alternative='greater')
# print(stat, p)
n1, n2 = len(agree_scores), len(disagree_scores)
r_rb = 2*stat/(n1*n2) - 1
print(p, r_rb)

"""
Wilcoxon test for paired data
"""
import pandas as pd
from scipy.stats import wilcoxon

m1, m2, m3 = [], [], []
for _, r in df.iterrows():
    s = {r.iloc[1]: 3, r.iloc[2]: 2, r.iloc[3]: 1}
    m1.append(s[1])
    m2.append(s[2])
    m3.append(s[3])

mean1 = sum(m1)/len(m1)
mean2 = sum(m2)/len(m2)
mean3 = sum(m3)/len(m3)

stat12, p12 = wilcoxon(m1, m2, alternative='greater')
stat13, p13 = wilcoxon(m1, m3, alternative='greater')
stat23, p23 = wilcoxon(m2, m3, alternative='greater')

p12 *= 3
p13 *= 3
p23 *= 3

import numpy as np
def rb(x,y):
    d=np.array(x)-np.array(y)
    return (np.sum(d>0)-np.sum(d<0))/(np.sum(d!=0))

rb12,rb13,rb23 = rb(m1,m2), rb(m1,m3), rb(m2,m3)

print(p12, p13, p23, mean1, mean2, mean3, rb12, rb13, rb23)
print("--------------------------------")


df_task = df.groupby('medical_task')
for task, group in df_task:
    m1, m2, m3 = [], [], []
    for _, r in group.iterrows():
        s = {r.iloc[1]: 3, r.iloc[2]: 2, r.iloc[3]: 1}
        m1.append(s[1])
        m2.append(s[2])
        m3.append(s[3])
    stat12, p12 = wilcoxon(m1, m2, alternative='greater')
    stat13, p13 = wilcoxon(m1, m3, alternative='greater')
    stat23, p23 = wilcoxon(m2, m3, alternative='greater')
    mean1, mean2, mean3 = sum(m1)/len(m1), sum(m2)/len(m2), sum(m3)/len(m3)
    rb12, rb13, rb23 = rb(m1, m2), rb(m1, m3), rb(m2, m3)
    print(p12, p13, p23)
    print(task, p12*3, p13*3, p23*3, mean1, mean2, mean3, rb12, rb13, rb23)
    print("--------------------------------")


df_group = df[df.iloc[:, -1] == 1]
m1, m2, m3 = [], [], []
for _, r in df_group.iterrows():
    s = {r.iloc[1]: 3, r.iloc[2]: 2, r.iloc[3]: 1}
    m1.append(s[1])
    m2.append(s[2])
    m3.append(s[3])
stat12, p12 = wilcoxon(m1, m2, alternative='greater')
stat13, p13 = wilcoxon(m1, m3, alternative='greater')
stat23, p23 = wilcoxon(m2, m3, alternative='greater')

print(len(m1), len(m2), len(m3))
p12 *= 3
p13 *= 3
p23 *= 3
mean1, mean2, mean3 = sum(m1)/len(m1), sum(m2)/len(m2), sum(m3)/len(m3)
rb12, rb13, rb23 = rb(m1, m2), rb(m1, m3), rb(m2, m3)
print(p12, p13, p23, mean1, mean2, mean3, rb12, rb13, rb23)
print("--------------------------------")


