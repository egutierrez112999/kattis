cases = int(input())

for i in range(cases):
    test = input().split()
    strip_total = int(test[0])
    outlets = 1
    strips = test[1:]
    for i in strips:
        outlets-=1
        outlets+=int(i)
    print (outlets)

