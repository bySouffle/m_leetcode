from cnt_time import fn_timer


class Solution(object):
    @fn_timer
    def transpose(self, A):
        
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """        
        A_ROW = len(A)
        A_COL = len(A[0])

        B = []

        for i in range(A_COL ):
            B_row = []              
            for j in range(A_ROW):
                B_row.append(A[j][i])
            B.append(B_row)

        return B    
        """

        """
        A_ROW = len(A)
        A_COL = len(A[0])
        B_row = [0]*A_ROW
        B = []

        for i in range(A_COL):
              
            for j in range(A_ROW):
                B_row[j]=A[j][i]
            B.append(B_row.copy())


        return B
        """
    
        # return [ [A[i][j] for i in range(len(A))] for j in range(len(A[0])) ]
        # print(A)
        # print(*A)
        # return [list(lows) for lows in list(zip(*A))]   

        B = []
        for i in range(len(A[0])):
            B.append([ A[j][i] for j in range(len(A)) ])
        return B

if __name__ == "__main__":
    a = Solution()
    # b = a.transpose([[1,2,3],[4,5,6],[7,8,9]])
    b = a.transpose([[1,2,3],[4,5,6]])

    print(b)