from f import *
from math import *


def riemannSum(m, a = 0, b = 1, n = 8192):
    p, q = 0.0, 0.0
    delta = (b - a) / n
    for i in range(n):
        t = delta * i + a
        ini = -2 * m * t * pi
        p += (x(t) * cos(ini) - y(t) * sin(ini)) * delta
        q += (x(t) * sin(ini) + y(t) * cos(ini)) * delta
    return (p, q)

def collect():
    def sign(n):
        if n >= 0: return 1
        return -1
    A, B = [], []
    for i in range(-50, 51):
        temp = riemannSum(i)
        A.append(temp[0])
        B.append(temp[1])
    # print(f"A = [{', '.join(['0' if c == 0 else str(abs(c) * 1e4 // 1 / 1e4 * sign(c)) for c in A])}]")
    # print(f"B = [{', '.join(['0' if c == 0 else str(abs(c) * 1e4 // 1 / 1e4 * sign(c)) for c in B])}]")
    print(f"A = [{', '.join([f'{c:.5f}' for c in A])}]")
    print(f"B = [{', '.join([f'{c:.5f}' for c in B])}]")

    

if __name__ == '__main__':
    # for i in range(100):
    #     print(f(i / 100))
    collect()
    # print(f(0.5))

