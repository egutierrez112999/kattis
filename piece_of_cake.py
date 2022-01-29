line = input()
n, h, v = line.split()
n = int(n)
h = int(h)
v = int(v)
length = 0;
width = 0;
if h > (n-h):
    length = h
else:
    length = n-h
if v > (n-v):
    width = v
else:
    width = n-v
print(width * length * 4)
