import numpy as np

def make_diagonal(v):
    res = np.zeros((len(v),len(v)))
    for i in range(len(v)):
        res[i][i] = v[i]
    return res
    
    
    
