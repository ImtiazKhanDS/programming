'''Given an integer array , and integer k 
   find minimum number of swaps to bring
   elements<=k together.

   example : 2 7 9 5 8 7 4
   k : 5
   swap 7 and 5 and swap 9 and 4
   output : min swaps : 2
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")
    #sliding window technique.
    k=int(input("input the k value : "))
    # min swaps=count of legal elements - maximum count subarray with legal elements
    #count of legal elements:
    count_legal_elements=0
    for i in range(n):
        if array[i]<=k:
            count_legal_elements+=1
    #maximum count subarray with legal elements using sliding window technique.
    max_count=float('-inf')
    count_=0
    for i in range(k):
        if array[i]<=k: count_+=1
    for j in range(k,n):
        max_count=max(max_count,count_)
        count_+=1 if array[j]<=k else 0
        count_-=1 if array[j-k]<=k else 0
    max_count=max(max_count,count_)
    print(f"minimum swaps required : {count_legal_elements-max_count}")


    



