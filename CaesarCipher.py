import string

#decode
def decoder(message, offset):
    alpha = string.ascii_lowercase
    new = ""
    chars = ["!", " ", "," , "?", ".", "'"]
    for letter in message:
        if letter in chars:
            new = new + letter
        else:
            shift = (alpha.find(letter) + offset) % 26
            new = new + alpha[shift]
    print(new)
    
#encode    
def coder(message, offset):
    alpha = string.ascii_lowercase
    new = ""
    chars = ["!", " ", "," , "?", ".", "'"]
    for letter in message:
        if letter in chars:
            new = new + letter
        else:
            shift = (alpha.find(letter) - offset) % 26
            new = new + alpha[shift]
    print(new)

#brute force
for i in range(1,27):
    print("offset: " + str(i))
    print(decoder(message, i))
