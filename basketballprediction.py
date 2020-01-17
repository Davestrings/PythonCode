TeamAScore = input("Enter home team score: ")
TeamBScore = input("Enter away team score: ")
hasBall = input("Is leading team with the ball?(1(yes)or 2(no)): ")
time = input('Enter time remaining: ')

TeamAScore = int(TeamAScore)
TeamBScore = int(TeamBScore)
hasBall = int(hasBall)
time = float(time)

diff = abs(TeamAScore - TeamBScore)

diff -= 3
if hasBall == 1:
    diff += 0.5
else:
    diff -= 0.5


diff = diff**2


if diff > time:
    print("Lead is safe")
    print("difference is:",diff)
else:
    print("Lead is not safe")
    print("difference is:",diff)

