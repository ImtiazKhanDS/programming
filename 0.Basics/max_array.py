'''Program to find max of an array in place 
  example =[1,2,3,4,5,6] -> 6
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)

    maxm=array[0]
    for i in range(1,n):
        if array[i]>maxm:
            maxm=array[i]

    print(maxm)