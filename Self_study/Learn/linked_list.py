# 5108

# for tc in range(1, int(input())+1):
#     n, m, l = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for _ in range(m):
#         i, j = map(int, input().split())
#         nums.insert(i, j)
#     print('#{} {}'.format(tc, nums[l]))

# 5110

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m-1):
        l = len(nums)
        temp = list(map(int, input().split()))
        f = temp[0]
        for i in range(l):
            if nums[i] > f:
                nums[i:0] = temp
                break
        ll = len(nums)
        if l == ll:
            nums += temp
    print('#{} {}'.format(tc, ' '.join(map(str, nums[-1:-11:-1]))))


# 5120

# for tc in range(1, int(input())+1):
#     n, m, k = map(int, input().split())
#     password = list(map(int, input().split()))
#     i = 0
#     for _ in range(k):
#         i += m
#         l = len(password)
#         if i == l:
#             sum = password[i-1]+password[0]
#             password.insert(i, sum)
#         elif i > l:
#             i = i % l    
#             sum = password[i-1]+password[i]
#             password.insert(i, sum)
#         else:
#             sum = password[i-1]+password[i]
#             password.insert(i, sum)
#     if len(password) <= 10:
#         print('#{} {}'.format(tc, ' '.join(map(str, password[::-1]))))
#     else:
#         print('#{} {}'.format(tc, ' '.join(map(str, password[-1:-11:-1]))))

# 5122

# for tc in range(1, int(input())+1):
#     n, m, l = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for _ in range(m):
#         order = list(input().split())
#         o = order[0]
#         if o == 'I':
#             nums.insert(int(order[1]), int(order[2]))
#         elif o =='D':
#             nums.pop(int(order[1]))
#         elif o == 'C':
#             nums[int(order[1])] = int(order[2])
#     if l >= len(nums):
#         print('#{} {}'.format(tc, -1))
#     else:
#         print('#{} {}'.format(tc, nums[l]))
