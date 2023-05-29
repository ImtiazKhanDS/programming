'''Given a 2-d matrix n*n , given a key k search for the element 
   and give the coordinates of that element in the matrix.
   Each row of the matrix is sorted and each column of the matrix is sorted.
'''

if __name__=="__main__":
    r=int(input("enter the number of rows in the matrix : "))
    c=int(input("enter the number of columns in the matrix : "))
    
    array_2d=[]
    for i in range(r):
        array=[]
        for j in range(c):
            temp=int(input("enter next element in the array : "))
            array.append(temp)
        array_2d.append(array)
    print(f"2d array  : {array_2d}")
    key=int(input("Enter the key to search : "))

    j=c-1
    i=0
    while i<r and j>=0:
        if array_2d[i][j]==key:
            print(f"The coordinates of the search term is at {(i,j)}")
            break
        elif array_2d[i][j]>key:
            j-=1
        else:
            i+=1
    

