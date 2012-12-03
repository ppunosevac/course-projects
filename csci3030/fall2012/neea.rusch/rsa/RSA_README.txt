RSA IMPLEMENTATION

This project demonstrates the RSA protocol and enables encryption/decryption
of alphanumeric strings

  - Author: Neea Rusch nrusch at aug dot edu 
  - This is a school project, so use it at your own risk
  - Created and completed sometime Sep - Oct 2012
  - References/General background information about RSA:
    Cetin Kaya Koc "High-Speed RSA Implementation" (1994), Bender &
    Williamson, "A Short Course in Discrete Mathematics" (2004)

    SYSTEM REQUIREMENTS
  - Created on Windows/Python Shell 2.7.3. Have not tested on
    on other OS/python implementations
  - Code uses only standard libraries (datetime, random, sys, time etc.)
    As long as these are accessible, program should run as intended

    FILES ETC
    This project consists of 6 files, the "support" files have an underscore:

      (1) RSA.py            - The main class
      (2) RSAMethods.py     - Encrypt and decrypt data
      (3) getPrime.py       - Generates large primes
      (4) RSA_demo.py       - Demonstrates functions of the main class
      (5) RSA_exectest.py   - Different exec test related to main class
      (6) RSA_README.txt    - Docs

-------------------------------------------------------------------------------
GENERAL DOCUMENTATION AND USE
-------------------------------------------------------------------------------

The implementation is fully accessible through the main RSA-class.

This is an object oriented solution. Creating an instance of the class will
generate an RSA-user object. Each user has:
    
  1) their own set of public/private keys
  2) ability to access and reset their keys
  3) ability to encrypt and decrypt messages using their own  
     or someone else's keys

To create an instance of the class: 
>>> objName = RSA(['name'])

The name parameter is optional and you may also set it later. Initializing an
object will automatically generate keys for the user. Initializing an object
requires generating two random large primes through the GetPrime() method,
and so execution time of the initialization depends on how fast the program
can compute two such primes. See reference Table 1 below for execution time
testing results.

After creating a RSA-user object, the following methods are accessible from
outside the class:
    
  1) GenKeys             
  2) GetPubKeys
  3) Encrypt
  4) Decrypt
  5) Name
  6) GetD_demo

-------------------------------------------------------------------------------
DESCRIPTIONS OF CLASS METHODS
-------------------------------------------------------------------------------

GenKeys() 
    Method replaces current RSA keys with new ones. This method resets all
    keys and once the keys have been replaced, the old keys cannot be restored.

GetPubKeys(['key-name']) 
    Method returns a dictionary with public e and n keys and their values
    respectively. Specifying a key parameter ('n' or 'e') will return the int
    value of the specified key. The secret key d is not accessible through
    this method. Prime numbers p and q, where n = pq, are limited by the scope
    of the method in which they are created, therefore there is no way to
    access p and q once an N-key has been generated.

Encrypt('string',[n],[e]) 
    Method encrypts a plaintext passed in through the first parameter. Numeric
    N and e keys may be manually specified allowing the use of someone else's
    keys. If no keys are specified, the method uses the RSA user's own keys.
    The string passed to the method can be any string literal, and character
    encoding/decoding is done using the python ord() and unichr() functions
    which provides support for unicode chracters. The numeric conversion of
    each character is first padded to a fixed length, and a combination
    of the substrings is then ciphered using the RSA encryption algorithm.
    Given the various steps taken to convert and pad characters prior to the
    actual RSA conversion, all encryption and decryption must be done using
    these two methods in order to receive valid in- and output.

Decrypt('string',[n][d])
    Method decrypts a numeric ciphertext passed in through the first parameter
    in the method header. Numeric N and d keys may be manually specified
    allowing decryption using someone else's keys. If no keys are specified
    the method automatically used the user's own keys.
    The cipthertext is first tested for validity. The string must be numeric
    and of length >= 1 else the test fails the method returns with an error
    message. The function then proceeds with decrypting the message using the
    RSA decryption algorithm. The output is analyzed in fixed length
    sections and converted back to plaintext using the python unichr()
    function. 

Name(['name'])
    Name accessor returns or sets RSA user's name. If no parameter is given,
    the method returns current value, else the method changes the name to
    the value passed in as the parameter.

GetD_demo()
    For the purposes of this implementation (since it is a demonstration of
    the RSA protocol), there may arise an instance where knowing the d key
    should be crucial to verifying the program works as intended. This method
    is included in the demonstration in order to address that need. The method
    returns the integer value of the secret d key.

This implementation does not provide ways for secure d key exchange. Further,
it provides easy access to the d key for demonstrational purposes. Therefore
this implementation is purely an educational project, and designed to
demonstrate the functioning and capabilities of the RSA protocol. For secure
and trustworthy solutions please refer to a professional implementation.

-------------------------------------------------------------------------------
REFERENCES
-------------------------------------------------------------------------------

Table 1. Random execution time testing of the GetPrime-method

Each row represents the mean of 20 iterations of the method (400 iterations
total) 'Repetitions' is the amount of times a number had to be generated before
primality test returned true.

#       Exectime (s)  Repetitions   Exectime/rep (ms)
------------------------------------------------------
001.    0.6006150642           95        50.935848582
002.    0.7965420116          124       57.5599621137
003.    1.2333595157          191       51.7663604653
004.    0.7481707941          116       60.9668505515
005.    0.9325215391          143       59.2718414844
006.    0.8612143722          133       60.6473641904
007.    0.9997084371          153       61.4844335782
008.    0.8770274399          141       59.2744995215
009.    0.6553409546          103       62.7448162966
010.    0.4193374682           57       44.5510388797
011.    0.8902286708          130       60.0397416913
012.    1.0558113671          164       63.6153347511
013.     0.838016141          141       54.6977183398
014.    1.0562552503          163        58.524622637
015.    0.6999271171          115       48.2875143366
016.    0.5382104953           88       53.8704194084
017.    0.5344663707           86       55.1727622449
018.    0.7171375831          113       38.8317149683
019.    0.5988558392           97        45.624233876
020.    0.9489494754          153       52.5895431668
------------------------------------------------------
        0.8000847953          125       55.0228310542


Table 2. Encryption-Decryption Accuracy and Time Testing

#        string length      Input == Output           Exectime (s)
------------------------------------------------------------------
001.           62                  1                  0.1161044211
002.           38                  1                  0.1147022177
003.           51                  1                  0.1184059007
004.           66                  1                  0.1155992591
005.           56                  1                  0.1062448579
006.           19                  1                  0.0612811824
007.           12                  1                  3.5603043823
008.           31                  1                   2.910699195
009.           15                  1                  1.9561944325
010.           18                  1                   1.008381163
011.           36                  1                    2.19031064
012.          207                  1                  0.5514848256
013.          206                  1                   3.043625377
014.          161                  1                  1.0224251267
015.          958                  1                 64.4831130074
016.          359                  1                 42.1668514434
017.          461                  1                 58.2713564154
------------------------------------------------------------------

All strings encrypted using different keys
Overall accuracy: 100.0 %

Both tests are repeatable through RSA_exectest.py 
 
-------------------------------------------------------------------------------
GENERAL COMMENTARY REGARDING THIS RSA PROJECT
-------------------------------------------------------------------------------

When starting this project, the very first problem I had was the question
of very large primes: how to determine if a very large integer is indeed
a prime number? During the research phase I first came across the Fermat
primality test, but soon determined it was insufficient to meet the needs
of this project because of the possibility of Carmichael numbers that could
test as false positives. My second option, and ultimately what I decided
to use, was the Miller-Rabin primality test. Based on my research it seemed
relatively fast and sufficiently accurate to meet the requirements of this
project.

The Miller-Rabin primality testing and RSA encryption and decryption
algorithms all require modular exponentiation. Python pow() function was
very useful and fast for the purposes of handling modular exponentiation of
very large integers. I used it in each case.

When creating very large integers for primality testing, I used two random
values: first the current datetime value in microseconds, and a random number
generated using the python random library within a given range: 1 * 10^79 -
1 * 10^99. The sum of these two numbers is multiplied by two, and 1 is added to
the product, resulting in an odd integer of 80-100 digits. The final N-key is
the product of two of such large integers that have been determined to be
prime based on the Miller-Rabin test.

Once I had established methods for creating very large primes, the rest of
the algorithm was fairly easy to implement. I decided to build a class
implementation, because it seemed logical to have the various keys and
different methods grouped within a single unifying object. Then it would be
easy to pass the keys from one method to the next while maintaining them
under a single object. Also it allowed clearly defining what each user should 
or should not be able to do. Similar to the prime generation script, which 
is in its own file, I separated the encryption and decryption code from the 
main RSA class. The reasoning was to keep the class itself fairly clean and 
simple in terms of code, but also because I think each of the three parts 
warrants careful consideration in their own right. 

With the encryption (and decryption being the reverse function of the
encryption) I decided it would be likely that a user would want to encrypt
a string with alphanumeric characters. I made this possible, and set the 
encoding to unicode to allow maximum flexibility for user input. The
conversion is done using pythong ord() and unichr() methods. The length of
the input is not limited but does slow down the process in relation to the
length of the input string. The longest string I successfully tested was
3,334 characters in length. See reference Table 2 for more testing values. 

I padded each converted character to 6 digits, with each numeric value
starting with 1 and filled with zeros until whatever value is given by
the ord() function. I decided on this scheme because a fixed length would
help me to decode the values during the decryption. The preceding 1 and 0
-combination is more complex than just using a single digit for padding.
After converting each character, I joined the list of numeric values into a
long string. If the string length was still less than length of N [because
then we also know its value is < N] I would encrypt directly using the RSA
encryption protocol. Longer strings are split into equal size sequences
depending on length of input and N-key. Each substring is then encrypted
in sections, and the final output is a concatenation of the encrypted
substrings. The decryption functions the same way but in reverse.

Last, during the program testing phase, I decided to add the method for
displaying the d-key since this is a demonstrational project only. If this
was a real implementation I would try hard to keep the d key very well
hidden and design a way for secure key exchange. One option is of course
the Diffie-Hellman algorithm. Another practical way would be to use some
other encryption protocol for encrypting a message, and then used RSA for
encrypting the secret key alone. In this particular implementation, with
alphanumeric strings the process of encrypting and decrypting messages
requires multiple additional steps which slows down the process.
