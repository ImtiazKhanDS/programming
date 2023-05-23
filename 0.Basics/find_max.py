'''find the maximum of two variables.'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    y=int(input("enter y value : "))
    z=int(input("enter z value : "))
    if x>=y and x>=z:
        print(f"the maximum value is x: {x}")
    elif y>=z and y>=x:
        print(f"the maximum value is y: {y}")
    else:
        print(f"the maximum value is z: {z}")