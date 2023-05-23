'''gets factorial of a number'''
if __name__=="__main__":
    result=1
    x=int(input("enter x value : "))
    for i in range(1,x+1):
        result*=i
    print(result)