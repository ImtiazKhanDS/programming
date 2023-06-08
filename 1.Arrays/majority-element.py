from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/'''
        n=len(nums)
        maj_element=-1;votes=0
        for i in range(n):
            if votes==0:
                maj_element=nums[i]
                votes=1
            else:
                if maj_element==nums[i]:
                    votes+=1
                else:
                    votes-=1
        return maj_element
    
if __name__ == "__main__":
    sol=Solution()
    print(sol.majorityElement([3,2,3]))