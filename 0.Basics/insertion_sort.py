
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

    for j in range(n):
        i=j
        while i>0 and (array[i]<array[i-1]):
            tmp=array[i]
            array[i]=array[i-1]
            array[i-1]=tmp
            i-=1
    print(f"sorted array after insertion sort {array}")
