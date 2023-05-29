'''Given a 2-d matrix m*n , find sum of all its submatrices'''

if __name__=="__main__":
    r=int(input("enter the number of rows in the matrix : "))
    c=int(input("enter the number of columns in the matrix"))
    
    array_2d=[]
    for i in range(r):
        array=[]
        for j in range(c):
            temp=int(input("enter next element in the array : "))
            array.append(temp)
        array_2d.append(array)
    print(f"2d array  : {array_2d}")


    # top left and bottom right we can uniquely determine a matrix
    # i1, j1 for top left
    # bottom right i2 , j2 must follow the constraint i2>=i1 and j2>=j1
    # considering any cell i,j , the number of choices for top left (i+1)*(j+1)
    # the number of choices for bottom right (N-i)*(N-j)
    # total submatrices which contain the cell i, j : (i+1)(j+1)*(N-i)*(N-j)*a[i][j]
    overall_contribution=0
    for i in range(r):
        for j in range(c):
            overall_contribution+=array_2d[i][j]*(i+1)*(j+1)*(r-i)*(c-j)
    print(f"sum of all submatrices : {overall_contribution}")


