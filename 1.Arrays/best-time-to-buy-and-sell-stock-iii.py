from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''compute prefix profit and suffix profit and take max of the summation of both
        prefix profit denotes if i sell today , what is my max profit
        suffix profit denotes if buy and sell later than today then what is my max profit.
        
        '''
        n=len(prices)
        prices_min=[0]*n
        prices_min[0]=prices[0]
        for i in range(1,n):
            prices_min[i]=min(prices_min[i-1],prices[i])

        prefix_profit=[0]*n
        for i in range(1,n):
            pre_profit=prices[i]-prices_min[i-1]
            prefix_profit[i]=max(pre_profit,prefix_profit[i-1])
        
        prices_max=[0]*n
        prices_max[n-1]=prices[n-1]
        for i in range(n-2,-1,-1):
            prices_max[i]=max(prices_max[i+1],prices[i])
        
        suffix_profit=[0]*n
        suffix_profit[n-1]=0
        for i in range(n-2,-1,-1):
            suf_profit=prices_max[i+1]-prices[i]
            suffix_profit[i]=max(suf_profit,suffix_profit[i+1])
        
        ans=suffix_profit[0]
        for i in range(1,n):
            ans=max(ans,prefix_profit[i]+suffix_profit[i])
        return ans
    



if __name__=="__main__":
    sol=Solution()
    print(sol.maxProfit([3,3,5,0,0,3,1,4]))
    print(sol.maxProfit([1,2]))