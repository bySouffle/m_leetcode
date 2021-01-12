class Solution:
    def getWinner(self, arr , k ) :
        """{    慢
                连胜回合数 k
                (1. 最大的数 排到它时 一直连胜) 
                (   相当于一个冒泡排序  )
                (   )
            }
        """
        cnt = 0
        
        for i in range(len(arr)*( len(arr) -1 )):


            if arr[0] > arr[1]:
                arr.append(arr.pop(1))
                cnt += 1
                print("arr[0]>arr[1] {}".format(arr[0]))
                if cnt == k:
                    return arr[0]
                print(arr)
            else:
                cnt = 1
                if cnt == k:
                    return arr[1]
                arr.append(arr.pop(0))


        return arr[0]
        



if __name__ =="__main__":
    s = Solution()
    a = s.getWinner(arr = [1,25,35,42,68,70], k = 1)
    print(a)