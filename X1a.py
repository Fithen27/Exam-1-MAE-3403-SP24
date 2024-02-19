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
        # Generating rock size following a normal distribution with mean=0.5 and standard deviation=0.1
        size = random.normalvariate(0.5, 0.1)
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
        # If the size is larger than or equal to 1 inch, it passes through the big screen
        if size >= 1:
            passed_big_screen.append(size)
        # If the size is less than 3/8 inch, it passes through the small screen
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
        # Generate rock sizes for a sample
        rocks = generate_rock_sizes(N)
        # Calculate the sample mean
        sample_mean = sum(rocks) / N
        # Calculate the sample variance
        sample_variance = sum((size - sample_mean) ** 2 for size in rocks) / (N - 1)
        # Append the sample mean and variance to their respective lists
        sample_means.append(sample_mean)
        sample_variances.append(sample_variance)
    return sample_means, sample_variances

# The following code controls the execution flow of the sampling process and computes the statistical properties
# of the sample means and displays the results

def main():
    # Parameters
    N = 100  # Number of rocks in each sample
    num_samples = 11  # Number of samples

    # Perform sampling
    sample_means, sample_variances = sample_rock_sizes(N, num_samples)

    # Compute mean and variance of sampling mean
    mean_of_means = sum(sample_means) / num_samples
    variance_of_means = sum((mean - mean_of_means) ** 2 for mean in sample_means) / (num_samples - 1)

    # Output results
    print("Sample Mean and Variance:")
    for i in range(num_samples):
        print(f"Sample {i + 1}: Mean={sample_means[i]}, Variance={sample_variances[i]}")
    print("\nMean and Variance of Sampling Mean:")
    print(f"Mean of Sampling Mean: {mean_of_means}")
    print(f"Variance of Sampling Mean: {variance_of_means}")

if __name__ == "__main__":
    main()

