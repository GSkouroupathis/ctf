# Problem is modified vigenere, this won't work
# check https://f00l.de/hacking/vigenere.php

f = open('da-message.txt')
ff = f.read()
key = 'topkek'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

deciphered=''
i = 0
for e in ff:
    if e != '\n':
        k = key[i % len(key)]
        eIndex = alphabet.index(e)
        kIndex = alphabet.index(k)
        d = alphabet[(eIndex + kIndex) % len(alphabet)]

        # replace letters with their opposites
        # to transform to modified viginere
        newalphabet = alphabet[eIndex:] + alphabet[:eIndex]
        if alphabet.index(d) > eIndex:
            d = newalphabet[ len(alphabet) - (alphabet.index(d) - eIndex) ]
        else:
            d = newalphabet[ - (alphabet.index(d) - eIndex) ]
        #d = alphabet[ (alphabet.index(d) - eIndex) ]
        i += 1
    else:
         d = '\n'
    deciphered += d
    
print deciphered
