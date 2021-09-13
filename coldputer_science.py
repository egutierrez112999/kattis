recordings = int(input())
temps = input().split()
below_zero = 0
for i in temps:
    temp = int(i)
    if temp < 0:
        below_zero += 1
    else:                           
        pass
print(below_zero)
