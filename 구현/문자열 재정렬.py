n = list(map(str, input()))
n.sort()

i = 0
sum = 0

while True:
    if n[i].isdigit() == True:
        sum += int(n[i])
        i += 1
    else:
        break

result = ''.join(n[i:])
if i != 0:
    result = result + str(sum)