# 5174

# def find(rn):
#     global cnt
#     if child1[rn] != 0:
#         cnt += 1
#         find(child1[rn])
#     if child2[rn] != 0:
#         cnt += 1
#         find(child2[rn])
#     return

# for tc in range(1, int(input())+1):
#     e, n = map(int, input().split())
#     child1 = [0] * (e+2) # 자식 1(왼쪽), 노드 번호가 1로 시작하기 때문과 노드의 번호가 e+1번까지 존재하므로
#     child2 = [0] * (e+2) # 자식 2(오른쪽), 노드 번호가 1로 시작하기 때문과 노드의 번호가 e+1번까지 존재하므로
#     nods = list(map(int, input().split()))
#     for i in range(0, e*2, 2): # 짝수 번째 값이 부모, 홀수 번째 값이 자식 노드이므로 
#         if child1[nods[i]] == 0: # 자식 1이 비어있는 값이면 먼저 넣어줌
#             child1[nods[i]] = nods[i+1]
#         else: # 자식 1이 있다면 비어있는 자식 2값에 넣어줌
#             child2[nods[i]] = nods[i+1]
#     cnt = 1 # 자기자신부터 세니까
#     find(n)        
        
#     print('#{} {}'.format(tc, cnt))

# 5176

for tc in range(1, int(input())+1):
    n = int(input())
    binary_tree = [0] * (n+2)
    for i in range(1, n+1):
        binary_tree[i] = i
        if i > 1:

    print('#{} {} {}'.format(tc, binary_tree[1], binary_tree[n//2]))

# 5178

# for tc in range(1, int(input())+1):
#     n, m, l = map(int, input().split())
#     binary_tree = [0] * (n+1) # 이진트리를 1차 리스트로 만들고, 노드가 1부터 시작하므로 n+1을 줌
#     for _ in range(m):
#         n_n , v = map(int, input().split()) 
#         binary_tree[n_n] = v # 노드 번호와 값을 입력 받아 이진트리에 저장
#     i = n
#     while i > 1:
#         if i % 2: # 노드의 끝 번호가 홀수 일때 => 짝꿍이 있는 친구
#             hap = binary_tree[i-1] + binary_tree[i] 
#             binary_tree[(i-1)//2] = hap
#             i -= 2
#         else: # 노드의 끝 번호가 짝수 일때 => 혼자 있는 친구
#             binary_tree[i//2] = binary_tree[i]
#             i -= 1
#     print('#{} {}'.format(tc, binary_tree[l]))

# 