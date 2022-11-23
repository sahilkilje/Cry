def cryptanalysis():
  cipher_text=input('Enter the cipher text:')
  for k in range(26):
    plain_text=''
    for letter in cipher_text:
      c=ord(letter)-65
      e=(c-k)%26
      plain_text+=chr(e+65)
    print('With key = ',k,plain_text)
cryptanalysis()
