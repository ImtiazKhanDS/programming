
'''Given an array do selection sort
  step 1 : find smallest
  step 2 : swap the smallest element in the first place.
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    for i in range(n):
       minm=array[i]
       for j in range(i+1,n):
           if array[j]<minm:
               minm=array[j]
               idx=j
       temp=array[idx]
       array[idx]=array[i]
       array[i]=temp

    print(f"Sorted Array : {array}")

