from typing import List
class Solution:
    def _prefix_max(self, arr: List[int]):
        self._prefix_max(arr)
        n=len(arr)
        self.prefix_max=[float('-inf') for i in range(n)]
        self.prefix_max[0]=arr[0]
        for i in range(1,n):
            self.prefix_max[i]=max(self.prefix_max[i-1],arr[i])
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n):
            ans+= 1 if self.prefix_max[i]==i else 0
        return ans
            