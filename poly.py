import numpy as np

def findCoefficients(x, y, order = 3):
    return np.polyfit(x, y, order)