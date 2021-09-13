mbs = int(input())
months_past = int(input())
hours_used = []
for i in range(months_past):
    hours_used.append(int(input()))
rollover = mbs
for i in hours_used:
    rollover+= (mbs - i)
print(rollover)
