class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #returns bool
        o_b = 0
        o_e = len(matrix)-1
        i_b = 0
        i_e = len(matrix[0])-1
        last_inner = len(matrix[0])-1
        outer_mid = 0
        # while o_b <= o_e:
        #     o_m = (o_e+o_b)/2
        #     i_m = (i_e+i_b)/2
        #     if matrix[o_m][i_m] == target:
        #         return true
        #     elif matrix[o_m][i_m] < target:
        #         if i_m == len(matrix[0])-1:
        #             o_m +=1
        #             i_m = 0
        #         else: 
        while o_b <= o_e:
            outer_mid = (o_b+o_e)//2
            if matrix[outer_mid][0] > target:
                o_e = outer_mid-1
            elif matrix[outer_mid][last_inner]< target:
                o_b = outer_mid+1
            else:
                break;
        while i_b <= i_e:
            inner_mid = (i_b+i_e)//2
            if matrix[outer_mid][inner_mid] == target:
                return True
            if matrix[outer_mid][inner_mid] < target:
                i_b = inner_mid +1
            elif matrix[outer_mid][inner_mid] > target:
                i_e = inner_mid -1

        return False
