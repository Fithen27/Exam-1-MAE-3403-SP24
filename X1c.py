import random
import math

# The following code was written and debugged with the help of ChatGPT.
# Comments and docstrings below were created to best explain each step of the code

# Define the second-order ordinary differential equation (ODE): y'' - y = x
def f(x, y, z):
    """
    Defines the second-order ODE: y'' - y = x

    Args:
    x: float, independent variable
    y: float, dependent variable y
    z: float, dependent variable z (y')

    Returns:
    float, the value of the second derivative y'' given x, y, and z
    """
    return x + y

# Implement the Improved Euler method to compute one step
def improved_euler_step(x, y, z, h):
    """
    Computes one step of the Improved Euler method.

    Args:
    x: float, current value of independent variable
    y: float, current value of dependent variable y
    z: float, current value of dependent variable z (y')
    h: float, step size

    Returns:
    float, updated value of y
    float, updated value of z
    """
    # Compute the slope at the current point
    f1 = z
    # Use the slope to estimate the value of y and z at the next point
    f2 = f(x + h, y + h * z, z + h * f(x, y, z))
    # Compute the weighted average of the slopes to get the updated values of y and z
    y_new = y + h * (f1 + f2) / 2
    z_new = z + h * (f(x, y, z) + f(x + h, y + h * z, z + h * f(x, y, z))) / 2
    return y_new, z_new

# Implement the Runge-Kutta method to compute one step
def runge_kutta_step(x, y, z, h):
    """
    Computes one step of the Runge-Kutta method.

    Args:
    x: float, current value of independent variable
    y: float, current value of dependent variable y
    z: float, current value of dependent variable z (y')
    h: float, step size

    Returns:
    float, updated value of y
    float, updated value of z
    """
    # Compute the slopes at four different points to estimate the next value of y and z
    k1 = h * z
    l1 = h * f(x, y, z)
    k2 = h * (z + 0.5 * l1)
    l2 = h * f(x + 0.5 * h, y + 0.5 * k1, z + 0.5 * l1)
    k3 = h * (z + 0.5 * l2)
    l3 = h * f(x + 0.5 * h, y + 0.5 * k2, z + 0.5 * l2)
    k4 = h * (z + l3)
    l4 = h * f(x + h, y + k3, z + l3)
    # Compute the weighted average of the slopes to get the updated values of y and z
    y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z_new = z + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    return y_new, z_new

# Solve the second-order ODE using both Improved Euler and Runge-Kutta methods
def solve_ode(initial_y, initial_z, step_size, target_x):
    """
    Solves the second-order ODE using Improved Euler and Runge-Kutta methods.

    Args:
    initial_y: float, initial value of y at x=0
    initial_z: float, initial value of y' at x=0
    step_size: float, step size for numerical solution
    target_x: float, value of x at which to compute y and y'

    Returns:
    float, value of y at the target_x using Improved Euler method
    float, value of y' at the target_x using Improved Euler method
    float, value of y at the target_x using Runge-Kutta method
    float, value of y' at the target_x using Runge-Kutta method
    """
    x = 0
    y = initial_y
    z = initial_z

    while x < target_x:
        # Adjust the step size for the final step
        if x + step_size > target_x:
            step_size = target_x - x

        # Compute next step using Improved Euler method
        y, z = improved_euler_step(x, y, z, step_size)

        # Compute next step using Runge-Kutta method
        y_rk, z_rk = runge_kutta_step(x, initial_y, initial_z, step_size)

        x += step_size

    return y, z, y_rk, z_rk

# Main function to take user input and display the results
def main():
    print("For the initial value problem y’’- y = x")
    initial_y = float(input("Enter the value of y at x=0: "))
    initial_z = float(input("Enter the value of y’ at x=0: "))
    step_size = float(input("Enter the step size for the numerical solution: "))
    target_x = float(input("At what value of x do you want to know y and y’? "))

    y_ie, z_ie, y_rk, z_rk = solve_ode(initial_y, initial_z, step_size, target_x)

    print(f"At x={target_x}")
    print("For the Improved Euler method:")
    print(f"y={y_ie:.3f}, and y'={z_ie:.3f}")
    print("For the Runge-Kutta method:")
    print(f"y={y_rk:.3f}, and y'={z_rk:.3f}")

# Execute the main function
if __name__ == "__main__":
    main()
