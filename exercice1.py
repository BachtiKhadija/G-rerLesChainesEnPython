message="bonjour le monde"

cryptedstr=""
#on peut parcourir une chaine en utilisant la boucle for 
for c in message:
    scii=ord(c)
    if(c.isupper()):
        newAscii=(scii-ord('A')+3)%26+ord('A')
    elif (c.islower()):
        newAscii=(scii-ord('a')+3)%26+ord('a')
    else:
        newAscii=scii
    cryptedstr=cryptedstr+chr(newAscii)
print("crypted message : {}".format(cryptedstr))
