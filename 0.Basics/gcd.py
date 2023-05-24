'''find the gcd/hcf of two variables.'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    y=int(input("enter y value : "))
    # gcd can never be greater than mininum of two values x,y
    # 1<=gcd(x,y)<=min(x,y)
    min_=min(x,y)
    gcd_=1
    for i in range(1,min_):
        if x%i==0 and y%i==0:
            gcd_=i
    print(gcd_)

