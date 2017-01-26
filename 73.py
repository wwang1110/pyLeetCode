class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return
        a = 1
        b = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i != 0 and j != 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                    else:
                        if i == 0:
                            a = 0
                        if j == 0:
                            b = 0
        print(a)
        print(b)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0 and j != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        if a == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if b == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

if __name__ == "__main__":
    s = Solution()
    s.setZeroes([[1,0,3]])
