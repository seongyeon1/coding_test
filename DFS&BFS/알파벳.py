from collections import deque

def bfs():
    queue = deque()
    alpha = []

    i, j, cnt = 0, 0, 1
    queue.append((i, j, arr[i][j]))

    while queue:
        si, sj, a = queue.popleft()
        alpha.append(a)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            
            if (0 <= ni < r) and (0 <= nj < c) and (arr[ni][nj] not in alpha):
                queue.append((ni, nj, arr[ni][nj]))
                alpha.append(arr[ni][nj])
                cnt += 1

    return cnt

r, c = map(int, input().split())
arr = [input() for _ in range(r)]
r = bfs()
print(r)
