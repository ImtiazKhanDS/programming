'''Given a 2-d matrix n*n , find the maximum consecutive difference between 2 elements.
   {3, 6, 9, 1}
        | sort
   {1, 3, 6, 9}
        | consecutive difference.
 max(2   3  3) -> 3
 o/p : 3 
 
 i/p : 20 25 27 33 65 70
 o/p : 32
 
 '''


if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    '''
    N=6, min=10, max=20
    (max-min)/N-1 = 2 (number of gaps , if there are n elements there will be n-1 gaps)
    so the answer is never smaller than 2 in this case.

    min = 20
    max=70
    N=6
    70-20/6-1 = 10
    20,30,40,50,60 70
    form buckets
    min     min+gap-1   min   max
    [20.....29]         20    27
    [30.....39]         33    33
    [40.....49]         X     X
    [50.....59]         X     X
    [60.....69]         65    65
    [70.....79]         70    70

    bucket number : (arr[i]-min)/gap
    '''
    #create two buckets maxm bucket and minm bucket.
    # calculate the maximum and minimum for each bucket.
    # take the difference of previous bucket max and current bucket min
    # take the maximum of above point to get maximum gap.
    maxm_bucket=[float('-inf') for _ in range(n)]
    minm_bucket=[float('inf')  for _ in range(n)]
    minm=min(array)
    maxm=max(array)
    if maxm==minm: 
        print("all the elements in the array are same the gap is same which is 0 .")
        exit(0)
    gap=(maxm-minm)//(n-1) if (maxm-minm)%(n-1)==0 else (maxm-minm)//(n-1)  + 1
    print(f"minimum element: {minm} maximum element : {maxm} gap : {gap}")
    for i in range(n):
        bkt_num = (array[i] - minm) // gap
        print(f"bucket number : {bkt_num}")
        maxm_bucket[bkt_num]=max(maxm_bucket[bkt_num],array[i])
        minm_bucket[bkt_num]=min(minm_bucket[bkt_num],array[i])
    print(f"maximum bucket : {maxm_bucket}")
    print(f"minimum bucket : {minm_bucket}")

    ans=float('-inf')
    prev=float('-inf')
    for i in range(n):
        if minm_bucket[i]==float('inf') : continue
        if prev==float('-inf') : prev=maxm_bucket[i]
        else:
            ans=max(ans,minm_bucket[i]-prev)
            prev=maxm_bucket[i]

    print(f"maximum gap between two consecutive elements in the array : {ans}")
        



