cases = int(input())
for i in range(cases):
    case = input().split()
    bpm = (60*float(case[0])) / float(case[1])
    threshold = bpm/float(case[0])
    min_abpm = round(bpm - threshold, 4)
    max_abpm = round(bpm + threshold, 4)
    print(min_abpm,round(bpm, 4),max_abpm)

