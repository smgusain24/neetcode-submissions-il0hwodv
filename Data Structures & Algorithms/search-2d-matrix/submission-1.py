class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols= len(matrix), len(matrix[0])

        # First search the row
        
        top, bottom = 0, rows-1 
        found = False
        search_row = -1
        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][0]>target:
                bottom=mid-1
            elif matrix[mid][-1]<target:
                top=mid+1
            else:
                found=True
                search_row = mid
                break
        if not found:
            return False
        l, r = 0, cols-1
        while l<=r:
            mid = l+(r-l)//2 
            if matrix[search_row][mid] == target:
                return True
            elif matrix[search_row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
