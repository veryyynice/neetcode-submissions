class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first we reverse order of sub arrays then make all the rows columsn
        matrix[:] = matrix[::-1]
        #then last row becomes last column

        #ex. [1][0] = [0][1]

        #y
        for x in range(len(matrix[0])):
            #y
            for y in range(x+1,len(matrix[0])):
                matrix[x][y],matrix[y][x] = matrix[y][x], matrix[x][y]

