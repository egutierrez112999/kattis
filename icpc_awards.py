total_teams = int(input())
top_12 = []
schools = []
for i in range(total_teams):
    if len(top_12) == 12:
        extra_team = input()
    else:
        team = input()
        school = (team.split())[0]
        if school in schools:
            pass
        else:
            top_12.append(team)
            schools.append(school)
for i in top_12:
    print(i)


