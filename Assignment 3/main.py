import pandas as pd
import scipy.stats as stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

import numpy as np

df = pd.read_csv('wages.csv')


# Extract only the rows where the 'Gender' column is 'Female'
female_data = df[df['gender'] == 'F']
female_wages = female_data.annual_salary.values
male_data = df[df['gender'] == 'M']
male_wages = male_data.annual_salary.values
# `female_data` is a list of rows in the CSV file where the 'Gender' column is 'Female'



def plot_edf(data, sex):
    color="blue"
    gen = "Male"
    if(sex == 0):
        color="red"
        gen = "Female"
    sns.kdeplot(data, cumulative=False, color=color)
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Empirical Distribution Function for ' + gen )
    plt.xlim([0, 350000])
    plt.show()

def plot_ecdf(data, sex):
    color="blue"
    gen = "Male"
    if(sex == 0):
        color="red"
        gen = "Female"
    sns.kdeplot(data, cumulative=True, color=color)
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Empirical Distribution Function for ' + gen)

    plt.xlim([0, 350000])
    plt.show()
# Example usage

plot_edf(female_wages, 0)
plot_edf(male_wages, 1)

plot_ecdf(female_wages, 0)
plot_ecdf(male_wages, 1)


# Note: This block takes 4-7 Minutes, depending on your machine.

import numpy as np

observed_statistic, pvalue = stats.ks_2samp(female_wages, male_wages)


num_permutations = 10000
permuted_statistics = []
counter = 0
for i in range(num_permutations):
    permuted_group1 = np.random.permutation(np.concatenate((female_wages, male_wages)))[:len(female_wages)]
    permuted_group2 = np.random.permutation(np.concatenate((female_wages, male_wages)))[len(male_wages):]
    permuted_statistic, _ = stats.ks_2samp(permuted_group1, permuted_group2)
    permuted_statistics.append(permuted_statistic)
    if (permuted_statistic >= observed_statistic) | (permuted_statistic <= -observed_statistic):
        counter += 1


pvalue = (counter+1) / (num_permutations+1)
print("P-value of the test is " + str(pvalue))
import seaborn as sns
import matplotlib.pyplot as plt


# Plot the empirical density of the permuted test statistics
sns.kdeplot(permuted_statistics, color='blue')
plt.axvline(observed_statistic, color='red', label='Observed Test Statistic')

# Add a label to the x-axis
plt.xlabel('Permuted Test Statistics')

# Add a label to the y-axis
plt.ylabel('Density')

# Show the plot
plt.show()

import numpy as np

observed_statistic = np.mean(female_wages) - np.mean(male_wages)
num_permutations = 10000
permuted_statistics = []
counter_mean = 0
for i in range(num_permutations):
    permuted_group1 = np.random.permutation(np.concatenate((female_wages, male_wages)))[:len(female_wages)]
    permuted_group2 = np.random.permutation(np.concatenate((female_wages, male_wages)))[len(female_wages):]
    permuted_statistic = np.mean(permuted_group1) - np.mean(permuted_group2)
    permuted_statistics.append(permuted_statistic)
    if (permuted_statistic >= observed_statistic) or (permuted_statistic <= -observed_statistic) :
        counter_mean += 1


pvalue = (counter_mean+1) / (num_permutations +1)
print("counter = " + str(counter_mean))
print(num_permutations)
print(pvalue)

# Plot the empirical density of the permuted test statistics
sns.kdeplot(permuted_statistics, color='blue')
plt.axvline(observed_statistic, color='red', label='Observed Test Statistic')

# Add a label to the x-axis
plt.xlabel('Permuted Test Statistics')

# Add a label to the y-axis
plt.ylabel('Density')

# Show the plot
plt.show()
