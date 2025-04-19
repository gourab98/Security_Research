teams =["A", "B", "C", "D"]
for home_team in teams:
    for away_team in teams:
        if(home_team!=away_team):
            print(home_team,away_team)
# The above code generates all possible pairs of team members.