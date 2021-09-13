import math
situations = int(input())
sits = []
for i in range(situations):
    sits.append(int(input()))
for i in sits:
    f = str(math.factorial(i))
    print(f[-1])
