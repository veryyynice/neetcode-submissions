class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first we reverse order of sub arrays then make all the rows columsn
        matrix[:] = matrix[::-1]
        #then last row becomes last column

        #ey. [1][0] = [0][1]
        #ey  1,0 = 0,1 
        #34
        #12
        for y in range(len(matrix[0])):
            #y
            for x in range(y+1,len(matrix[0])):
                matrix[y][x],matrix[x][y] = matrix[x][y], matrix[y][x]

