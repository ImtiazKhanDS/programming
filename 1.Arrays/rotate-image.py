from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
            transpose  -> reverse
        1 2 3      1 4 7      7 4 1
        4 5 6  ->  2 5 8  ->  8 5 2
        7 8 9      3 6 9      9 6 3
        """
        n=len(matrix)
        # transpose
        for i in range(n):
            for j in range(n):
                if i<j:
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp

        # reverse
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
if __name__=="__main__":
    sol=Solution()
    print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))