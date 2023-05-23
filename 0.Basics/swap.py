'''Swapping values without using a extra variable.'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    y=int(input("enter y value : "))
    print(f"Before swapping entered values x :{x}, y : {y}")
    x=x+y
    y=x-y
    x=x-y
    print(f"After swappingentered values x :{x}, y : {y}")