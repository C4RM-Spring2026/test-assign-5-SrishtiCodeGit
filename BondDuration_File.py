import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    C = couponRate * face / ppy
    
    t = np.arange(1, n + 1)
    cf = np.full(n, C)
    cf[-1] += face
    
    discount = 1 / (1 + r) ** t
    pvcf = cf * discount
    
    return np.sum(t * pvcf) / np.sum(pvcf)
