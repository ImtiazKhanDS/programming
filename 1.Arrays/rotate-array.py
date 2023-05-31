from typing import List

class Solution:
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: Arr[5] = { 1 7 3 4 5 }, k = 3
        Output: Arr[5] = [ 3 4 5 1 7 ]
        [ 1 7 3 4 5 ] → [ 3 4 5 1 7 ] 
        We can divide the array into two subarrays of length N-k and k. Now, if 
        we carefully look at the reverse of the two subarrays - 
        reverse of [ 1 7 ] → [ 7 1 ]
        reverse of [ 3 4 5 ] → [ 5 4 3 ] 
        Combining the above two reversed sub-arrays, we get → [ 7 1 5 4 3 ]
        And on reversing the above array, we get → [ 3 4 5 1 7 ], which is the desired output.
        """
        # first reverse the part till k th index and k+1 to nth index
        # then reverse the whole array.
        #import pdb
        #pdb.set_trace()

        n=len(nums)
        k=k%n
        i=0
        while i<n/2:
            nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
            i+=1
        i=0
        while i<k/2:
            nums[i],nums[k-i-1]=nums[k-i-1],nums[i]
            i+=1
        i=k
        while i<(n+k)/2:
            nums[i],nums[n+k-i-1]=nums[n+k-i-1],nums[i]
            i+=1