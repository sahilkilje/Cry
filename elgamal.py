pt=int(input("Enter plain text: "))
p=int(input("select large prime number p : "))
d=int(input("select private key D : "))
e1=int(input("select public key E1: "))
#key generation

e2=(e1**d)%p
print("public keys are : (",e1,e2,p,")")
print("private keys : ",p)

#encryption
r=int(input("Select random number r : "))
c1=(e1**r)%p
temp=e2**r
c2=(pt*temp)%p

print("Encryption : (",c1,c2,")")

#decryption

temp2=c1**d
d=2
while d<temp2:
    if((d*temp2)%p)==1:
        break
    else:
        d+=1
decryption=(c2*d)%p
print("decrypted message : ",decryption)
