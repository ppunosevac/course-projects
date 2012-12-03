#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import getPrime as gP
import RSAMethods as rM
import random
import time
import RSA


# ----- Test Encryption and Decryption ------------------------------------------------

def SmTest(n = 0, e = 0, d = 0):
    """ simple test for encryption/decryption """
    s = raw_input("Enter some string: ") 

    if n == 0 or e == 0 or d == 0:
        user = RSA.RSA()
        s = user.Encrypt(s)
        print "After En-&Decrypt: {}".format(user.Decrypt(s))

    else:
         s = rM.Encrypt(s, n, e)
         print "After En-&Decrypt: {}".format(rM.Decrypt(s, n, d))


def CryptTest(n, mInput = False, newKeys = True, ShowStrings = False):
    """ test encryption and decryption, n -> iterations """

    strgs = []
    if mInput == True:
        for i in range(0, n):
            strgs.append(raw_input("Enter test string: "))
    else:
        strgs.append(u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSTUVWXYZ123456789")
        strgs.append(u"hello world here are some random words")
        strgs.append(u"This will be a string with unicode characters: \xf8\x100\xff")
        strgs.append("213717823612736182361872361872361782361278361827631872362172316782")
        strgs.append(u"aksjdkajdalksjdalksdjalskdjasldkjalsdkjasldjasljakdsjasj")
        strgs.append(u"this is some string")
        strgs.append(u"short string")
        strgs.append(u"sample input: my pw is password")
        strgs.append(u"Today is \x53\x75\x6e\x64\x61\x79")
        strgs.append(u"Hercules is a hero")
        strgs.append(u"These next ones will be long strings")
        strgs.append(u"It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        strgs.append(u"Ukko nooa ukko nooa oli kunnon mies, Kun han meni saunaan laittoi laukun naulaan, ukko nooa ukko noaa oli kunnon mies. Paljon onnea vaan paljon onnea vaan, paljon onnea wahteveryournameis paljon onnea vaan!")
        strgs.append(u"Nulla sed erat quis diam luctus dignissim ac at quam. Sed blandit lectus vel elit aliquam eget placerat purus rutrum. Aenean vel urna purus, mattis mollis ipsum.")
        strgs.append(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque semper metus at magna scelerisque vestibulum. Nulla sed erat quis diam luctus dignissim ac at quam. Sed blandit lectus vel elit aliquam eget placerat purus rutrum. Aenean vel urna purus, mattis mollis ipsum. Morbi placerat orci nec neque consectetur congue. Aliquam dignissim tortor id turpis ornare nec hendrerit lorem malesuada. Etiam a sem ac ante sollicitudin aliquam eget et risus. Curabitur fringilla risus in dui eleifend eget tristique ligula aliquam. Etiam vel libero sed sem scelerisque accumsan. Morbi mattis malesuada lacus, in venenatis metus imperdiet et. Donec at neque ac lacus suscipit aliquet sit amet a justo. Donec sit amet pretium ligula. In hac habitasse platea dictumst. Donec feugiat, quam at dignissim scelerisque, felis tellus consectetur neque, sed suscipit nulla enim ac lacus. Pellentesque nisl eros, blandit quis eleifend at, gravida nec elit. Sed ac ligula erat.")
        strgs.append(u"Nam suscipit dapibus augue, sit amet accumsan leo cursus pulvinar. Morbi sed nibh lacus. Cras sit amet venenatis dolor. Sed sem diam, consequat nec laoreet sit amet, luctus eget nisi. Etiam ornare ante a massa lacinia luctus. Vestibulum id purus mauris. Nam lectus purus, lacinia in vulputate a, semper quis elit. Maecenas eget magna non odio aliquet dapibus.")
        strgs.append(u"Nulla ut augue urna, at placerat nibh. Sed sit amet ante eget risus mattis hendrerit. Praesent nulla nunc, facilisis quis ultrices sit amet, viverra in est. Mauris euismod fermentum purus ut rutrum. Donec convallis adipiscing mauris, et ornare nulla pretium non. Praesent iaculis tristique varius. Integer sed mauris et turpis imperdiet fringilla sit amet nec tortor. Praesent mollis enim eget est eleifend pellentesque. Nam eget elit at turpis ultrices tempor.")

    if n > len(strgs):
        n = len(strgs)
        
    # column setup
    colSetup = "{0:6}{1:^20}{2:^20}{3:>20}"
    dashes = colSetup.format('-' * 6, '-' * 20, '-' * 20, '-' * 20)
    print colSetup.format('#',
                          'string length',
                          'Input == Output',
                          'Exectime (s)')
    print dashes

    p = RSA.RSA()
    results, pct = [], 0

    for i in range(0, n):
        s, t = strgs[i], []
        t.append(len(s))

        t0 = time.clock()
        x = p.Encrypt(s)
        y = p.Decrypt(x)
        t1 = time.clock() - t0

        t.append(y == s)
        pct += int(y == s)
        t.append(str(round(t1, 10)))

        print colSetup.format(str(i + 1).zfill(3) + '.  ',
                              t[0], t[1], t[2])

        results.append([s, y])

        # setting newKeys = True will create new keys for each iteration
        if newKeys == True:
            p.GenKeys()

    print dashes

    print "\nAll strings encrypted using {} keys".format(
        "different" if newKeys == True else "same")

    print "Overall accuracy: {} %".format(str(round(100 * float(pct)/float(n),2)))

    if ShowStrings == True:
        print "\n\nString input/Decrypted Output: "
        for i in results:
            print i[0]
            print i[1]
            print dashes
            
        
# ----- Some methods for testing exectime ---------------------------------------------

def doPrimeTime():
    """ returns # of iterations until prime found, exectime """
    
    t0 = time.clock()
    x = gP.GetPrime('test')
    y = (time.clock() - t0)
    return x, y

def PrimeTest(n, prt = True):
    """ Test individual exectime of GetPrime method """

    # column setup
    colSetup = "{0:6}{1:>16}{2:>13}{3:>20}"
    dashes = colSetup.format('-' * 6, '-' * 16, '-' * 13, '-' * 20)
    
    if prt == True:
        print colSetup.format('#', 'Exectime (s)',
                              'Repetitions',
                              'Exectime/rep (ms)')
        print dashes 

    res=[[],[],[]]

    # loop to test exectime
    for i in range(1, n + 1):
        c = doPrimeTime()
        res[0].append(round(c[1], 10))
        res[1].append(int(c[0]))
        res[2].append(round((c[1]/c[0]) * (10 ** 4), 10))

        if prt == True:
            print colSetup.format(
                    str(i).zfill(3) + '.  ',
                    str(res[0][i-1]), res[1][i-1], str(res[2][i-1]))

    # average of each column
    avg = (str(round(sum(res[0]) / float(len(res[0])), 10)),
           int(round(sum(res[1]) / float(len(res[1])), 0)),
           str(round(sum(res[2]) / float(len(res[2])), 10)))
               
    if prt == True:
        print dashes  
        print colSetup.format('AVRG', avg[0], avg[1], avg[2])

    return avg


def TestMeanTime(n, k):
    """ Test average exectime of GetPrime
        n -> total # of iterations, k -> # of iterations / each mean
        e.g. n = 10, k = 5: get average time of 5 iterations of GetPrime,
        repeat 10 times
    """

    # column setup
    colSetup = "{0:6}{1:>16}{2:>13}{3:>20}"
    dashes = colSetup.format('-' * 6, '-' * 16, '-' * 13, '-' * 20)
    tot=[[],[],[]]

    # loop to test time
    for n in range(1, n + 1):

        avg = PrimeTest(k, False)
        
        tot[0].append(float(avg[0]))
        tot[1].append(avg[1])
        tot[2].append(float(avg[2]))
        print colSetup.format(str(n).zfill(3) + '.  ', avg[0], avg[1], avg[2])


    # print average of all rows
    print dashes
    print colSetup.format('AVRG',
        str(round(sum(tot[0]) / float(len(tot[0])), 10)),
        int(round(sum(tot[1]) / float(len(tot[1])), 0)),
        str(round(sum(tot[2]) / float(len(tot[2])), 10)))
