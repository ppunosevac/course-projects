##Copyright (c) 2012, Stephan Pardue
##Contributions include 
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without
##modification, are permitted provided that the following conditions are met: 
##
##1. Redistributions of source code must retain the above copyright notice, this
##   list of conditions and the following disclaimer. 
##2. Redistributions in binary form must reproduce the above copyright notice,
##   this list of conditions and the following disclaimer in the documentation
##   and/or other materials provided with the distribution. 
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
##ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
##WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
##DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
##ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
##(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
##(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
##The views and conclusions contained in the software and documentation are those
##of the authors and should not be interpreted as representing official policies, 
##either expressed or implied, of the FreeBSD Project.
import re
from sympy import Symbol

DEBUG = True

euclidean = lambda x : euclidean(x + [x[-2]%x[-1]]) if x[-1] != 0 else x
gcd = lambda x, y : euclidean([x, y])[-2]
divisors = lambda x : [n for n in range(2, x+1) if x % n  == 0]
common_divisors = lambda x, y : divisors(gcd(x,y))


def is_prime(x):
    for n in xrange(2, x):
        if x%n == 0:
            return False
    return True

def primes():
    x = 2
    while 1:
        if is_prime(x):
            yield x
        x+=1

def prime_factorization(x):
    """prime_factorization(226512)={11: 2, 2: 4, 3: 2, 13: 1}"""
    factors = {}
    for prime in primes():
        while x%prime == 0:
            try:
                factors[prime]+=1
            except KeyError:
                factors[prime] = 1
            x/=prime
            if is_prime(x):
                if factors.has_key(x):
                    factors[x]+=1
                else:
                    factors[x] = 1
                return factors


def lcm_by_prime_factorization(m, n):
    m = prime_factorization(m)
    n = prime_factorization(n)
    lcm = 1
    lastPrime = max(max(m), max(n))
    for prime in primes():
        if prime > lastPrime:
            break
        powM = m[prime] if m.has_key(prime) else 0
        powN = n[prime] if n.has_key(prime) else 0
        lcm*=prime**max(powM, powN)
    return lcm

lcm_euc = lambda m, n: (m*n)/gcd(m,n)

def rem_and_quo(x, y):
    """
    returns a tuple of the remainders
    and quotients used in the euclidean algorithm.
    both are lists
    """
    remainders = [x, y]
    quotients = []
    while 1:
        rem = x%y
        quo = x/y
        if rem == 0:
            break
        remainders.append(rem)
        quotients.append(quo)
        x = y
        y = rem
    return remainders, quotients

def equations(m, n):
    rems, quos = rem_and_quo(m,n)
    equations = {}
    for i, rem in enumerate(rems):
        if i+2 < len(rems):
            leftSide = str(rems[i+2])
            rightSide = "%d - (%d*%d)"%(rems[i], rems[i+1], quos[i])
            equations[leftSide] = rightSide
    return equations

def expand_expr(m, n):
    eqs = equations(m,n)
    sGcd = str(gcd(m,n))
    equation = eqs[sGcd] # start with gcd
    doneSet = set([str(m), str(n)])
    while 1:
        nums = re.findall(r"(?<!\*)\b[0-9]+\b", equation)
        if set(nums) == doneSet:
            break
        for leftSide in eqs:
            regex = r"(?<!\*)\b%s+\b"%leftSide
            equation = re.sub(regex, "(%s)"%eqs[leftSide], equation)
            if DEBUG:
                print equation
    return equation


def find_a_b(m, n):
    expr = expand_expr(m, n)
    expr = re.sub(r"\b%d\b"%m, "m", expr)
    expr = re.sub(r"\b%d\b"%n, "n", expr)
    print expr
    m = Symbol("m")
    n = Symbol("n")
    return str(eval(expr))


def test(m,n):
    out = find_a_b(m, n)
    rightSide = eval(out.replace("m", str(m)).replace("n", str(n)))
    if rightSide == gcd(m, n):
        print out
