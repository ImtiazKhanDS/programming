'''Given an integer array of size n , find sum of all its subarray'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    # all the subarrays will have a starting point and ending point
    # There are n subarrays whose starting point is 0, n-1 for point 1 and so on.
    # n(n+1)/2 subarrays.
    # 1 -1 2 0 3 4 
    #      -
    # for starting point i have 3 choices , for ending point i have 4 choices : 4 *2=8

    ans=0
    for i in range(n):
        ans+= array[i]*(i+1)*(n-i)
    print(f"sum of all subarrays : {ans}")
