class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get matrix dimensions
        ROWS, COLS = len(matrix), len(matrix[0]) # no of rows and columns 

        # treat the 2d matrix as a flattened 1D array for binary search
        l, r = 0, ROWS * COLS - 1 # left pointer at start, right pointer at end of 1d array

        # standard binary search loop 
        while l <= r: 
            # calculate middle index (avoiding integer overflow)
            m = l + (r-l) // 2

            # convert 1d index back to 2d coordinates 
            row, col = m//COLS, m % COLS 

            # compare target with middle element 
            if target > matrix[row][col]:
                l = m + 1 # target is larger, search right half 
            elif target < matrix[row][col]:
                r = m - 1 # target is smaller, search left half 
            else:
                return True 

        return False 
        