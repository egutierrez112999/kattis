problem_set = input().split(';')
total_problems = 0
for i in problem_set:
    if '-' in i:
        probs = i.split('-')
        total_problems += ((int(probs[-1])-int(probs[0]))+1)
    else:
        total_problems += 1
print(total_problems)
