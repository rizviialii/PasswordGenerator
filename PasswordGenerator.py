import random

def passwordGenerator(length):
    #type of charaters present in password
    capitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallLetters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"
    #creating password
    all = capitalLetters + smallLetters + numbers + symbols
    password = "".join(random.sample(all,length))
    #return password
    return password

print(passwordGenerator(16))

