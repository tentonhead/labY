import math
import numpy as np


def sigma(x):
    """
    Takes in array of squares of deviations.
    Returns standard deviation.
    """
    n = len(x)
    σ = math.sqrt(np.sum(x)/n*(n-1))
    return σ

def standard_deviation(data, presicion=3):
    """Calculates standard deviation for given data and returns two numpy
    arrays. Deviation from average and deviation from average squared.
    """
    n        = len(data)
    avg      = np.average(data) 
    avg_dif  = np.zeros(n)
    avg_dif2 = np.zeros(n)

    for i in range(n):
        avg_dif[i] = round(data[i] - avg, presicion)
        avg_dif2[i] = round(avg_dif[i]**2, presicion)
    return avg_dif, avg_dif2
