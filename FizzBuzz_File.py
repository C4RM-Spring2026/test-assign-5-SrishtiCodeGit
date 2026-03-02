import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = nums.astype(object)
    
    fizz = nums % 3 == 0
    buzz = nums % 5 == 0
    
    result[fizz & buzz] = "fizzbuzz"
    result[fizz & ~buzz] = "fizz"
    result[buzz & ~fizz] = "buzz"
    
    return result
