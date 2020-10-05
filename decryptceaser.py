import nltk
from nltk.corpus import words
s=list(map(str,input("Enter Text to be decrypted seperated by space:\n").split()))
a =[x.lower() for x in s] 

str1=''.join(a) 
letter = []

if (str1 in words.words()):
       print('Already Decrypted :',''.join(s))
      
else :
   
      for i in range(1,27):
        str1 = ''
        letter.clear()
        a.clear()
        for j in s:
         #print(letter)
         
         if (ord(j)+i>90 and j.isupper()):
           letter.append(chr(64+i-(90-ord(j))))
         
         elif (ord(j)+i>122 and j.islower()):
           letter.append(chr(96+i-(122-ord(j))))
        
         else :
           letter.append(chr(ord(j)+i))
         
        a=[x.lower() for x in letter] 
        str1=''.join(a)   
        
        if (str1 in words.words()):
            
            print("Decrypted Text is :",''.join(letter))
            break
        elif(i==26):
            print('Wrong Input')
           
           