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
    prefix_max=[0]*n
    prefix_max[0]=array[0]
    
    for i in range(1,n):
        prefix_max[i]=max(prefix_max[i-1],array[i])
    print(f"prefix sum array  : {prefix_max}")

    q=int(input('input the number of queries : '))
    for j in range(q):
        k=int(input('input idx value : '))
        print(prefix_max[k])
