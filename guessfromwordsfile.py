from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
# encrypted = "t0ed+TDTf4e1V3Vz94nAN+nj1uDgMPZnfd7BDyBoy/GeGk6LiImMBPPHvN8DcLgIhWo4ByqxpZby99nQpU8KuA=="
# encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

with open("words.txt", "r") as f:
    line = f.readline()
    while line:
        secret = line.strip()
        if (secret[-1:] == "\n"):
            print "Error, new line character at the end of the string. This will not match!"
        elif (len(secret) >= 32):
            print "Error, string too long. Must be less than 32 characters."
        else:

            if (decoded.startswith('FLAG:')):
                print "\n"
                print "Success: "+secret+"\n"
                print decoded+"\n"
            else:
                pass
                # print 'Wrong password'
        line = f.readline()        


