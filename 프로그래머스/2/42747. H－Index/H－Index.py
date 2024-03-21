def solution(citations):
    citations.sort()
    l = len(citations)
    while l >= 0:
        # h번 이상 인용된 논문
        t = len([c for c in citations if c >= l])
        
        if t >= l:
            answer = l
            break
        
        l -= 1
    return answer