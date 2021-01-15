class Solution:
    def maximumProduct(self, nums )  :
        nums_len = len(nums)
        if nums_len < 3:
            return False
        nums.sort()
        x = 1
        print(nums[-3:])
        for i in nums[-3:]:
            x*=i
        return x    
        # return (x = x*i for i in nums[-3:])


if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([1,5,3,4]))