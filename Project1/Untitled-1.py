
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def multiply(a,b):
    if a >10:
        ans = a+b
    else:
        ans = a-b
        
    return ans

if __name__ == '__main__':
    a = int(input('please enter a number'))
    b= int(input('please enter another number'))
    print(multiply(a,b))
# print(2+2)
