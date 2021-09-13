judges_votecast = input().split()
votes = []
for i in range(int(judges_votecast[1])):
    votes.append(int(input()))
votes_to_come = int(judges_votecast[0]) - int(judges_votecast[1])

def find_average(limit):
    total = 0
    for vote in votes:
        total+= vote
    for i in range(votes_to_come):
        total += limit
    average = total/int(judges_votecast[0])
    return average
print(find_average(-3), find_average(3))
