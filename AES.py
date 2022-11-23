from Crypto.Cipher import AES
import binascii, os
text_file = open("/content/demo_textfile.txt", "r")
text = text_file.read()
print(f"The contents of text file are \n{text}")
msg = bytes(text, encoding='utf-8')

#secret key
secretKey = os.urandom(32)

#Encryption
aesCipher = AES.new(secretKey, AES.MODE_GCM)
ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
encryptedMsg = ciphertext, aesCipher.nonce, authTag

#Decryption
(ciphertext, nonce, authTag) = encryptedMsg
aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
ct = binascii.hexlify(encryptedMsg[0]).decode('utf-8')

pt = plaintext.decode('utf-8')

#Print data in new file 
file_text = open("Decryption_file.txt","w+")
text2 = file_text.write("Encrypted Data:-\n")
text2 = file_text.write(str(encryptedMsg))
text2 = file_text.write("\nDecryption or Plaintext:-\n")
text2 = file_text.write(pt)
file_text.close()
