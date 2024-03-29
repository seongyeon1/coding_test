import sys
input = sys.stdin.readline

N = int(input())
q = []
p = 0

for i in range(N):
    c = input().split()

    # push X: 정수 X를 큐에 넣는 연산이다.
    if c[0] == 'push':
        q.append(c[-1])

    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif c[0] == 'size':
        print(len(q) - p)

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif c[0] == 'empty':
        print(1 if len(q)-p == 0 else 0)
    
    elif len(q)-p == 0:
        print(-1)

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'pop':
        print(q[p])
        p += 1

    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'front':
        print(q[p])
    
    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'back':
        print(q[-1])