from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        '''3,4,-1,1
           3,4,5,1
           3,-4,5,-1
        '''

        # make all elements out of range as n+1
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1

        # make the index negative.
        for i in range(n):
            a=abs(nums[i])
            if a==n+1:
                continue
            nums[a-1]=-abs(nums[a-1])
          
        print(f"{nums}")
        # Iterate over the index and give the index which is first positive.
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
            

if __name__=='__main__':
    s=Solution()
    print(s.firstMissingPositive([3,4,-1,1]))