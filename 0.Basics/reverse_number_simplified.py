'''Reversing a number simplified approach'''
if __name__=="__main__":
    x=int(input("Enter the value of x : "))
    ans=0
    while x:
        r=x%10
        ans=ans*10 + r
        x//=10
    print(ans)