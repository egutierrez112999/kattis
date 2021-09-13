words = input().split()
status = 'yes'
for i in words:
    total = words.count(i)
    if total > 1:
        status = 'no'
print(status)
