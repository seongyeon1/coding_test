n = int(input())

from collections import deque

#deque 생성
d = deque(maxlen=n)

for _ in range(n):
    word = input()
    i = 0
    while (i < n) | (len(d[i]) > word ):
        i += 1
    
    if word not in d:
        d.insert(n, word)
'''
[정렬 기준]
1) 길이가 짧은 것부터
2) 길이가 같으면 사전 순으로
'''
d
