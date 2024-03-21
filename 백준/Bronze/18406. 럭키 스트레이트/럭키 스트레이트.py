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