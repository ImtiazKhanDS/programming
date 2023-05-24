'''Program to reverse an array in place 
  example =[1,2,3,4,5,6] -> output=[6,5,4,3,2,1]
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)

    print("original array : " , array)
    i=0; j=n-1
    while i<j:
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
        i+=1
        j-=1
    print("reversed inplace array : " , array)

    