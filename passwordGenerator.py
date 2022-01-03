import random
def passwordGenerator(length):
    #type of charaters present in password
    letters = "abcdefghijklmnopqrstuvwxyz" 
    numbers = "0123456789"
    symbols = "!@#$%^&*()"
    #creating password
    all = letters.upper() + letters + numbers + symbols
    password = "".join(random.sample(all,length))
    #return password
    return password

#driver code
print(passwordGenerator(4))


