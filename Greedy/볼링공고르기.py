
# N, M를 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(input().split())
data.sort()

c = 0
for i in range(len(data)):
	# 나와 같은 숫자의 데이터 갯수를 전체에서 뺀다
  c += len(data) - data.count(data[i])

# 빼고 겹치는거 반 나눈다
result = c / 2
print(int(result))
