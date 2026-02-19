## An Email slicer is a very useful program for separating the username and domain name of an email address.

user_email = input("Enter your email address: ")

username = user_email.split("@")[0]
domain_name = user_email.split("@")[1]

print("Username is:", username)
print("Domain name is:", domain_name)
