def solution(numbers):
    numbers = sorted(numbers)
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            val = numbers[i] + numbers[j]
            if val not in answer:
                answer.append(val)
        
    return sorted(answer)