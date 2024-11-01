import numpy as np

def roundVector(vector, numDecimalPlaces):
    return np.array(list(map(lambda x: round(x, numDecimalPlaces), vector)))

def floorVector(vector, floor=0):
    minValue = min(vector)
    offsetArray = list(map(lambda x: (x - minValue) + floor, vector))
    return np.array(offsetArray)

def normalizeVector(vector):
    length = np.linalg.norm(vector)
    return vector / length

def rangeVector(vectorIn, floor):
    vector = floorVector(vectorIn, floor)
    ceiling = max(vector)
    return (vector / ceiling)
