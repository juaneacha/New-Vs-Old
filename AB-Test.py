

#Code for Mann-Whitney U test 
from scipy.stats import mannwhitneyu
import pandas as pd


#Load data
df = pd.read_csv('Wages from Ala Restaurant (05_09_2024 - 01_30_2025) - Sheet1.csv')
print(df)

#Sampling the data for old and new menus
df = df[:12]
df['Gross Earnings'] = df['Gross Earnings'].astype(float)
oldMenu = df[df['Menu'] == 'Old']['Gross Earnings']
newMenu = df[df['Menu'] == 'New']['Gross Earnings']

#Show data for old and new menus
print(oldMenu)
print(newMenu)

#Perform mann whitney test 
stat, p_val = mannwhitneyu(newMenu, oldMenu, alternative='less') 
print('Statistics=%.2f, p=%.2f' % (stat, p_val)) 

#Level of significance 
alpha = 0.05

#Conclusion 
#Introducing a New Menu can increase revenue by 10% to 15% according to Sling. Therefore:
    #The null hypothesis is that new menu's revenue is GREATER than old menu's revenue
    #The alternate hypothesis is that new menu's revenue is LESS than old menu's revenue

if p_val < alpha: 
    print('Reject Null Hypothesis (new menu`s revenue IS NOT greater than old menu`s)') 
else: 
    print('Do Not Reject Null Hypothesis (new menu`s revenue IS greater than old menu`s)')
