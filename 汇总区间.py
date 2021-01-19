class Solution:
    def summaryRanges(self, nums ):

        # begin = 0
        # end = 0
        # for i in range(len(nums)):
        #     begin = i
        #     for j in range(i+1, len(nums)):
                    
        #         if (nums[i]+1) == nums[j]:
        #             end = nums[j]
        #         if (nums[i]+1) != nums[j]:   
        # diff = []

        # ret = []            

        # for i in range(len(nums)-1):
        #     diff = [nums[i]]
        #     if nums[i]+1 == nums[i+1]:
        #         diff.append(nums[i+1])
        #     # ret.append[diff]
        #     ret.append(diff)
            
        #     if nums[i]+1 > 

        """

        1. 做差         X
        2. 单循环判断   X
        
        """
        ret = []
        n = 0

        # while 循环 用if 判断条件退出循环

        while n < len(nums):    # 范围
            if n+1 <len(nums) and nums[n] + 1 == nums[n+1]: # 上一个等于下一个 给一个index 标记开始元素
                m = n
                while n+1 <len(nums) and nums[n] + 1 == nums[n+1]:  # 再来一个循环找出边界
                    n += 1
                ret.append("{}->{}".format(nums[m],nums[n]))    # 输出
                
            else:   # 下一个不等于上一个加 1
                ret.append(str(nums[n]))    # 直接输出
            n += 1
        return ret




        n = 0
        ret = []

        while n < len(nums):
            if n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                m = n
                while n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                    n+=1
                ret.append("{}->{}".format(nums[m],nums[n]))

            else:
                ret.append("{}".format(n))
            
            n+=1
            

        n = 0
        ret = []
        while n+1 < len(nums):
            if n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                m = n
                while n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                    n+=1
                ret.append("{}->{}",format(nums[m],nums[n]))

            else:
                ret.append("{}".format(nums[n]))
                
            n+=1

if __name__ =="__main__":
    s= Solution()
    print(s.summaryRanges([0,1,2,4,5,7]) )