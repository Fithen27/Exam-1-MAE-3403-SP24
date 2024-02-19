import random
import math

# The following code was written and debugged with the help of ChatGPT.
# Comments and docstrings below were created to best explain each step of the code

# The following set of code generates N random rock sizes following a normal distribution.
# The loop iterates N times, as specified by the function range(N)

def generate_rock_sizes(N):
    """
    Generates N random rock sizes following a normal distribution.

    Args:
    N: int, number of rocks

    Returns:
    list of floats, sizes of rocks
    """
    rock_sizes = []
    for _ in range(N):
        # Generating rock size following a normal distribution
        size = random.normalvariate(0.5, 0.1)  # mean=0.5, standard deviation=0.1
        rock_sizes.append(size)
    return rock_sizes

# The next set of code takes a list of rock sizes as an input and filters them based on predefined criteria
# Like passing through a specified mesh screen
# Then returns two lists containing the sizes of rocks that passed through each screen

def sieve_rocks(rock_sizes):
    """
    Sieves rocks based on mesh screen sizes.

    Args:
    rock_sizes: list of floats, sizes of rocks

    Returns:
    list of floats, sizes of rocks that passed through the 1"x1" mesh screen
    list of floats, sizes of rocks that didn't pass through the 3/8"x3/8" mesh screen
    """
    passed_big_screen = []
    passed_small_screen = []
    for size in rock_sizes:
        if size >= 1:
            passed_big_screen.append(size)
        if size < 0.375:
            passed_small_screen.append(size)
    return passed_big_screen, passed_small_screen

# This following set of code takes two parameters (N) and (num_sample) and generates samples of rock sizes
# Each containing (N) rocks, It computes the sample mean an variance for each sample and returns mean and variance

def sample_rock_sizes(N, num_samples):
    """
    Samples rock sizes and computes sample mean and variance.

    Args:
    N: int, number of rocks in each sample
    num_samples: int, number of samples

    Returns:
    list of floats, sample means
    list of floats, sample variances
    """
    sample_means = []
    sample_variances = []
    for _ in range(num_samples):
        rocks = generate_rock_sizes(N)
        sample_mean = sum(rocks) / N
        sample_variance = sum((size - sample_mean) ** 2 for size in rocks) / (N - 1)
        sample_means.append(sample_mean)
        sample_variances.append(sample_variance)
    return sample_means, sample_variances

# This function takes sample means, standard deviations, and sample sizes of two independent samples and caluclates the
# T-statistic for comparing their means. The T-statistic quantifies the difference between the means relative to the
# variability in the data, providing a measure of the significance of the observed difference

def calculate_t_statistic(mean_A, mean_B, std_dev_A, std_dev_B, n_A, n_B):
    """
    Calculates the t-statistic for two independent samples.

    Args:
    mean_A: float, sample mean of Supplier A
    mean_B: float, sample mean of Supplier B
    std_dev_A: float, standard deviation of Supplier A
    std_dev_B: float, standard deviation of Supplier B
    n_A: int, sample size of Supplier A
    n_B: int, sample size of Supplier B

    Returns:
    float, t-statistic
    """
    numerator = mean_A - mean_B
    denominator = math.sqrt((std_dev_A ** 2 / n_A) + (std_dev_B ** 2 / n_B))
    t_statistic = numerator / denominator
    return t_statistic

# This function takes as input the degrees of freedom and a specified T-Value and computes the probability of the
# T-Distribution at that t-value. This probability provides information about the likelihood of observing the given
# T-Value under t-distribution with the specified degrees of freedom.

def t_distribution_probability(degrees_freedom, t_value):
    """
    Calculate the probability of the t-distribution given degrees of freedom and t value.

    Args:
        degrees_freedom (int): Degrees of freedom for the t-distribution.
        t_value (float): Value of t for which the probability is calculated.

    Returns:
        float: Probability of the t-distribution.
    """
    # Calculate the t-distribution probability using the provided function
    numerator = math.gamma((degrees_freedom + 1) / 2)
    denominator = math.sqrt(degrees_freedom * math.pi) * math.gamma(degrees_freedom / 2)
    coefficient = math.pow(1 + (t_value ** 2 / degrees_freedom), -(degrees_freedom + 1) / 2)
    return (numerator / denominator) * coefficient

# This function takes as input two lists of sample means and conducts a one-sided t-test to determine if there is
# statistically significant difference between their means. It calculates the t-statistic, degrees of freedom, and
# p-value and predefined significance level, it makes decision about the difference in means between the two suppliers.

def perform_t_test(sample_means_A, sample_means_B):
    """
    Performs a one-sided t-test to compare two sample means.

    Args:
    sample_means_A: list of floats, sample means of Supplier A
    sample_means_B: list of floats, sample means of Supplier B
    """
    mean_A = sum(sample_means_A) / len(sample_means_A)
    mean_B = sum(sample_means_B) / len(sample_means_B)
    std_dev_A = math.sqrt(sum((mean - mean_A) ** 2 for mean in sample_means_A) / (len(sample_means_A) - 1))
    std_dev_B = math.sqrt(sum((mean - mean_B) ** 2 for mean in sample_means_B) / (len(sample_means_B) - 1))
    n_A = len(sample_means_A)
    n_B = len(sample_means_B)

    t_statistic = calculate_t_statistic(mean_A, mean_B, std_dev_A, std_dev_B, n_A, n_B)
    df = n_A + n_B - 2  # degrees of freedom

    # For a one-sided t-test, the p-value is half of the two-sided p-value
    p_value = t_distribution_probability(df, t_statistic) / 2

    # Check if the p-value is less than the significance level (α)
    alpha = 0.05
    if p_value < alpha:
        print("Supplier B's gravel size is statistically significantly smaller than Supplier A's.")
    else:
        print("Supplier B's gravel size is not statistically significantly smaller than Supplier A's.")

# The function controls the execution flow of the sampling process for two suppliers and preforms a one-sided t-test
# to compare their means. It serves as the entry point for the script.
def main():
    # Parameters
    N = 100  # Number of rocks in each sample
    num_samples = 11  # Number of samples

    # Perform sampling for Supplier A and Supplier B
    sample_means_A, _ = sample_rock_sizes(N, num_samples)
    sample_means_B, _ = sample_rock_sizes(N, num_samples)  # Assuming Supplier B also submits 11 samples

    # Perform one-sided t-test
    perform_t_test(sample_means_A, sample_means_B)


if __name__ == "__main__":
    main()
