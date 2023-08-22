from os import *
from sys import *
from collections import *
from math import *

def pow(X, N):

    # Write your code here.
    # print((X^N))
    X = int(X)
    N = int(N)

    if N == 0:
        return 1
    if N == 1:
        return X
    if N % 2 == 0:
        half_power = pow(X, N // 2)
        return half_power * half_power
    
    else:
        half_power = pow(X, (N - 1) // 2)
        return X * half_power * half_power
    
    pass