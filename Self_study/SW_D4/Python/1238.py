from collections import deque # 라이브러리 사용을 생활화:D
for tc in range(1, 11): # 테스트케이스가 10개니까
    l, s = map(int, input().split()) # 주어지는 입력 값의 길이, 시작 값
    data = list(map(int, input().split())) # 데이터로 입력 받기
    visited = [0] * 101 # 방문 배열, 부여될 수 있는 번호가 1에서 100이하이므로 101
    Q = deque()
    Q.append((s, 1)) # 시작 값과 시간(=> 가장 나중에 연락 받는 사람이 여러 명일 수 있으므로 구분하기 위해 시간도 같이 기록)
    visited[s] = 1 # 시작 값 방문 처리
    ans = [s, 1] # 가장 나중에 연락 받게 되는 사람의 번호와 시간
    while Q: # BFS 구현
        n, t = Q.popleft() # 노드와 타임
        for i in range(0, l, 2): # from, to의 구성이므로 from 값인 짝수 번째만을 확인
            if data[i] == n and not visited[data[i+1]]: # from에 노드가 있고, 그 노드의 to를 방문하지 않은 경우
                visited[data[i+1]] = 1 # to 값을 방문 처리
                Q.append((data[i+1], t+1)) # 큐에 from 값이 될 to 값과 시간 넣기
                ans = [data[i+1], t+1] # 가장 나중에 연락 받는 사람의 번호 일 수 있으므로 정답 값 갱신
            elif data[i] == n and visited[data[i+1]] or n not in data[:l:2]: # 노드가 from 값에 있지만 그 노드의 이미 to를 방문했거나, 노드가 아예 from 값에 있지 않은 경우(to인 경우로만 존재)
                if t > ans[1]: # 시간이 이전에 방문했던 시간 보다 크다면 
                    ans = [n, t] # 정답 값 갱신
                elif t == ans[1]: # 시간이 이전에 방문했던 시간과 같다면
                    if ans[0] < n: # 연락 받은 사람의 번호가 큰 값을 경우에만
                        ans[0] = n # 정답 값을 갱신
    print(f'#{tc} {ans[0]}') # 테스트 케이스 번호와 가장 나중에 연락 받는 사람의 번호만 출력