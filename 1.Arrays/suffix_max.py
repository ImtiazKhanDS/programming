'''
Given an array A and q queries 
each query is has l and r.
for each query return the sum of the elements from l to r.
'''
if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array before sorting : {array}")

    # prefix sum is the sum till every index.
    suffix_max=[0]*n
    suffix_max[n-1]=array[n-1]
    
    for i in range(n-2,-1,-1):
        suffix_max[i]=max(suffix_max[i+1],array[i])
    print(f"suffix max array  : {suffix_max}")

    q=int(input('input the number of queries : '))
    for j in range(q):
        k=int(input('input idx value : '))
        print(suffix_max[k])
