'''find the lcm of two variables.'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    y=int(input("enter y value : "))
    # lcm can never be greater than product of two values x,y
    # max(x,y)<=lcm(x,y)<=x*y
    prod_=x*y
    init_=max(x,y)
    lcm_=-1
    for i in range(init_,prod_+1):
        if i%x==0 and i%y==0 and lcm_==-1:
            lcm_=i
    print(lcm_)
