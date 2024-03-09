
def solution1(arr, intervals):
    answer = []
    for interval in intervals:
        for i in range(interval[0], interval[1]+1):
            answer.append(arr[i])
    return answer

def solution2(arr, intervals):
    answer = []
    for interval in intervals:
        for i in range(interval[0], interval[1]+1):
            answer.append(arr[i])
    return answer

def solution3(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]
