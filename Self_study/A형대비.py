def cal(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        if op1 < 0 and abs(op1) % op2 != 0:
            return (op1 // op2) +1
        elif op1 < 0 and abs(op1) % op2 ==0 :
            return op1 // op2
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
    for i in range(1<<(n-1)):
        for j in range(1, )
        st = []
        st.append(nums[0])
        for i in range(n-1):
            c = cal(st.pop(), nums[i+1], p[i])
            st.append(c)
        temp.append(st.pop())
    ans.append(max(temp) - min(temp))

j = 1
for i in ans:
    print('#{} {}'.format(j, i))
    j += 1

