from functools import cmp_to_key

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(lambda x, y :int(x+y) - int(y+x)), reverse = True)
    return str(int(''.join(numbers)))

# def solution(numbers):
#     answer = ''
#     numbers=list(map(str,numbers))
#     numbers.sort(key=lambda x:x*4, reverse=True)
#     answer=str(int(''.join(numbers)))

#     return answer