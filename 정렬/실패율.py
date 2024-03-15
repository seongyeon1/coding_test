def solution(N, stages):
    fail = [0 for _ in range(N+1)]

    for stage in stages:
        fail[ stage - 1 ] += 1
        
    for i in range(len(fail)):
        if sum(fail[i:]) != 0:
            fail[i] /= sum(fail[i:])
        
    return [i + 1 for i in sorted(range(len(fail)), key=lambda k: fail[k],reverse=True) if i < N]
