class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        u = 0
        b = len(matrix) - 1
        row = -1

        while b >= u:
            mid = (b + u) // 2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] > target:
                if mid > 0 and matrix[mid-1][0] < target:
                    row = mid - 1
                    break
                else:
                    b = mid - 1

            elif matrix[mid][0] < target:
                if mid == len(matrix)-1 or matrix[mid+1][0] > target:
                    row = mid
                    break
                else:
                    u = mid + 1

        if row == -1:
            return False

        myrow = matrix[row]

        ll = 0
        rr = len(myrow) - 1

        while ll <= rr:
            midd = (ll + rr) // 2

            if myrow[midd] == target:
                return True

            if myrow[midd] > target:
                rr = midd - 1
            else:
                ll = midd + 1

        return False