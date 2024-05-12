from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시의 거리는 0으로 설정

q = deque([x])
cnt = 0
while q:
    v = q.popleft()

    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)


# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)