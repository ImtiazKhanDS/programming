'''Given an integer array , and integer k , print the sum of 
   every subarray (contiguos chunk).
   example : 1 2 -1 0 4
   k=3
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")
    #sliding window technique.
    k=int(input("input the window size : "))
    sum_=0
    for i in range(k):
        sum_+=array[i]
    for j in range(k,n,1):
        print(sum_)
        sum_+=array[j] # add the current element
        sum_-=array[j-k] # remove the last window first element.
    print(sum_)
    



