def func(num1, num2):

    
    len1, len2 = len(num1),len(num2)
    s_num = sorted(num1 + num2)
    print(s_num)
    print((len(s_num)/2))
    print((len(s_num)/2) -1)
    # print(s_num[int(len(s_num)/2)
    # print((s_num[int(len(s_num)/2) -1])/2))
    # odd
    if len(s_num)%2 == 1:
        return s_num[int(len(s_num)/2) ]

    if len(s_num)%2 == 0:
        a = s_num[int(len(s_num)/2) ]
        b = s_num[int(len(s_num)/2) -1]

        return ( s_num[int(len(s_num)/2) ] + s_num[int(len(s_num)/2) -1])/2
    

    

if __name__ == "__main__":
    num1, num2 = [1,2], [3,4]
    print(func(num1, num2))