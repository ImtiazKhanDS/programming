'''how many numbers are factor of a number'''
if __name__=="__main__":
    count=0
    x=int(input("enter x value : "))
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    print(f"number of factors of {x} is {count}")