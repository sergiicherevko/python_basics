#get user email

email = input("What is your email?: ").strip()

# slice out user name

username = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1:]

# format message

output = "Your username is {} and your domain is {}".format(username, domain)

# display output message

print(output)