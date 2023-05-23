'''check whether a number is prime or not'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    c=0
    for i in range(1, x+1):
        if x%i==0:
            c+=1
    if c==2:
        print("prime")
    else:
        print("not prime")