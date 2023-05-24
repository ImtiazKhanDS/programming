'''Given an integer N reverse the number 
   example : 45123
   output : 32154
'''

if __name__=="__main__":
    N=int(input("Enter the value of N : "))
    temp=N;d=0
    while temp:
        d+=1
        temp//=10
    
    ans=0
    while N:
        r=N%10
        ans+=r* 10**(d-1)
        d=d-1
        N//=10
    print(ans)

