s="bonjour"
#slice=s[2:5]  #récupérer une tranch de s ,allant de caractére de pos 2 jusqu'a caractére de postion 5-1
#print(slice)

#slice2=s[0:] #pour avoir une copie de s

#ou 
slice3=s[::1]
#print(slice3)


#syntaxe générale 
#nomChaine[start:end:step]  #step par défaut égal à 1

#slice4=s[5:1:-1]   # de 5 A 1-pas #de 5 a 1 -(-1) # de 5 a 2
#print(slice4)


slice5=s[::-1]
print(slice5)

