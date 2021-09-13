rodnum = int(input())
rods = []
for i in range(rodnum):
    rods.append(int(input()))
length = 0
for i in rods:
    if length > 0:
        length += i
        length -= 1
    else:
        length = i
print(length)
