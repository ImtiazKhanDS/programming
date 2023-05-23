'''print pattern of digits
   370987
   37098
   3709
   370
   37
   3
'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    while x>0:
        print(x)
        x=x//10
    