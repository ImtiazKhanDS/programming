from typing import List
class Solution:
    def _prefix_max(self,height:List[int]):
        '''calculates prefix max of heights'''
        n=len(height)
        self.prefix_maxm=[float('-inf')]*n
        self.prefix_maxm[0]=height[0]
        for i in range(1,n):
            self.prefix_maxm[i]=max(self.prefix_maxm[i-1],height[i])

    def _suffix_max(self,height:List[int]):
        '''calculates suffix max of heights'''
        n=len(height)
        self.suffix_maxm=[float('-inf')]*n
        self.suffix_maxm[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            self.suffix_maxm[i]=max(height[i],self.suffix_maxm[i+1])
        
    def trap(self, height: List[int]) -> int:
        self._prefix_max(height)
        self._suffix_max(height)
        ans=0
        n=len(height)
        for i in range(1,n-1):
            maxm=min(self.prefix_maxm[i],self.suffix_maxm[i])
            if maxm-height[i]>0:
                ans=ans+(maxm-height[i])
        return ans
