"""
Assignment description:

The shadow file of a Linux operating system contains the following line:
“$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1
XHmSID/5VkeFiEaSA2b0”
You’re asked to crack the given hash, knowing that the password is in a 3-digit format. You’re encouraged to
solve this exercise using Python. Once you’re done, and if you want, you can use a password-cracking tool like
John the Ripper to confirm the result.
"""

import hashlib
from passlib.hash import sha512_crypt

#Checking in a range of 1000 to check from 000 to 999           - line 23
#Then adding 00 to the number for the first 9 numbers (0-9)     - line 24
#Then adding 0 to the number for the next 90 number (10-99)     - line 26
#This is since we know the password is in a 3-digit format
#Then checking if it matches the hashed version of the password - line 31
#We break the loop if there is a match                          - line 33
#The match is 479

for x in range(1000):
    if x < 10:
        x = "00" + str(x)
    elif (x > 9 and x < 100):
        x = "0" + str(x)
    
    pw = sha512_crypt.using(salt="penguins", rounds=5000).hash(str(x))
    if pw == "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0":
        print(x)
        break
    
    print(x)


#============================================================
# second version with itertools:


def count(start=0, step=1):
    print("Working ...")
    n = start
    while True:
        pw = sha512_crypt.using(salt="penguins", rounds=5000).hash(str(n))
        if pw == "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0":
            return n
        else:
            n += step 
    
print(count())