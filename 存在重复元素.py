import collections

# class Solution:
#     def containsNearbyDuplicate(self, nums , k )  :
#         """
#             1. 相同元素
#             2. 索引

#             可以用collection
#         """
#         d = collections.defaultdict(list)
#         for i in range(len(nums)):
#             d[ nums[i] ].append(i)
#         print(d)
#         ret = 0
#         for k,v in d.items():
#             print(v)
#             if len(v) >= 2:
                
#                 for i in range(1,len(v)):
#                     for j in range(len(v)-1):
#                         # ret = 
#                         # ret = min(ret,abs(v[i]-v[j]) )
#                         # print(ret)
#                         if ret == k:
#                             return True

#                 if ret > k:
#                     return False

        
import collections

class Solution:
    def containsNearbyDuplicate(self, nums , k ) -> bool:
        """
            1. 相同元素
            2. 索引

            可以用collection
        """
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[ nums[i] ].append(i)
        ret = 0
        for key,v in d.items():
            if len(v) >= 2:
                ret = v[1]-v[0]
                for i in range(0,len(v)-1):
                    for j in range(i+1,len(v)):
                        
                        # ret = min(ret,abs(v[i]-v[j]) )
                        print(i,j)
                        ret = min(ret,abs(v[i]-v[j]))
                        print(ret)
                        print(k)
                        if ret <= k:
                            print("zzz")
                            return True

        return False       




if __name__ == "__main__":
    s = Solution()
    s.containsNearbyDuplicate([1,2,3,1,1,2,3], 0)