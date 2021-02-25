inp = int(input("Enter the no of teams: "))
teams = {}
wins = []
win_rec = []
for i in range(inp):
    print()
    teams.setdefault(input("Enter the name of team: ").capitalize() , [int(input("Enter the no of wins: ")) , int(input("Enter the no losses:"))])
inp2 = input("\nEnter the name of team to search for: ").capitalize()
win_percent = teams[inp2][0] / (teams[inp2][0] + teams[inp2][1]) * 100
print(f"Winning percent of team {inp2} is {win_percent}")
for i in teams:
    wins.append(teams[i][0])
    if teams[i][0] > 0:
        win_rec.append(i)
print(f"\nThe no of wins list is {wins} and the winning record list is {win_rec}")
