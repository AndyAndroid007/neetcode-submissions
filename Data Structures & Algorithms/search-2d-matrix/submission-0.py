class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        a,b = 0,(m*n)-1
        while a <= b:
            mid = (a+b)//2
            x = matrix[(mid//n)][(mid%n)]
            if x == target:
                return True
            elif x < target:
                a = mid+1
            else:
                b = mid-1
        return False
        