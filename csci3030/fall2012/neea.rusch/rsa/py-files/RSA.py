#/usr/local/bin/python

import fractions as f
import getPrime as Prime
import RSAMethods as rsam
import random as r

class RSA:
    """ Creates RSA user """
    
    def __Eulers(self):
        """ Euler's totient function """
        p = Prime.GetPrime()
        q = Prime.GetPrime()
        return (p - 1) * (q - 1),  p * q
    
    def __init__(self, nm = 'Anonymous'):
        """ RSA class constructor """
        self.Name(nm)
        self.GenKeys()

    def GenKeys(self):
        """ create or reset all keys """
        x = self.__Eulers()
        self.__euler = x[0]
        self.__n = x[1]
        self.__e = self.__GenE()
        self.__d = self.__ModInverse(self.__e, self.__euler)

    def GetPubKeys(self,k=''):
        """ return user's keys """
        kDict = {'e' : self.__e, 'n' : self.__n}
        if kDict.has_key(k):
            return kDict[k]
        else:
            return kDict
    
    def Name(self,nm=''):
        """ username accessor """
        if len(nm) == 0:
            return self.__name
        else:
            self.__name = nm

    def __GenE(self, tmp = 0):
        while (tmp == 0 or f.gcd(tmp,self.__euler) != 1 or
               self.__ModInverse(tmp, self.__euler) == 0):
            tmp = r.randrange(9999, int(self.__euler / 10 ** 100))
        return tmp        

    def __Xgcd(self, a, b):
        if a == 0:
           return (b, 0, 1)
        else:
           g, y, x = self.__Xgcd(b % a, a)
           return (g, x - (b // a) * y, y)

    def __ModInverse(self, a, m):
        g, x, y = self.__Xgcd(a, m)
        if g == 1:
            return x % m
        else:
            return 0

    def Encrypt(self, msg, n = 0, e = 0):
        """ encrypt a string """
        if n == 0 or e == 0:
            n, k = self.GetPubKeys('n'), 1
            e = self.GetPubKeys('e')
            
        m = rsam.Encrypt(msg, n, e)

        if k == 1:
            while (msg !=
                   rsam.Decrypt(m, n, self.GetD_demo())):
                self.GenKeys()
                n = self.GetPubKeys('n')
                e = self.GetPubKeys('e')
                m = rsam.Encrypt(msg, n, e)                
        return m
    
    def Decrypt(self, msg, n = 0, d = 0):
        if n == 0:
            n = self.GetPubKeys('n')
        if d == 0:
            d = self.GetD_demo()
        """ decrypt a string """
        return rsam.Decrypt(msg, n, d)

    def GetD_demo(self):
        """ return private key """
        return self.__d    
