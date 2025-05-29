import math
import numpy as np
#from numpy.lib.function_base import average

from ..records.record import Record


def sigma(x: Record):
    """
    Takes in array of squares of deviations.
    Returns standard deviation.
    """
    n = len(x.data)
    σ = math.sqrt(np.sum(x.data)/n*(n-1))
    return σ

def standard_deviation(record: Record|np.ndarray, unit: str, presicion=3):
    """Calculates standard deviation for given data and returns two numpy
    arrays. Deviation from average and deviation from average squared.
    """
    n        = len(record.data)
    avg      = np.average(record.data) 
    avg_dif  = np.zeros(n)
    avg_dif2 = np.zeros(n)

    for i in range(n):
        avg_dif[i] = round(record.data[i] - avg, presicion)
        avg_dif2[i] = round(avg_dif[i]**2, presicion)
    dif_label  = f"{unit}-<{unit}>"
    dif_label2 = f"({unit}-<{unit}>)^2"
    avg_dif  = Record(avg_dif, dif_label)
    avg_dif2 = Record(avg_dif2, dif_label2)
    return avg_dif, avg_dif2
