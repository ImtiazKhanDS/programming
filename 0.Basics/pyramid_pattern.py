'''print pyramid
   *
  * *
 * * *
 * * * *
'''
if __name__=="__main__":
    x=int(input("enter x value : "))
    for i in range(1,x+1):
        print(' '*(x-i),end='')
        for j in range(i):
            print('*', end=' ')
        print(end='\n')