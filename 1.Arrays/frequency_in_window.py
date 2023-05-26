'''Given an integer array , and integer k 
   find freq(x) in every window of size-k
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
    x=int(input("enter the value to measure frequency of : "))
    count_=0
    for i in range(k):
        count_+=1 if x==array[i] else 0
    for j in range(k,n,1):
        print(count_)
        count_+=1 if x==array[j] else 0 # add the current element
        count_-=1 if x==array[j-k] else 0 # remove the last window first element.
    print(count_)
    



