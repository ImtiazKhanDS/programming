'''Program to find insert an element in an array 
  example =[1,2,3,4,5,6],3,8 -> [1,2,3,8,4,5,6]
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    index,value=int(input("enter the value of index : ")),int(input("enter the value to be inserted : "))
    array.append(None)
    print(array)
    for i in range(n-1,index,-1):
        array[i+1]=array[i]
    array[index]=value
    print(array)