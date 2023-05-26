'''Given an array of n numbers the numbers indicate heights of pillars.
   Measure the amount of clogged in this histogram.
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    prefix_max=[0]*n
    prefix_max[0]=array[0]
    for i in range(n):
        prefix_max[i]=max(prefix_max[i-1],array[0])
    print(f"prefix max : {prefix_max}")
    suffix_max=[0]*n
    suffix_max[n-1]=array[n-1]
    for i in range(n-2,-1,-1):
        suffix_max[i]=max(suffix_max[i+1],array[0])
    print(f"suffix max : {suffix_max}")

    water_clogged=0
    for i in range(1,n-1):
        diff=min(prefix_max[i-1],suffix_max[i+1])
        if diff>array[i]:
            water_clogged+=diff-array[i]
    
    print(f"water clogged in the pillars : {water_clogged}")