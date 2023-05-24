# 1,11,111,1111, ....
#N=3
# Sum of first N terms.
if __name__=="__main__":
    n=int(input("enter x value : "))
    result=0; t=1
    for i in range(1,n+1):
        result+=t
        t=t*10+1
    print(result)