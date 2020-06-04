for tc in range(1, int(input())+1):
    nums, t = map(int, input().split())
    nums = list(map(int, str(nums)))
    stan = [i for i in nums]
    stan.sort(reverse=True)
    h = 0
    i = 0
    cnt = 0
    while cnt < t:
        if nums[i] != stan[i]:
            mrear = 0
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == stan[i]:
                    mrear = j
                    break
            if nums.count(stan[i]) > 1 and t > 1:
                nrear = 0
                for k in range(len(nums)):
                    if nums[k] == stan[-1-h]:
                        nrear = k
                        break
                nums[nrear], nums[mrear] = stan[i], stan[-1-h]
                i += 1
                h += 1
                cnt += 1
            else:
                nums[mrear], nums[i] = nums[i], stan[i]
                i += 1
                cnt += 1
        elif nums[i] == stan[i]:
            i += 1
        if nums == stan:
            if (t-cnt) % 2 == 0:
                cnt += (t-cnt)
            else:
                if nums[0] == nums[1]:
                    cnt += (t-cnt)
                else:
                    nums[-1], nums[-2] = nums[-2], nums[-1]
                    cnt += (t-cnt)
    print('#{} {}'.format(tc, ''.join(map(str, nums))))