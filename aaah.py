import sys
data = sys.stdin.readlines()

ability = str(data[0])
req = str(data[1])
if len(ability) >= len(req):
    print('go')
else:
    print('no')
