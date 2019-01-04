import string

# encode
def enc_vigenere(message, keyword):
    alpha = string.ascii_lowercase
    chars = ["!", " ", "," , "?", ".", "'"]
    repkey = ''
    while (len(repkey) < len(message)):
        repkey += keyword
    finkey = repkey[:len(message)]
    output = ''
    for i in range(len(message)):
        if message[i] in chars:
            output = output + message[i]
        else:
            shift = (alpha.find(message[i]) + alpha.find(finkey[i])) % 26
            output = output + alpha[shift]
    print(output)

#decode
def dec_vigenere(message, keyword):
    alpha = string.ascii_lowercase
    chars = ["!", " ", "," , "?", ".", "'"]
    repkey = ''
    while (len(repkey) < len(message)):
        repkey += keyword
    finkey = repkey[:len(message)]
    output = ''
    for i in range(len(message)):
        if message[i] in chars:
            output = output + message[i]
        else:
            shift = (alpha.find(message[i]) - alpha.find(finkey[i])) % 26
            output = output + alpha[shift]
    print(output)
