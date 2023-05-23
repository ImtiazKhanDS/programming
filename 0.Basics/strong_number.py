'''strong number
   145
'''
def factorial(n):
    if n==1 or n==0: return 1
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
if __name__=="__main__":
    x=int(input("enter x value : "))
    y=x
    sum_=0
    while x>0:
        d=x%10
        x=x//10
        sum_+=factorial(d)
    print(sum_)
    if sum_==y:
        print("strong number")
    else:
        print("not a strong number")