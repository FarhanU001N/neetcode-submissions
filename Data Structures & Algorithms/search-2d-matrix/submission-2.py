class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bigl=0
        bigr=len(matrix)
        while bigl<bigr:
            bigmid=(bigl+bigr)//2
            l,r=0, len(matrix[bigmid])
            if matrix[bigmid][l]>target:
                bigr=bigmid
            elif matrix[bigmid][r-1]<target:
                bigl=bigmid+1
            else:
                while l<r:
                    mid=(l+r)//2
                    if matrix[bigmid][mid]>target:
                        r=mid
                    elif matrix[bigmid][mid]<target:
                        l=mid+1
                    elif matrix[bigmid][mid]==target:
                        return True
                return False
        return False