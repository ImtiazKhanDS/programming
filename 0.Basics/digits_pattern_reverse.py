'''print pattern of digits
   370987

   3
   37
   370
   3709
   37098
   370987
'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    d=1
    while x//d>9:
        d=d*10
    while d>0:
        print(x//d)
        d=d//10
    