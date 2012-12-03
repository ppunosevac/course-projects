#/usr/local/bin/python
# -*- coding: utf-8 -*-

import fractions as f

def Encrypt(msg, n, e):
    """ encrypts plaintext """

    if len(msg) == 0:
        return
    
    if msg.isdigit() == False:
        msg = list( u"" + msg )

    # convert all chars to 6 digit numeric
    msg = map(lambda x: "1%05d" % ord(x), msg)
    tmp, output = ''.join(msg), ""
    c = len(str(n))

    if len(tmp)< c:

        # encrypt short strings without splitting
        output = str(pow(int(tmp), e, n))
        
    else:

        # find i where temp / i == 0 and i < len(n)
        m, i = len(tmp), c - 1
        while m % i != 0:
            i -= 1
            
        # split temp string
        output = split_len(tmp, i)

        # RSA encryption
        output = map(lambda x: pow(int(x), e, n), output)

        # find max string length of substrings
        sLen = max(map(lambda x: len(str(x)), output))

        # pad substrings to max length
        output = map(lambda x: str(x).zfill(sLen), output)

        # first 12 digits indicate split lenghts
        output = "1{}1{}{}".format(
            str(i).zfill(5), str(sLen).zfill(5), ''.join(output))

    return output

def Decrypt(msg, n, d):
    """ decrypts ciphertext """
    
    try:
        msg = int(msg)
    except:
        if msg.isdigit() == False or len(msg) == 0:
            print "input string is not numeric!"
            return

    c = len(str(n))

    if msg < n:

        # if msg < n, decrypt immediately 
        tmp = str(pow(msg, d, n))
        
    else:

        # get split sizes stored in front of msg
        tLen = int(str(msg)[1:6])
        sLen = int(str(msg)[7:12])

        # pop split size from msg
        msg = str(msg)[12:]

        # split msg by split size
        sqs = split_len(str(msg), sLen)

        # decrypt each substring
        sqs = map(lambda x: str(pow(int(x), d, n)).zfill(tLen), sqs)
        
        # join substrings to get temp string
        tmp = ''.join(sqs)
    
    # split temp string to substrings of size 6
    char_list = split_len(tmp, 6)    

    try:
        # pop leading 1 and any zeros from each substring
        char_list = map(lambda x: int(str(x)[1:]), char_list)

        # convert remaining integers to unicode chars
        char_list = map(lambda x: unichr(x), char_list)
        
    except:
        # return with error when unichr() fails
        return False

    # join chars into a string
    return u"" + ''.join(char_list)


def split_len(seq, length):
    """ split string by length """
    return [seq[i:i+length] for i in range(0, len(seq), length)]

