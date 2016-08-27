# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:44:13 2016

@author: Peter Swinburne
"""
from fibo import fib_n
from fibo import fib_mn


def main():
    for i in range(1, 20):
        f = fib_n(i)
        print(f)
    f = fib_mn(10, 20)
    print("Fib20 - Fib10 = ", f)


if __name__ == '__main__':
    main()
