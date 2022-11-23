#VIGNERE CIPHER
def key_matching(PT,key):
 key = list(key)
 if len(key) == len(PT):
   return key
 else:
   for i in range(len(PT) - len(key)):
     key.append(key[i % len(key)])
   return ("" . join(key))
def encrypt(PT,key):
 en_text = []
 for i in range(len(PT)):
   x = (ord(PT[i]) +ord(key[i])) % 26
   x += ord('A')
   en_text.append(chr(x))
 return("" . join(en_text))

def decrypt(CT,key):
 en_text = []
 for i in range(len(CT)):
   x = (ord(CT[i]) - ord(key[i])+26) % 26
   x += ord('A')
   en_text.append(chr(x))
 return("" . join(en_text))
plain_text = input("Enter Plain Text:  ")
key_value = input("Enter Key:  ")
key = key_matching(plain_text, key_value) 
print("Cipher Text:  " + encrypt(plain_text,key))
Cipher_text = encrypt(plain_text,key)
print("Decryption Text:  " + decrypt(Cipher_text,key))
