# it-security


## The assignment for crypt:

Assignment description:

The shadow file of a Linux operating system contains the following line:
“$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0”

You’re asked to crack the given hash, knowing that the password is in a 3-digit format. You’re encouraged to solve this exercise using Python. 
Once you’re done, and if you want, you can use a password-cracking tool like John the Ripper to confirm the result.



## The assignment for nslookup:

The first draft of the code was not safe. It could be hacked by, when asked for a domain name, giving it a domain name AND a command. 

E.g.: www.kea.dk & dir

This would give us the domain information + the ls information. 
The assignment is to solve this issue through whitelist, blacklist or other methods. 
