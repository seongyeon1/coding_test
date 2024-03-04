user_input = input()
t = int(user_input[0])
for i in range(1, len(user_input)):

  if (t <= 1 )|(int(user_input[i]) <= 1):
    t += int(user_input[i])
  else:
    t *= int(user_input[i])

print(t)
