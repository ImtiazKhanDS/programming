'''Program to count frequency of an element in an array 
  example =[1,2,3,3,5,6],3 -> 1:1,2:1,3:2,5:1,6:1
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    for j in range(n):
        count=0
        for i in range(n):
            if array[i]==array[j]:
                count+=1
        print(f"The count of the element {array[j]} : {count}")