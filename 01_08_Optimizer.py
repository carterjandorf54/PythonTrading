import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    """Given a scalar X, return some vlaue (a real number)"""
    Y = (X - 1.5)**2 + 0.5
    print(f"X = {X}, Y={Y}")
    return Y

def test_run():
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method="SLSQP", options={'disp': True})
    print(f"Minima Found At: X = {min_result.x, min_result.fun}")

    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()

def fit_line(data, error_func):
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:,1])]) # Slope = 0, intercept = mean(y values)

    # Plot initial guess (Optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial Guess")

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, l, args=(data,), method="SLSQP", options={'disp': True})
    return result.x


def error(line, data):
    # Parameters
    # Line: Tuple/List/Array (C0,C1) where C0 is slope and C1 is Y-intercept
    # Data: 2D Array where each row is a point (x, y)
    # Returns error as a single real value

    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err

def use_minimizer():
    l_orig = np.float32([4,2])
    print(f"Original Line: C0 = {l_orig[0]}, C1 = {l_orig[1]}")
    Xorig = np.linspace(0,10,21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth = 2.0, label = "Original Line")

    # Generate noisy Data Points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label="Data Points")

    # Try to fit a line to this data
    l_fit = fit_line(data, error)
    print(f"Fitted Line: C0 = {l_fit[0]}, C1 = {l_fit[1]}")
    plt.plot(data[:, 0], l_fit[0] * data[:,0] + l_fit[1], 'r--', linewidth=2.0, label="Something")

    plt.legend()

    plt.show()

def error_poly(C, data):
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err

def fit_poly(data, error_func, degree=3):
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial Guess")

    result = spo.minimize(error_func, Cguess, args=(data,), method="SLSQP", options={'disp':True})
    return np.poly1d(result.x)

if __name__ == "__main__":
    use_minimizer()