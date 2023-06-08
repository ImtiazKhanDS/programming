from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count1,count2,maj1,maj2=0,0,0,1
        for i in range(n):
            if nums[i]==maj1:
                count1+=1
            elif nums[i]==maj2:
                count2+=1
            elif count1==0:
                maj1=nums[i]
                count1=1
            elif count2==0:
                maj2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        ans=[]
        for maj in [maj1,maj2]:
            count=0
            for p in nums:
                if p==maj:
                    count+=1
            if count>n//3:
                ans.append(maj)

        return ans
    
if __name__ == "__main__":
    s=Solution()
    print(s.majorityElement([3,2,3]))