

#Code for Mann-Whitney U test 
from statistics import median
from scipy.stats import mannwhitneyu
import pandas as pd
import numpy as np


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







def nonparametric_confidence_interval(data, confidence=0.90, n_bootstrap=10000):
    """
    Calculates a non-parametric confidence interval using the percentile bootstrap method.

    Args:
        data (list or numpy.ndarray): The sample data.
        confidence (float, optional): The confidence level (e.g., 0.90 for 90%). Defaults to 0.90.
        n_bootstrap (int, optional): The number of bootstrap samples. Defaults to 10000.

    Returns:
        tuple: A tuple containing the lower and upper bounds of the confidence interval.
    """
    
    if len(data) < 2:
      raise ValueError("Data must contain at least two values")
    
    # Generate bootstrap samples
    bootstrap_samples = np.random.choice(data, size=(n_bootstrap, len(data)), replace=True)

    # Calculate the mean of each bootstrap sample
    bootstrap_means = np.mean(bootstrap_samples, axis=1)

    # Determine the confidence interval bounds
    alpha = 1 - confidence
    lower_percentile = alpha / 2 * 100
    upper_percentile = (1 - alpha / 2) * 100
    lower_bound = np.percentile(bootstrap_means, lower_percentile)
    upper_bound = np.percentile(bootstrap_means, upper_percentile)

    return lower_bound, upper_bound








data = list(oldMenu) + list(newMenu)
print(len(data))
print(median(data))

result = nonparametric_confidence_interval(data, confidence=0.95, n_bootstrap=10000)
print(result)

