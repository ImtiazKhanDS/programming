'''calculate the sum of the digits in a number'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    s=0
    while x>0:
        s+=x%10
        x=x//10
    print(s)