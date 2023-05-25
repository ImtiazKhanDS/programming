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
    prefix_sum=[0]*n
    prefix_sum[0]=array[0]
    
    for i in range(1,n):
        prefix_sum[i]=prefix_sum[i-1]+array[i]
    print(f"prefix sum array  : {prefix_sum}")

    q=int(input('input the number of queries : '))
    for j in range(q):
        l,r=int(input('input l value : ')),int(input('input r value : '))
        if l==0:
            print(prefix_sum[r])
        else:
            print(prefix_sum[r]-prefix_sum[l-1])
