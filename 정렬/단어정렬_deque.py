from collections import deque

def compare_words(word1, word2):
    '''
    [정렬 기준]
    1) 길이가 짧은 것부터
    2) 길이가 같으면 사전 순으로
    '''
    if len(word1) != len(word2):
        return len(word1) - len(word2)
    return 1 if word1 > word2 else -1 if word1 < word2 else 0

def binary_insert(d, word):
    left, right = 0, len(d)
    while left < right:
        mid = (left + right) // 2
        if compare_words(word, d[mid]) < 0:
            right = mid
        else:
            left = mid + 1
    d.insert(left, word)

# Input number of words
n = int(input())
d = deque()

prev_word = None
for _ in range(n):
    word = input().strip()
    if word not in d: 
        binary_insert(d, word)
        prev_word = word

print('\n'.join(d))
