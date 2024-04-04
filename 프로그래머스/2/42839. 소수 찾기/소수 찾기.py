from itertools import permutations

def checkPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    num = []
    
    for i in range(1, len(numbers) + 1):
        num.append(list(permutations(numbers, i)))
    num = [int(''.join(y)) for x in num for y in x]
    
    for i in num:
        if checkPrime(i):
            answer.append(i)
    return len(set(answer))

