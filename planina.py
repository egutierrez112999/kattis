iterations = int(input())
side = 2
for i in range(iterations):
    new_points = side - 1
    points = new_points + side
    side = points
print(side*side)
