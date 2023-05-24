'''Program to count frequency of an element in an array 
  example =[1,2,3,3,5,6],3 -> 2
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    x=int(input("enter the element you want frequency of : "))
    count=0
    for i in range(n):
        if array[i]==x:
            count+=1
    print(f"The count of the element {x} : {count}")
    
