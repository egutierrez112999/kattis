periods = int(input())
period_list = []
for i in range(periods):
    period_list.append(input().split())
qaly = 0
for period in period_list:
    qaly += (float(period[0])* float(period[1]))
print(round(qaly, 5))
