cards = input()
status = 1
for i in cards:
    total = cards.count(i)
    if total > 1:
        status = 0
print(status)
