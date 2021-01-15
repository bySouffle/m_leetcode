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
        ret_nums = []    

        ret = [nums[0]]
        for i in range(1,len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                ret.append(nums[i+1])
            else:
                if len(ret) > 1:
                    ret_nums.append("{}->{}".format(ret[0],ret[-1]))
                if len(ret) == 1:
                    ret_nums.append("{}".format(ret[0]))
                ret= [nums[i]]

        print(ret_nums)      




if __name__ =="__main__":
    s= Solution()
    s.summaryRanges([0,2,3,4,6,8,9])