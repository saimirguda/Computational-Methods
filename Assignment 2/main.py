import pandas as pd
import scipy.stats as stats
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt
import statistics as stat

# Task 1 of CMS
df = pd.read_csv("height.csv")
array = df['height'].to_numpy()
print(array)

# Plot the kernel density estimate of the data
sns.kdeplot(array, fill=True)

# Add labels and title
plt.xlabel('height')
plt.ylabel('Density')
plt.title('Empirical Distribution of Height')

# Show plot
plt.show()

# Task 2 of CMS
sorted_array = sorted(array, reverse=False)
median = stat.median(array)
mean = stat.mean(array)
iqr = stats.iqr(array)
percentile = np.percentile(array, 90)
abs_difference_mm = median - mean
skew = stats.skew(array)
kurtosis = stats.kurtosis(array)

print("Median: " + str(round(median, 5)) )
print("Mean: "+ str(round(mean, 5)))
print("IRQ: "+ str(round(iqr, 5)))
print("90th Percentile: "+ str(round(percentile, 5)))
print("Abs difference: "+ str(round(abs(abs_difference_mm), 5)))
print("Skewness: "+ str(round(skew, 5)))

print("Kurtosis: " + str(round(kurtosis, 5)))