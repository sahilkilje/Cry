#AFFINE CIPHER

def encrypt_words():
    plain_text=input('Enter the plain text to be encrypted:')
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    cipher_text=''
    for i in plain_text:
        if i.isupper():
            x=ord(i)-65
            enc_val=(a*x+b)%26
            cipher_text+=' '+chr(enc_val+65)
        else:
            x=ord(i)-97
            enc_val=(a*x+b)%26
            cipher_text+=' '+chr(enc_val+97)
    print(cipher_text)

def decrypt_words():
    cipher_text=input('Enter the cipher text to be decrypted:')
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    c=0
    for i in range(1,27):
        if (a*i)%26==1:
            c=i
    plain_text=''
    for i in cipher_text:
        if i.isupper():
            y=ord(i)-65
            enc_val=(c*(y-b))%26
            plain_text+=' '+chr(enc_val+65)
        else:
            y=ord(i)-97
            enc_val=(c*(y-b))%26
            plain_text+=' '+chr(enc_val+97)
    print(plain_text)
    
encrypt_words()          
decrypt_words()
