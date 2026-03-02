import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    out = np.array(nums, dtype = object)
    mod3 = nums % 3 == 0
    mod5 = nums % 5 == 0 
    mod15 = nums % 15 == 0

    out[mod3] = 'fizz'
    out[mod5] = 'buzz'
    out[mod15] = 'fizzbuzz'
    
    return list(out)
