'''Given an array of n numbers and  also given p, q, r numbers
   maximize this expression p*arr[i]+q*arr[j]* r*arr[k]
   i<j<k
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    p=int(input("enter p value : "))
    q=int(input("enter q value : "))
    r=int(input("enter r value : "))
    prefix_max=[0]*n
    prefix_max[0]=array[0]*p
    for i in range(1,n):
        prefix_max[i]=max(prefix_max[i-1],array[i]*p)
    
    print(f"prefix max : {prefix_max}")
    suffix_max=[0]*n
    suffix_max[n-1]=r*array[n-1]
    for i in range(n-2,-1,-1):
        suffix_max[i]=max(suffix_max[i+1],array[i]*r)
    print(f"suffix max : {suffix_max}")

    result=float('-inf')
    for k in range(1,n-1):
        result=max(result,prefix_max[k-1]+q*array[k]+suffix_max[k+1])
    print(result)



    
