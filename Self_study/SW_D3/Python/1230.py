for tc in range(1, 11):
    n = int(input()) 
    original_code = list(input().split())
    n_orders = int(input())
    orders = list(input().split())
    for i in range(len(orders)):
        if orders[i] == 'I':
            for t in range(int(orders[i+2])):
                original_code.insert(int(orders[i+1])+t, orders[i+3+t])
        elif orders[i] == 'D':
            for _ in range(int(orders[i+2])):
                original_code.pop(int(orders[i+1]))
        elif orders[i] == 'A':
            original_code += orders[i+2:i+2+int(orders[i+1])]
    print('#{} {}'.format(tc, ' '.join(original_code[:10])))