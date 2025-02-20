   
# code for Mann-Whitney U test 
from scipy.stats import mannwhitneyu 

# perform mann whitney test 
stat, p_value = mannwhitneyu(batch_1, batch_2) 
print('Statistics=%.2f, p=%.2f' % (stat, p_value)) 

# Level of significance 
alpha = 0.05

# conclusion 
if p_value < alpha: 
    print('Reject Null Hypothesis (Significant difference between two samples)') 
else: 
    print('Do not Reject Null Hypothesis (No significant difference between two samples)')
