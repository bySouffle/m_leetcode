class Solution:
    def numSubmatrixSumTarget( self, matrix, target):
        """
        1.  single row
        2.  single col
        3.  single element

        4.  Multiple row  
        5.  Multiple col
        """

        row_len , col_len = len(matrix) , len(matrix[0])
        ret = 0
        sum = 0

        row_count ,col_count = [], []

        # row
        for i in range(row_len):
            for s in matrix[i]:
                sum += s
            
            #   行总和
            row_count.append(sum)

            if sum == target:
                ret += 1   
                print("row") 
                print(ret)
            sum = 0

            for j in range(col_len):
                sum += matrix[i][j]


                if matrix[i][j] == target:
                    ret += 1
                print(ret)
            
            col_count.append(sum)
            if sum == target:
                ret += 1
            print("col") 
            print(ret)
            sum = 0

        print(row_count,col_count)

        for i in range(len(row_count)):
            
            for j in range(i + 1,len( row_count)):
                print(i,j)

                if (row_count[i]+row_count[j]) == target:
                    ret += 1
                    


        return ret

if __name__ == "__main__":
    sol = Solution()
    ret = sol.numSubmatrixSumTarget(matrix=[[0,0,0,1,1],[1,1,1,0,1],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,1]],target = 0)    
    print(ret)