# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:44:34 2016

@author: Peter Swinburne
"""


def fib_n(n):
    i = 1
    j = 1
    k = 1
    while(i <= n):
        l = k + j
        j = k
        k = l
        i = i + 1
    return k


def fib_mn(m, n):
    a = fib_n(m)
    b = fib_n(n)
    return(b-a)
