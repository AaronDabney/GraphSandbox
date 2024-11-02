import numpy as np

def round_vector(vector, num_decimal_places):
    return np.array(list(map(lambda x: round(x, num_decimal_places), vector)))

def floor_vector(vector, floor=0):
    min_val = min(vector)
    offsets = list(map(lambda x: (x - min_val) + floor, vector))
    return np.array(offsets)

def normalize_vector(vector):
    length = np.linalg.norm(vector)
    return vector / length

def range_vector(vector_in, floor):
    vector = floor_vector(vector_in, floor)
    ceiling = max(vector)
    return (vector / ceiling)
