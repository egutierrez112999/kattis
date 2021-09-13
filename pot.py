nums = int(input())
lst = []
for i in range(nums):
    lst.append(input())
total = 0
for i in lst:
    total += int(i[:-1])**int(i[-1])
print(total)
