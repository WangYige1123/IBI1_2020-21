n = 84
r = 1.1
i = 0
while i < 5:
# This step caculates the number of infected individuals after one round
  n = n + n * r
  i = i + 1
# This step get the reasult which is a number rather than five numbers
print (n)
