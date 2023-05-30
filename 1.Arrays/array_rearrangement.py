'''Given an integer array of n elements, Arr[n] E {0,...N-1} permutation
   change this array into some other array if arr[i]==j => output arr[j]=i
   i/p : 1 3 0 2
   o/p : 2 0 3 1


'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")
    # using a temporary array 
    '''
    for i=0 to n:
      tmp[arr[i]]=i
    
    O(n), O(n)

    can we solve this without using the temporary array ?
    instead of storing x , store -(x+1)
    '''

    for i in range(n):
      if array[i]>=0:
         index=array[i]
         value=i
         # whenever the value corresponds to the index 
         # of the starting point we have to execute
         while (index!=i):
            temp=array[index] # store the next index in temp
            array[index]=-(value+1) 
            value=index # assign the current index as the value
            index=temp # assign the temp to index.
         array[index]=-(value+1) # the last value is discared so we write it here.
    
    for i in range(n):
       array[i]=-1*array[i]-1 # change to original number.

    print(f"re-arranged array : {array}")   