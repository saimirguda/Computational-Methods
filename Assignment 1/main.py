import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math

np.random.seed(11933108)

mu0 = 70
mu1 = 50
mu2 = 100

sigma = np.random.normal(7, 1, 1)
print(sigma)
n = 3
alpha = 0.03
alpha1_2 = 0.04
power_speed = 0
sigma_xn = sigma / np.sqrt(n)

def calc_crit_value(alpha, mu0, sigma, n):
    critical_value = norm.ppf(1 - alpha, mu0, sigma / math.sqrt(n))
    return critical_value

def calc_power(crit_value, travel_speed, sig, n, boo):
    power = 1 - norm.cdf(crit_value, travel_speed, sig / math.sqrt(n))
    global power_speed
    if boo == math.ceil(power*100)/100:
        power_speed = travel_speed

    return power

def calc_radar_amount(mu, sigma, alpha, req_power):
    n = 0
    c_value = 0
    power = 0
    while power <= req_power:
        n += 1
        c_value = calc_crit_value(alpha, mu, sigma, n)
        power = calc_power(c_value, 1.1 * mu, sigma, n, -1)

    return n

critical_value = calc_crit_value(alpha, mu0, sigma, n)
critical_value1 = calc_crit_value(alpha1_2, mu1, sigma, n)
critical_value2 = calc_crit_value(alpha1_2, mu2, sigma, n)

print("Critical Value for mu0. CV = " ,critical_value)
print("Critical Value for mu1. CV = " , critical_value1)
print("Critical Value for mu2. CV = " , critical_value2)
print(" ")

# Plot normal distribution of Xn TEST 1
x = np.linspace(mu0 - 3 * sigma_xn, mu0 + 3 * sigma_xn, 100)
y = norm.pdf(x, mu0, sigma_xn)
plt.plot(x, y, label='Xn')

# Add horizontal line at speed limit
plt.vlines(mu0, 0, 0.2, colors='gray', linestyles='--', label='Speed limit')

# Add vertical line at threshold
plt.vlines(critical_value, 0, 0.2, colors='red', linestyles='--', label='Threshold')

# Add labels and legend
plt.xlabel('Speed (km/h)')
plt.ylabel('Probability Density')
plt.legend()

# Set y-axis limit
plt.ylim(0, 0.2)

# Show plot
plt.show()






power0 = calc_power(critical_value, 1.1 * mu0, sigma, n, -1)
print("Power for test 1 mu0. Power =" , power0)


requried_power = 0.95
num_of_radars = calc_radar_amount(mu0 , sigma, alpha, requried_power)
print("Num of radars for test 1 mu0. Radars = " , num_of_radars)
print(" ")



# Plot normal distribution of Xn TEST 2
x = np.linspace(mu1 - 3 * sigma_xn, mu1 + 3 * sigma_xn, 100)
y = norm.pdf(x, mu1, sigma_xn)
plt.plot(x, y, label='Xn')

# Add horizontal line at speed limit
plt.vlines(mu1, 0, 0.2, colors='gray', linestyles='--', label='Speed limit')

# Add vertical line at threshold
plt.vlines(critical_value1, 0, 0.2, colors='red', linestyles='--', label='Threshold')

# Add labels and legend
plt.xlabel('Speed (km/h)')
plt.ylabel('Probability Density')
plt.legend()

# Set y-axis limit
plt.ylim(0, 0.2)

# Show plot
plt.show()
power1 = calc_power(critical_value1, 1.1 * mu1, sigma, n, -1)
print("Power for test 2 mu1. Power = " ,power1)
requried_power = 0.95
num_of_radars1 = calc_radar_amount(mu1, sigma, alpha1_2, requried_power)
print("Num of radars for test 2 mu1. Radars = ", num_of_radars1)
print(" ")


# Plot normal distribution of Xn TEST 3
x = np.linspace(mu2 - 3 * sigma_xn, mu2 + 3 * sigma_xn, 100)
y = norm.pdf(x, mu2, sigma_xn)
plt.plot(x, y, label='Xn')

# Add horizontal line at speed limit
plt.vlines(mu2, 0, 0.2, colors='gray', linestyles='--', label='Speed limit')

# Add vertical line at threshold
plt.vlines(critical_value2, 0, 0.2, colors='red', linestyles='--', label='Threshold')

# Add labels and legend
plt.xlabel('Speed (km/h)')
plt.ylabel('Probability Density')
plt.legend()

# Set y-axis limit
plt.ylim(0, 0.2)

# Show plot
plt.show()
power2 = calc_power(critical_value2, 1.1 * mu2, sigma, n, -1)
print("Power for test 3 mu1. Power = " ,power2)
requried_power = 0.95
num_of_radars2 = calc_radar_amount(mu2, sigma, alpha1_2, requried_power)
print("Num of radars for test 3 mu2. Radars = ", num_of_radars2)
print(" ")
# Task d of the CMS

# TEST 1
requried_power = 0.99
speeds = np.linspace(1.1*mu0, 1.5*mu0, 1000)
powers = [calc_power(critical_value, speed, sigma, n, requried_power) for speed in speeds]

plt.plot(speeds, powers, label='Power in relation to Speed')
plt.xlabel('Car Speed (km/h)')
plt.ylabel('Power of the Test')
plt.axvline(x=power_speed, linestyle='--', color='red', label='Travel Speed')
plt.axhline(y=requried_power, linestyle='--', color='black', label='Power = 0.99')
print("Speed for power 0.99 m0. Speed for Power = ",power_speed)
plt.legend()
plt.show()

# TEST 2
speeds = np.linspace(1.1*mu1, 1.5*mu1, 1000)
powers = [calc_power(critical_value1, speed, sigma, n, requried_power) for speed in speeds]

plt.plot(speeds, powers, label='Power in relation to Speed')
plt.xlabel('Car Speed (km/h)')
plt.ylabel('Power of the Test')
plt.axvline(x=power_speed, linestyle='--', color='red', label='Travel Speed')
plt.axhline(y=requried_power, linestyle='--', color='black', label='Power = 0.99')
print("Speed for power 0.99 m1. Speed for Power = ",power_speed)
plt.legend()
plt.show()

# TEST 3
speeds = np.linspace(1.1*mu2, 1.5*mu2, 1000)
powers = [calc_power(critical_value2, speed, sigma, n, requried_power) for speed in speeds]

plt.plot(speeds, powers, label='Power in relation to Speed')
plt.xlabel('Car Speed (km/h)')
plt.ylabel('Power of the Test')
plt.axvline(x=power_speed, linestyle='--', color='red', label='Travel Speed')
plt.axhline(y=requried_power, linestyle='--', color='black', label='Power = 0.99')
print("Speed for power 0.99 m2. Speed for Power = ",power_speed)
plt.legend()
plt.show()



