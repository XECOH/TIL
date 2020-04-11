for tc in range(1, int(input())+1):
    original_memory = list(map(int, input()))
    current_memory = [0] * len(original_memory)
    cnt = 0
    while current_memory != original_memory:
        for i in range(len(original_memory)):
            if current_memory[i] != original_memory[i]:
                for j in range(i, len(original_memory)):
                    current_memory[j] = 1 - current_memory[j]
                cnt += 1
    print('#{} {}'.format(tc, cnt))
