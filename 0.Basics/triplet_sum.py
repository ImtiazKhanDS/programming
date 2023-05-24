
'''Given an array, and an int x , all the pairs that have sum=x'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    sum_triplet=int(input("enter the desired sum pair : "))

    for j in range(n):
        for i in range(j+1,n):
            for k in range(i+1,n):
                if array[i]+array[j]+array[k]==sum_triplet:
                    print(f"pairs with desired sum are {array[i]} , {array[j]} and {array[k]}")
        
    
