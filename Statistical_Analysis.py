#one-tailed t test


# Insert your values for Day 7 here
mean_A = INSERT_MEAN_A_VALUE
sd_A = INSERT_STANDARD_DEVIATION_A_VALUE
n_A = INSERT_SAMPLE_SIZE_A_VALUE

# Insert your values for Day 2 here
mean_B = INSERT_MEAN_B_VALUE
sd_B = INSERT_STANDARD_DEVIATION_B_VALUE
n_B = INSERT_SAMPLE_SIZE_B_VALUE

# Calculate the t-statistic
numerator = mean_A - mean_B
denominator = np.sqrt((sd_A**2 / n_A) + (sd_B**2 / n_B))
t_statistic = numerator / denominator

# Degrees of freedom for a two-sample t-test
degrees_of_freedom = n_A + n_B - 2

# One-tailed p-value (since it's an upper-tail test, we use 1 - t.cdf)
p_value = 1 - t.cdf(t_statistic, df=degrees_of_freedom)

# Print the calculated p-value
print("One-tailed p-value:", p_value)

# Specify the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than alpha
if p_value < alpha:
    print("Reject the null hypothesis. The mean of Group A is statistically greater than the mean of Group B.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to conclude that the mean of Group A is statistically greater than the mean of Group B.")

