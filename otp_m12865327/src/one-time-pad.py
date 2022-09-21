#Aidan Sorensen
#One-time pad
# Project 1, 9/18/2022

import random
import os

def KeyGen(lamed):
    """
    awooga
    given param, output a secret key sk. where the number of bits in sk is the param. also,
    write secret key to file.

    Args:
        lamed (lambda: int): bit length for key
    """  
    print(f"you selected {lamed} for your bit length")
    newkey = ""
    for i in range(lamed):
        temp = str(random.randint(0, 1))
        newkey += temp

    # write key to file named data/newkey.txt
    save_path = ""
    with open('C:\\Users\\Aidan\\OneDrive - University of Cincinnati\\otp_m12865327\\data', 'w') as fp:
        fp.write(newkey)
    #f = open ("data/key.txt", "x")
    #f.write(newkey)
    #f.close

    print(f"saved key, {newkey}, to  key.txt in /data folder")
    # next step

    pass

def Enc(message, key):
    """
    For the encryption function, given a plaintext m and a secret key sk, 
    your program needss to compute:
    - a ciphertext of this plaintext c ←m ⊕sk, 
    - print it in the terminal, 
    - and write this ciphertext to a file.
    """    
    pass

def Dec(c, key):
    """
    For the decryption function, given a ciphertext c and a secret key sk, your program need to 
    output the plaintext of this ciphertext m ←c ⊕sk, print it in the terminal, and write this
    plaintext to a file.
    """    
    pass


def main():
    userInput = input("please input lambda for key generation( 1 < x < 128, pref 32): ")
    KeyGen(int(userInput))

if __name__ == "__main__":
    main()
   