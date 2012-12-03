#/usr/local/bin/python

import datetime as dt
import random

def GetPrime(m=''):
    """ returns a large prime """
    
    t, i = RandomValue(), 1
    
    while MR(t) == False:
        t = RandomValue()
        i += 1

    if m == 'test':
        return i

    return t
    
def MR(n, a = 0):
    """ finds primes using Miller-Rabin primality test """

    s, e, l = 0, n - 1, 1
    while(a == 0 or a > n):
            a = 2 * dt.datetime.now().microsecond / 1000 + 1

    while(e % 2 == 0):
        s, e = s + 1, e / 2

    MR2, MR1 = 0, int(str(pow(a, e, n)))
    for i in range(1, s):
        MR2 = int(str(pow(a, (2 ** i) * e, n))) - n
        if MR2 == -1:
            break
    return (MR1 == 1 or MR2 == -1)

def RandomValue():
    """ generates a random odd integer with 80-100 digits """
    
    return 2 * ((dt.datetime.now().microsecond)
              + random.randrange(10 ** 79, 10 ** 99)) + 1

