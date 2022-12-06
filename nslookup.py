import subprocess
import re
# re = a module we import which contains regular and special expressions

domain_name = input("Enter the domain name: ")

regex = re.match('^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$', domain_name)
# Here we whitelist the characters that are allowed. Note: the space character isn't allowed. This will prevent a domain followed by a malicous command

command = "nslookup {}".format(domain_name)

# Here we put the whitelist in an if-statement to prevent any other outcomes than a domain or an error-message
if (regex):
    response = subprocess.check_output(command, shell=False, encoding="UTF-8")
    print(response)
else:
    print("Not a domain name")


#=====================================¨


"""
 # Can also be solved with shell=False
 # In that case line 14-15 would look like this:

response = subprocess.check_output(command, shell=False, encoding="UTF-8")
print(response)


"""