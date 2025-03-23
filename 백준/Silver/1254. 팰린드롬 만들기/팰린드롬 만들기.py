def make_palindrome(text):
    n = len(text)
    
    for i in range(n):
        temp = text + text[:i][::-1]  # i만큼 앞에서 잘라 뒤집어 붙임
        half = len(temp) // 2
        is_palindrome = True

        for j in range(half):
            if temp[j] != temp[-(j + 1)]:
                is_palindrome = False
                break

        if is_palindrome:
            return len(temp)
    
    return 2 * n - 1  # 최악의 경우 전체를 반대로 붙인 길이

# 예시
print(make_palindrome(input()))