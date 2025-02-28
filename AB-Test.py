

# code for Mann-Whitney U test 
from scipy.stats import mannwhitneyu
import pandas as pd


#Load data
df = pd.read_csv('Wages from Ala Restaurant (05_09_2024 - 01_30_2025) - Sheet1.csv')
print(df)

oldMenu = df['Gross Earnings'][:6].astype(float)
newMenu = df['Gross Earnings'][7:13].astype(float)

#Show data buckets
#print(oldMenu)
#print(newMenu)

# perform mann whitney test 
stat, p_value = mannwhitneyu(newMenu, oldMenu, alternative='greater') 
print('Statistics=%.2f, p=%.2f' % (stat, p_value)) 

# Level of significance 
alpha = 0.05

# conclusion 
#The null hypothesis is that revenue increases by 5 - 10% when the menu is changed
#The alternate hypothesis is that revenue does not increase by at least 5%

if p_value < alpha: 
    print('Reject Null Hypothesis (There IS NOT an a increase in revenue)') 
else: 
    print('Do not Reject Null Hypothesis (There IS an a increase in revenue)')
