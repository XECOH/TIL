from itertools import permutations
def cal(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        if op1 < 0 and op2 > 0:
            return -(abs(op1)//op2)
        elif op1 > 0 and op2 < 0:
            return -(op1//abs(op2))
        else:
            return op1 // op2
ans = []
for tc in range(int(input())):
    temp = []
    n = int(input())
    op = list(map(int, input().split()))
    opr = ['+', '-', '*', '/']
    oper = []
    nums= list(map(int, input().split()))
    for i in range(4):
        for j in range(op[i]):
            oper.append(opr[i])
    for p in permutations(oper):
        st = []
        st.append(nums[0])
        for i in range(n-1):
            c = cal(st.pop(), nums[i+1], p[i])
            st.append(c)
        if st[0] not in temp:
            temp.append(st.pop())
    ans.append(max(temp) - min(temp))

j = 1
for i in ans:
    print('#{} {}'.format(j, i))
    j += 1

