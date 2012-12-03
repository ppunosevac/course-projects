from easygui import *
from BooleanFunction import BooleanFunction
from hw63030 import *
from CombSter import *

if __name__ == "__main__":
    n=''
    while n!= "Cancel":
        n = buttonbox(
                "Please select program or cancel",
                "Compsci 3030 Exam programs",
                ["Boolean Table","Prime Factorization",
                 "GCD(m,n)=Am +Bn","GCD", "LCM","Euler",
                 "Combinational", "Stirling", "Primes", "LexOrder", "Cancel"])
        if n == "Boolean Table":
            x = integerbox(
                    "Imput the number of varibles you would like to use: 1-5",
                    "Boolean Table",
                    1,1,5)
            if x == 1:
                variableList = ['a','/\\','\/','~','(',')','Delete','End']
                thisstring= "g(a)="
            elif x == 2:
                variableList = ['a','b','/\\','\/','~','(',')','Delete','End']
                thisstring= "g(a,b)="
            elif x == 3:
                variableList = ['a','b','c','/\\','\/','~','(',')','Delete','End']
                thisstring= "g(a,b,c)="
            elif x == 4:
                variableList = ['a','b','c','d', '/\\','\/','~','(',')','Delete','End']
                thisstring= "g(a,b,c,d)="
            elif x == 5:
                variableList = ['a','b','c','d','e','/\\','\/','~','(',')','Delete','End']
                thisstring= "g(a,b,c,d,e)="

            while(1):
                n = buttonbox(
                    thisstring,
                    "Boolean Function",
                    variableList)
                if n == 'End':
                    break
                elif n == 'Delete':
                    if thisstring[-1] != '=':
                        thisstring = thisstring[:-1]
                else:
                    thisstring = thisstring + n
            
            boolfunction = BooleanFunction(thisstring)
            tablebool = boolfunction.truth_table()
            index = 1
            alpha = ['a','b','c','d','e']
            printtable = "a"
            while(index<x):
                printtable = printtable +" " + str(alpha[index])
                index = index+1
            printtable = printtable+"\tOut\n"
            index = 0
            for n in tablebool:
                for m in n:
                    if (index%(x+1))==(x):
                        printtable=printtable+'\t|'+str(m)+ '\n'
                    else:
                        printtable=printtable+str(m)+' '
                    index = index+1
                    
            msgbox(thisstring+"\n"+printtable,"Your Boolean Table")
            
        elif n == "Prime Factorization":
            x = integerbox(
                    "input a number to be factored",
                    "prime factorization",
                    0,
                    -100000000,
                    1000000000)
            factored = prime_factorization(x)
            primes = sorted(factored)
            output = ""
            for prime in primes:
                output+="(%d^%d)"%(prime, factored[prime])
            msgbox(output, "Prime Factorization")

        elif n == "GCD(m,n)=Am +Bn":
            m = integerbox("input m", "input m",
                    0, -10000000, 10000000)
            n = integerbox("input n", "input n",
                    0, -10000000, 10000000)
            output = """
            m = %d , n = %d
            gcd: %d
            %s = gcd(m,n)
            common divisors (there are %d of them)
            ---
            %s
            """%(
                    m,n,
                    gcd(m, n),
                    find_a_b(m,n),
                    len(common_divisors(m,n)),
                    str(common_divisors(m,n)))
            msgbox(output, "Output")

        elif n == "GCD":
            m = integerbox("input m", "input m",
                    0, -10000000, 10000000)
            n = integerbox("input n", "input n",
                    0, -10000000, 10000000)
            output = """gcd: %d"""%(gcd(m,n))
            msgbox(output, "output")
        elif n == "LCM":
            m = integerbox("input m", "input m",
                    0, -10000000, 10000000)
            n = integerbox("input n", "input n",
                    0, -10000000, 10000000)
            output = """lcm: %d"""%(lcm_euc(m,n))
            msgbox(output, "Output")
        elif n == "Euler":
            x = integerbox(
                    "Please input a positive number.",
                    "Euler Funtion",
                    0,
                    -100000000,
                    1000000000)
            output = float(x)
            factored = prime_factorization(x)
            primes = sorted(factored)
            for prime in primes:
                output = output *(1-1/float(prime))
            msgbox(msg="Euler(%d) = %d"%(x, output), title="Euler Function", ok_button="OK")
        elif n == "Combinational":
            q = integerbox("input n", "input n",
                    0, 0, 10000000)
            k = integerbox("input k", "input k",
                    0, 0, q)
            x = choose(q,k)
            msgbox(msg= "%d choose %d = %d."%(q,k,x) , title="Combinational", ok_button="OK")
        elif n == "Stirling":
            q = integerbox("input n", "input n",
                    0, 0, 10000000)
            k = integerbox("input k", "input k",
                    0, 0, q)
            x = partitions(q,k)
            msgbox(msg= "%d stirling %d = %d."%(q,k,x) , title="Stirling", ok_button="OK")
            
        elif n == "Primes":
            x = integerbox(
                    "input a number to find the primes\nthat are contain in that number.\n eg(19)\n There are 8 prime numbers\n2,3,5,7,11,13,17,19",
                    "Primes",
                    2,
                    2,
                    3000)
            u = 2
            w = ''
            numofPrimes =0
            while(u<=x):
                factored = prime_factorization(u)
                primes = sorted(factored)
                if(primes[0]==1 and primes[1]==u):
                    w=w+"%d,"%(u)
                    numofPrimes = numofPrimes +1
                    if (numofPrimes%12 == 0):
                        w = w +"\n"
                u = u+1
            msgbox(msg= "Number of primes are %d. \nPrimes of (%d) = \n"%(numofPrimes,x)+w , title="Primes", ok_button="OK")
        elif n == "LexOrder":
            x = integerbox("Please input number of letters", "Number can not exceed 3",
                    1, 1, 3)
            table = ''
            if x == 1:
                thisstring= "a"
            elif x == 2:
                thisstring= "ab"
            elif x == 3:
                thisstring= "abc"
            elif x == 4:
                thisstring= "abcd"
            table = lexorder(thisstring)              
            msgbox(msg= "The lex order of %s is\n%s"%(thisstring,table) , title="LexOrder")
    print "Program canceled"
