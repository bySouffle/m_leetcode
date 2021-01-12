def func_binary_serach(a, target):

    left_idx = 0
    right_idx = len(a)-1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2 # 2     4
        
        mid = a[ mid_idx ] 

        if mid == target:
            return mid
        if target > mid :
            left_idx = mid_idx + 1  # 2+1 3 
        else:
            right_idx = mid - 1

    return False

class BinarySearch:
    def func_binary_serach(self,a,target):
        if len(a) == 0:
            print(a)
            return False
        a.sort()
        mid_idx = len(a)//2
        if a[mid_idx] == target:
            return a[mid_idx]
        return self.func_binary_serach(a[mid_idx+1:], target) if a[mid_idx] < target else \
               self.func_binary_serach(a[:mid_idx-1], target)
        


if __name__ == "__main__":
    a = [1,2,4,6,8,19]
    target = 2

    s = func_binary_serach(a,target)
    print(s)

    f = BinarySearch()
    print(f.func_binary_serach([1,2,4,6,8,19],target))