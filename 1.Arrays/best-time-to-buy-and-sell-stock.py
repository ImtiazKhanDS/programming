from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''compute prefix min and suffix max and take max of the differences'''
        n=len(prices)
        prices_min=[0]*n
        prices_min[0]=prices[0]
        for i in range(1,n):
            prices_min[i]=min(prices_min[i-1],prices[i])
        
        prices_max=[0]*n
        prices_max[n-1]=prices[n-1]
        for i in range(n-2,-1,-1):
            prices_max[i]=max(prices_max[i+1],prices[i])

        ans=0
        for i in range(n):
            ans=max(ans,prices_max[i]-prices_min[i])
        return ans

if __name__=="__main__":
    sol=Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))