class Solution:
    def sumOddLengthSubarrays(self, arr )  :
        """
            1. 所有单个
            2. 奇数个 123 234 345 
                      12345 23456 .
        """

        lens = len(arr)
        m_sum = 0
        n = lens//2
        m_sum += sum(arr)
        for i in range(1,n+1):
            nums = 2*i+1 
            
            left = 0
            right = nums
            while right <= lens:
                print(arr[ left : right ])
                m_sum += sum( arr[ left : right ] )
                left += 1
                right = left + nums  

        return m_sum

if __name__ =="__main__":
    a = Solution()
    print(a.sumOddLengthSubarrays([10,11,12]))