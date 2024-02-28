# N을 입력받기
n = int(input())
# N개의 수를 공백으로 구분하여 입력받기
data = input().split()


x, y = 1, 1
for i in data:
    if (i == 'L') & (y > 1):
        y -= 1

    elif (i == 'R')  & (y < n):
        y += 1
    
    elif (i == 'U')& (x > 1):
        x -= 1

    elif (i == 'D')& (x < n):
        x += 1
    
    else:
        pass

print(x, y)