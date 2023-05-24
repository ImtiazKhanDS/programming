'''Given a number N and x give the sum of the x^0/0! + x/1! + x^2/2! and so on till x^n/n!'''
if __name__=="__main__":
    n=int(input("enter n value : "))
    x=int(input("enter x value : "))
    ans=0;prod=1;fact=1
    for i in range(0,n+1):
        ans+=prod/fact
        prod*=x
        fact*=(i+1)
    print(ans)

        