class Solution:
    def countServers(self, grid )  :
        """
        这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。

        如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

        请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

        """
        """
        1. 行列扫描 mn
        2. 全部统计到前面 有就扫没有不扫 最差mn

        """

        std_row = []
        std_col = []

        # for i in range(len(grid)):
        #     std_row.append(sum(grid[i]))

        #     for j in range(len(grid[0])):
                

        for j in range(len(grid[0])):
            
            col_sum = 0
            for i in range(len(grid)):
                col_sum += grid[i][j]
                # print(col_sum)
                if len(std_row) < len(grid):
                    std_row.append(sum(grid[i]))
            std_col.append(col_sum)
            # print(std_col)
            
        # print(std_row,std_col)

        cnt = 0
        for i in range(max(len(std_row),len(std_col) )):
            conn = max(std_col[i],std_row[i])
            if conn > 1:
                cnt += conn


        return cnt

        # for i in list(zip(*grid)):
        #     col


if __name__ == "__main__":
    s = Solution()
    a = s.countServers([[1,0],[1,1]])
    print(a)