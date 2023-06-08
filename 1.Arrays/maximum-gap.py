from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2 : return 0
        maxm=max(nums)
        minm=min(nums)
        if maxm==minm:return 0
        gap=(maxm-minm)//(n-1) if (maxm-minm)%(n-1)==0 else (maxm-minm)//(n-1) + 1
        maxm_bucket=[float('-inf') for _ in range(n)]
        minm_bucket=[float('inf') for _ in range(n)]
        for i in range(n):
            bucket=(nums[i]-minm)//gap
            maxm_bucket[bucket]=max(maxm_bucket[bucket],nums[i])
            minm_bucket[bucket]=min(minm_bucket[bucket],nums[i])
        print(f"maximum bucket : {maxm_bucket},minimum bucket : {minm_bucket}")
        ans=float('-inf')
        prev=float('-inf')
        for i in range(n):
            if minm_bucket[i]==float('inf'): continue
            if prev==float('-inf'): prev=maxm_bucket[i]
            else:
                ans=max(ans,minm_bucket[i]-prev)
                prev=maxm_bucket[i]

        return ans
if __name__=='__main__':
    nums=[3,6,9,1]
    print(Solution().maximumGap(nums))