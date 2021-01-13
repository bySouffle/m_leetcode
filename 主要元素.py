class Solution:
    def majorityElement(self, nums )  :
        """
        1. 长度
        2. 数量
        第一种方法最简单的方法循环统计输出
        第二种桶统计计算长度
        """
        
        m_lens = len(nums)  # 5
        m_lens_list = [0]* (max(nums) +1) 
        print(m_lens_list)
        for i in nums:  
            m_lens_list[i] += 1

        
        if max(m_lens_list) > (m_lens/2):
            return (m_lens_list.index(max(m_lens_list)))
        else:
            return -1



        m_dict = {}
        for i in range(len(nums)):
            if nums[i] not in m_dict.keys():
                m_dict[nums[i] ] = nums.count(nums[i])
        
        for k, v in m_dict.items():
            if v== max(m_dict.values()):
                if v > len(nums)/2:
                    return v
                else:
                    return -1    
        
        ret = [ k  for k,v in m_dict.items() if v == max( m_dict.values() ) ]
        if *ret > len(nums)/2:
            return *ret
        else:
            return -1
        



if __name__ == "__main__":
    s= Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))