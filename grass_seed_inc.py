seed_price =float(input())
total_lawns = int(input())
total_price = 0
for i in range(total_lawns):
    lawn = input().split()
    size = (float(lawn[0])*float(lawn[1]))
    price = seed_price * size
    total_price += price
print(total_price)
