S = input()
i = 1
c = 0

while i < len(S):
  if S[i] != S[i-1]:
      c += 1
  i += 1

print(round(c/2))
