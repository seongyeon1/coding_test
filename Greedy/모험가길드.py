# N을 입력받기
n = int(input())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
data.sort()

result = 0
l = len(data)

i = 0
while i <= l: # data 길이까지 반복
  v = data[i] # data의 공포도 저장해서 공포도의 사람 묶음
  # 해당 공포도 더한 만큼 다음 사람들을 그룹으로 묶어서 지나감
  if data[i + v - 1] == v:
    result += 1 # 그룹하나 증가 시킴
    l -= v
    i += v

print(result)
