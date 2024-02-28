n = input()

l = len(n)
f, r = 0, 0

for i in range(int(l/2)):
    f += int(n[i])
    r += int(n[-(i+1)])

if f == r:
    print('LUCKY')
else:
    print('READY')


###
n = list(map(int, input()))
mid = len(n) // 2
left, right = n[:mid], n[mid:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")