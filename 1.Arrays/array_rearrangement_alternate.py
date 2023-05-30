'''Given an integer array of n elements, Arr[n] E {0,...N-1} permutation
   change this array into some other array if arr[i]==j => output arr[j]=i
   i/p : 1 3 0 2
   o/p : 2 0 3 1


'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")
    
    for i in range(n):
        old_value=array[i]%n
        array[old_value]=i*n + array[old_value]
    
    for i in range(n):
        array[i]=array[i]//n
    
    print(f"rearranged array : {array}")