#to find whether a given username contains less than 10 characters or not
username = input("enter the username:")
if len(username)<10:
    print("username is valid")  
else:
    print("username is invalid")