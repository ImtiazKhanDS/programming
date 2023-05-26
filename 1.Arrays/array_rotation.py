'''Given an integer array , and integer k , rotate the array clockwise by k-units.
    example : 1 5 2 4 3
    k =3
    output  : 2 4 3 1 5
'''

if __name__=="__main__":
    n=int(input("enter the number of elements in the array : "))
    array=[]
    for i in range(n):
        temp=int(input("enter next element in the array : "))
        array.append(temp)
    print(f"array entered : {array}")

    k=int(input("enter the number of rotations : "))
    '''example : 1 5 2 4 3
            k=3
            1 5 2 4 3
            p1  p2
            reverse individually
            5 1 3 4 2
            now reverse the whole array
            2 4 3 1 5
            output  : 2 4 3 1 5
     '''
    
    #reverse individually
    i=0;j=(n-k)//2
    while i<j:
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
        i+=1
        j-=1
    i=(n-k)//2 +1 ;j=n-1   
    while i<j:
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
        i+=1
        j-=1
    #now reverse the whole array
    i=0;j=n-1
    while i<j:
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
        i+=1
        j-=1

    print(f"rotated array : {array}")



