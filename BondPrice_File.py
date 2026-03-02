import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    C = couponRate * face / ppy
    
    t = np.arange(1, n + 1)
    discount = 1 / (1 + r) ** t
    
    pv_coupons = np.sum(C * discount)
    pv_face = face / (1 + r) ** n
    
    return pv_coupons + pv_face
