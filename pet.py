players = []
for i in range(5):
    players.append(input().split())
winner = 0
score = 0
pnum=1
for player in players:
    pscore = 0
    for scored in player:
        pscore += int(scored)
    if pscore > score:
        score = pscore
        winner = pnum
    pnum +=1
print(winner, score)
