'''Program to delete an element in an array 
  example =[1,2,3,4,5,6],3 -> [1,2,4,5,6]
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    index=int(input("enter the value of index : "))
    print(array)
    for i in range(index+1,n):
        array[i-1]=array[i]
    array[n-1]=None
    print(array)