class Solution:
    def trap(self, height )  :
        """
            以台阶高度为参考线
            水位高为台阶高度减去本身高度
        """
        num = len(height)
        #   没有元素
        if num < 3:
            return 0

        left, right = [0]*num,  [0]*num
        left[0] = height[0]
        right[ num-1 ] = height[ num-1 ]        
        
        for i in range(1, num): # 5     1 2 3 4
            left[i] = max( left[i-1], height[i] )
        print(left)
        for i in reversed(range(num-1)):  # 0 1 2 3 | 4
            right[i] = max( right[i+1], height[i]  )
        print(right)

        return  sum ( min ( l,f ) -h   for l,f, h in zip(left,right,height) ) 


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))





