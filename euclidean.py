#euclidean

a=int(input("Enter first Number : "))
b=int(input("Enter second Number to : "))

if a>b:
    while(b!=0):
        q=a/b
        remainder=a%b
        a=b
        b=remainder
        print("Value of a : ",a)
        print("Value of b : ",b)
        print("Value of q : ",q)
        print("Value of r : ",remainder)
        if b==0:
            print("GCD of two Numbers :",a)
            break
else:
    temp=a
    a=b
    b=temp
    while(b!=0):
        q=a/b
        remainder=a%b
        a=b
        b=remainder
        print("Value of a : ",a)
        print("Value of b : ",b)
        print("Value of q : ",q)
        print("Value of r : ",remainder)
        if b==0:
            print("GCD of two Numbers is :",a)
            break
            
            
