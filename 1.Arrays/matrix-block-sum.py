from typing import List 
class Solution:
    def sum_region(self,r1,c1,r2,c2,matrix):
        ans=0
        m,n=len(matrix),len(matrix[0])
        ans+=matrix[r2][c2]            
        if r1-1>=0: ans-=matrix[r1-1][c2]
        if c1-1>=0: ans-=matrix[r2][c1-1]
        if r1-1>=0 and c1-1>=0: ans+=matrix[r1-1][c1-1]
        return ans

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            sum_=0
            for j in range(n):
                sum_ += mat[i][j]
                mat[i][j] = sum_
        for j in range(n):
            sum_=0
            for i in range(m):
                sum_ += mat[i][j]
                mat[i][j] = sum_
        ans=[]
        for i in range(m):
            row=[]
            for j in range(n):
                r1, c1, r2, c2= i-k,j-k,min(i+k,m-1),min(j+k,n-1)
                row.append(self.sum_region(r1,c1,r2,c2,mat))
            ans.append(row)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.matrixBlockSum([[1,2,3],
                              [4,5,6],
                              [7,8,9]],
                              1))                