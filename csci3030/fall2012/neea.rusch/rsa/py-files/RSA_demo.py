#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RSA as r
import random
import sys
 
def RSA_demo():
    """ RSA demo """
    
    users = []

    print "Welcome to RSA demo"
    sn = raw_input("Enter your name: ") 

    if len(sn) == 0:
        sn = "Anonymous"
        
    users.append(r.RSA(sn)) 

    print '\nGood news {} - you are now ready to use RSA'.format(users[0].Name())
    z = raw_input('Would you like to see your public keys? (Y/N): ') 

    if z.upper() == 'Y':
        print '\nYour n key is:\n{}'.format(str(users[0].GetPubKeys('n')))
        raw_input('\nYour e key is:\n{}'.format(str(users[0].GetPubKeys('e'))))
 
    print('\nBut RSA is no fun if you have no friends!')
    raw_input("We'll invite your friend to join us - hit any key to begin")
 
    friend_names = ['Wolfgang', 'Klaus', 'Ulf', 'Bruno', 'Georg',
                    'Waldemar', 'Horst', 'Jurgen', 'Karl-Heinz', 
                    'Heinrich', 'Friedman', 'Yngve', 'Rolf', 'Ingmar']
 
    x = random.randrange(0, len(friend_names))
    fn = friend_names[x]
 
    users.append(r.RSA(fn))

    some_messages = [u"Meet me @ Ristorante Pizzeria Mamma Mia 1800 tonight. Don't be late!!",
                     u"I have some J\xe4germeister if you want to come over to my house",
                     u"Ozturk told me you refuse to pay. I will bring my little\nfriend over to see you.",
                     u"Gertrude told me your secret! I know it all! Hahahaha!",
                     u"My email address is: <" + fn + "_123@ichLiebeLederhosen.de>.\nDon't give it to anyone else.",
                     u"Long time no see, ... Well if you think I forgot about that\n\xa280 you owe me, you are wrong!!!",
                     u"This is my address: 4330 Deans Bridge Rd. Come over anytime.",
                     u"I heard you and Manfred had a good time last night..!! :D",
                     u"I'm coming over to your house with pizza, what do you want on it??",
                     u"OMG that guy H\xe5kan is such an idiot, LOL... He told me his\npassword is UppY0uR$" + fn[0:2].upper() + fn[2:].lower() + "! I'm going to hack his account, hahaha!",
                     u"I saw your buddy on augustacrime.com, some friend you got. Hahahaha!",
                     u"Gudrun and Ulrike said they saw you last night with *you-know-who*.\nMust have been fun, LOL!"]
 
    raw_input('\nYour friend {} is now using RSA too!'.format(users[1].Name()))
 
    x = random.randrange(0, len(some_messages))
    OGmsg = u"Hey {},\n{}\n\nYour Friend, {}\n\n".format(
        users[0].Name(), some_messages[x], users[1].Name())
 
    msg = users[1].Encrypt(OGmsg)
 
    print '\nNow {} has sent you a message'.format(users[1].Name())
    z = raw_input('Enter Y if you want to see the ciphertext: ')
 
    if z.upper() == 'Y':
        raw_input('\n{}'.format(msg))

        raw_input("\nHoly crap! ... that makes no sense.")
 
    k, p = 1, 0
    raw_input ("\nOK. Next let's pretend you are a Keith the spy\nand as Keith the spy you want to decrypt the secret message")

    print "\nHere are {}'s public keys:".format(users[1].Name())
    raw_input('n:  {}\n\ne:  {}'.format(str(users[1].GetPubKeys('n')), 
                                    str(users[1].GetPubKeys('e'))))

    while k > 0:
        k, p = raw_input("\nEnter d-key [or '0' to quit]: "), p + 1
        if k.isdigit() != True:
            print "You must enter integer. Try again"
            continue
        else:
            k = int(k)
            if k < 1:
                break            
            tmp = users[0].Decrypt(msg, users[1].GetPubKeys('n'), k)
            if tmp == OGmsg:
                print('Holy crap Keith, you cracked the encryption!')
                print('Stop messing with this program and call CIA, they are looking to hire you.')
                raw_input('Have a nice day and goodbye!!\n\n')
                return
            else:
                print('No, Keith! Your d-key is wrong.')
                if p > 1:
                    if p % 3 == 2:
                        print("Come on, give up already!")
                    if p % 3 == 1:
                        print("Hah! You'll never get it..")
                    if p % 3 == 0:
                        print("Geez..Why are you still trying?!")

    raw_input ("\nWise decision Keith!\nOK. You are back to being {} again.".format(users[0].Name()))
    print '\nNow {} has shared his private key with you'.format(users[1].Name())
    raw_input ("Let's try to decrypt the message again. Hit any key to continue.")

    msg = users[0].Decrypt(msg, users[1].GetPubKeys('n'), users[1].GetD_demo())

    raw_input(u"\nHere is {}'s secret message to you:\n\n{}".format(users[1].Name(), msg))
    print '\n{}'.format('-' * 60)
    print 'Congratulations! You have completed this RSA demo.'
    print 'To use this implementation, check out readme file for instructions'
    print 'and download the code files to test it yourself. Goodbye!'
    return
 
RSA_demo() 
