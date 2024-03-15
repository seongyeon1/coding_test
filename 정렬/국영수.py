# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

col = ('이름','국어','영어','수학')
specs = (('국어', True),  # 1. 국어 점수가 감소하는 순서로
         ('영어', False), # 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
         ('수학', True),  # 3. 국어 점수와 영어 점수가 같으면 수학점수가 감소하는 순서로
         ('이름', False), # 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
         )

for key, reverse in reversed(specs):
    array.sort(key=lambda x: x[col.index(key)], reverse=reverse)

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0])
