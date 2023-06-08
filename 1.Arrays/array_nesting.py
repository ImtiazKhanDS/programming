from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        '''input : [5,4,0,3,1,6,2]
           output : 4'''
        n=len(nums)
        if n==1: return 1
        max_sequence=0
        for i in range(n):
            if nums[i]>0:
                ans=0;index=i;next_index=nums[index];
                while i!=next_index:
                    index=next_index
                    next_index=nums[index]
                    nums[index]=-(nums[index]+1)
                    ans+=1

                max_sequence=max(ans+1,max_sequence)
        return max_sequence
        
if __name__ == '__main__':
    s=Solution()
    print(s.arrayNesting([5,4,0,3,1,6,2]))