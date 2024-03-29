import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    tmp = list(map(int, input().split()))
    
    if tmp[0] == 1:
        stack.append(tmp[-1])
    
    elif tmp[0] == 2:
        if stack == []:
            print(-1)
        else:
            print(stack.pop())

    elif tmp[0] == 3:
        print(len(stack))
    
    elif tmp[0] == 4:
        if stack == []:
            print(1)
        else:
            print(0)
    
    elif tmp[0] == 5:
        if stack == []:
            print(-1)
        else:
            print(stack[-1])

    else:
        pass