'''Given a 2-d matrix m*n , Given Q queries , each
   query has 4 integers : (i1, j1) top left and (i2,j2) bottom right.
   find the sum of the elements within this subarray of the query.
'''

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

    #store the prefix sum of all the submatrix whose bottom right is i,j
    # do the prefix sum row wise and then do it column wise.
    # Now given i1,j1 and i2,j2 , the sum is Arr[i2][j2]-Arr[i2][j1-1]-Arr[i1-1][j2] + Arr[i1-1][j1-1]

    # precomputation
    for i in range(r):
        sum_=array_2d[i][j]
        for j in range(1,c):
            sum_+=array_2d[i][j]
            array_2d[i][j]=sum_
    print(f"prefix arrow summed array : {array_2d}")
    for j in range(c):
        sum_=array_2d[i][j]
        for i in range(1,r):
            sum_+=array_2d[i][j]
            array_2d[i][j]=sum_
    print(f"prefix sum array : {array_2d}")

    Q=int(input("Enter the number of queries : "))
    queries_list=[]
    for q in range(Q):
        (i1,j1),(i2,j2)=tuple(map(int,input("enter the query coordinate 1: ").split(","))),tuple(map(int,input("enter the query coordinate 2: ").split(",")))
        ans=array_2d[i2][j2]-array_2d[i2][j1-1]-array_2d[i1-1][j2] + array_2d[i1-1][j1-1]
        print(f" sum for coordinates {(i1,j1)} and {(i2,j2)} is:  {ans}")

