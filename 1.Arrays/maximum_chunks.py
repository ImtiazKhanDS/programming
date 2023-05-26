'''Given an integer array , which is a permutation of numbers from 0 to N-1
   1.split it into multiple chunks
   2.sort the chunks individually
   3.concatenate the sorted chunks.
   The concatenated array should be sorted.
   What is the maximum chunks the array can be split into ?
   Example : [1,2,0,4,3,5] maximum chunks : 
   [1,2,0,4,3,5]
   [1,2,2,4,4,5]
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    # Get the prefix max , if prefix max at index i is i then we can make that as a chunk.
    cmax=float('-inf')
    ans=0
    for i in range(n):
        cmax=max(cmax,array[i]) 
        if i==cmax:
            ans+=1
    print(f"maximum number of chunks : {ans}")
