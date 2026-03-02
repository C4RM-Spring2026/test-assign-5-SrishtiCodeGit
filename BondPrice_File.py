import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    y/=ppy
    couponRate /= ppy
    m*= ppy
    cf = face* couponRate
    t = np.arange(1, m+1)
    discount = (1+y) ** (-t)

    pvcfsum = (cf*discount).sum() + face*discount[-1]
    return pvcfsum
