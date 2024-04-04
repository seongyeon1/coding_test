def solution(brown, yellow):
    grid = brown + yellow
    for n in range(3, int(grid ** 0.5) + 1): # 최소 길이부터 정사각형까지
        if grid % n != 0:
            continue
        m = grid // n
        if (n-2) * (m-2) == yellow:
            return [m, n]




# def solution(brown, yellow):
#     x = (brown + 4 + pow(brown**2 - 8*brown - 16*yellow + 16, 0.5)) / 4
#     y = (brown + 4 - pow(brown**2 - 8*brown - 16*yellow + 16, 0.5)) / 4
#     answer = [x, y]
    
#     return answer