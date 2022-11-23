def encrypt(text,s):
   result = ""
   for i in range(len(text)):
       char = text[i]
       if(char.isupper()):
           result += chr((ord(char) + s - 65) % 26 + 65)
       else:
           result += chr((ord(char) + s - 97) % 26 + 97)
   return result

def decrypt(result,s):
   result1 = ""
   for i in range(len(text)):
       char = result[i]
       if(char.isupper()):
           result1 += chr((ord(char) - s - 65) % 26 + 65)
       else:
           result1 += chr((ord(char) - s - 97) % 26 + 97)
         
   return result1

text = input("Enter Text:   ")
s = int(input("Enter Key:   "))
print("Cipher:  " + encrypt(text,s))
ct=encrypt(text,s)
print("Decrypt:  " + decrypt(ct,s))
