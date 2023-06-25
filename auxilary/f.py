from math import *

def f(t):
    t = t % 1
    return (x(t), y(t))


### rectangle

def x(t): # 0 <= t < 1
    if t < 0.25:
        return 2 - 16 * t
    elif t < 0.5:
        return -2
    elif t < 0.75:
        return 16 * (t - 0.5) - 2
    else:
        return 2

def y(t): # 0 <= t < 1
    if t < 0.25:
        return 1
    elif t < 0.5:
        return 1 - 8 * (t - 0.25)
    elif t < 0.75:
        return -1
    else:
        return 8 * (t - 0.75) - 1


### circle
'''
def x(t): # 0 <= t < 1
    return 3 * cos(2 * pi * t)

def y(t): # 0 <= t < 1
    return 5 * sin(2 * pi * t)
'''