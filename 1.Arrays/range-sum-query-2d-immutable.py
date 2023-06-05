from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix_summation = matrix
        n=len(self.matrix_summation)
        m=len(self.matrix_summation[0])


        for i in range(0,n):
            sum_=0
            for j in range(0,m):
                sum_+=self.matrix_summation[i][j]
                self.matrix_summation[i][j]=sum_
        
        print(f"Row sum matrix : {self.matrix_summation}")

        for j in range(0,m):
            sum_=0
            for i in range(0,n):
                sum_+=self.matrix_summation[i][j]
                self.matrix_summation[i][j]=sum_
 
        print(f"Column sum matrix : {self.matrix_summation}")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.matrix_summation[row2][col2]
        if col1>0:
            ans-=self.matrix_summation[row2][col1-1]
        if row1>0:
            ans-=self.matrix_summation[row1-1][col2]
        if col1>0 and row1>0:
            ans+=self.matrix_summation[row1-1][col1-1]
        return ans
       

if __name__  == '__main__':
    matrix=[[3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1], 
            [1, 2, 0, 1, 5], 
            [4, 1, 0, 1, 7], 
            [1, 0, 3, 0, 5]]
    num_matrix=NumMatrix(matrix)
    print(num_matrix.sumRegion(2,1,4,3))
