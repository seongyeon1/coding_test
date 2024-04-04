def solution(brown, yellow):
    x = (brown + 4 + pow(brown**2 - 8*brown - 16*yellow + 16, 0.5)) / 4
    y = (brown + 4 - pow(brown**2 - 8*brown - 16*yellow + 16, 0.5)) / 4
    answer = [x, y]
    
    return answer