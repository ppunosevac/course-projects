##Copyright (c) 2012, David Stevens
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

from itertools import product

def factorial( n):
    n = n
    result = 1
    for i in xrange(1, abs(n)+1):
        result *=i
    if n >= 0:return result
    else:return -result
    
def choose(n , k):
    n = n
    k = k
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n)/(factorial(k)*factorial(n-k))

def permutations_Order_Matter(n,k):
    n=n
    k=k
    if k < 0 or k > n:
        return 0
    return factorial(n)/factorial(n-k)

def permutations_Order_Not_Matter(n,k):
    if k < 0 or k > n:
        return 0
    return n**k

def stirling():
    other1 = [1]
    yield other1
    while True:
        other2=[num1*num2 for (num1,num2) in enumerate(other1)]
        other1 =[num1+num2 for (num1,num2) in zip(other2+[0],[0]+other1)]
        yield other1

def partitions(n,k):
    if n==0 or k==1:
        return 1
    stir = stirling()
    for i in range(n+1):
        rang = stir.next()
    return rang[k]

def lexorder(x):
    table = ''
    if len(x) == 1:
        abclist = list(product(x, repeat=len(x)))
        for w in abclist:
            table=table+"%s"%w +'\n'
    elif len(x) == 2:
        abclist = list(product(x, repeat=len(x)))
        for w in abclist:
            table=table+"%s %s"%w +'\n'
    elif len(x) == 3:
        abclist = list(product(x, repeat=len(x)))
        for w in abclist:
            table=table+"%s %s %s"%w +'\n'
    elif len(x) == 4:
        index = 1
        abclist = list(product(x, repeat=len(x)))
        for w in abclist:
            table=table+str(index)+"."+"%s %s %s %s"%(w) + '\t'
            if index%8==0:
                table =table +'\n'
            if index <8 or index == 9 or index == 43:
                table = table+'\t'
            index=index+1
            
    return table
