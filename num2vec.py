import numpy as np
import math

def num2vec_matchvie(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    sign = 1 if num > 0 else -1
    num = abs(num)
    for i in range(vec_size):
        vec[i] = (int(num) % 10) * sign / 10
        num = num * 10
    return vec

def num2vec_1d(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    vec[7] = num
    return vec

def num2vec_sign(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    sign = 1 if num > 0 else -1
    vec[0] = sign
    num = abs(num)
    for i in range(vec_size-1):
        vec[i+1] = (int(num) % 10) / 10
        num = num * 10
    return vec

def num2vec_pow(num,vec_size=8):
    vec = np.zeros(vec_size, dtype=float)
    vec[0] = num
    vec[1] = num**2
    vec[2] = num**3
    vec[3] = num**5
    vec[4] = num**7
    vec[5] = num**11
    vec[6] = num**13
    vec[7] = num**17
    return vec
