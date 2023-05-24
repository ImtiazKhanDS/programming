'''Generate fibonacci numbers'''
if __name__=="__main__":
    n=int(input("enter x value : "))
    #t0=0, t1=1 ; t(i)=t(i-1)+t(i-2)
    prev=0;curr=1
    if n==0:
        print(0)
    else:
        for i in range(2,n+1):
            result=prev + curr
            prev=curr
            curr=result
        print(curr)

