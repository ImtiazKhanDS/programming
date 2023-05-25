
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
    print(f"array before sorting : {array}")
    for  j in range(n):
        for  k in range(j+1,n):
            if array[j]>array[k]:
                temp=array[j]
                array[j]=array[k]
                array[k]=temp
    print(f"bubble sorted array : {array}")

