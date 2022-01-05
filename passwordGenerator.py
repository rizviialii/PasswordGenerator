import random
def passwordGenerator(length):
    letters = "abcdefghijklmnopqrstuvwxyz" 
    numbers = "0123456789"
    symbols = "!@#$%^&*()"
    
    all = letters.upper() + letters + numbers + symbols
    password = "".join(random.sample(all,length))
    #return password
    return password

#driver code
print(passwordGenerator(4))


