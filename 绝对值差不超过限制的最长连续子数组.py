class Solution:
    def longestSubarray(self, nums , limit )  :
        """
        给你一个整数数组 nums ，和一个表示限制的整数 limit，
        请你返回最长连续子数组的长度，该子数组中的任意两个元素
        之间的绝对差必须小于或者等于 limit 。
        如果不存在满足条件的子数组，则返回 0 。

        输入：nums = [8,2,4,7], limit = 4
        输出：2 
        解释：所有子数组如下：
        [8] 最大绝对差 |8-8| = 0 <= 4.
        [8,2] 最大绝对差 |8-2| = 6 > 4. 
        [8,2,4] 最大绝对差 |8-2| = 6 > 4.
        [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
        [2] 最大绝对差 |2-2| = 0 <= 4.
        [2,4] 最大绝对差 |2-4| = 2 <= 4.
        [2,4,7] 最大绝对差 |2-7| = 5 > 4.
        [4] 最大绝对差 |4-4| = 0 <= 4.
        [4,7] 最大绝对差 |4-7| = 3 <= 4.
        [7] 最大绝对差 |7-7| = 0 <= 4. 
        因此，满足题意的最长子数组的长度为 2 。

        """
        

        # # 双循环超时！！！

        # lens = 0

        # for i in range(len(nums)):
        #     ret = []
        #     # ret.append(nums[i])
        #     for j in range(i, len(nums)):
        #         ret.append(nums[j])
        #         print(ret)
        #         if max(ret) - min(ret) <= limit:
        #             if lens < len(ret):
        #                 lens = len(ret)

        # return lens

        # 双循环超时！！！





if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([8,2,4,7], 4) )
