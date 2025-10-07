teams = (
    ("Команда А", 15),
    ("Команда Б", 12),
    ("Команда В", 18),
    ("Команда Г", 10),
    ("Команда Д", 14)
)

sorted_teams = sorted(teams, key=lambda x: x[1], reverse=True)
print(sorted_teams)
for i,(team, oh)  in enumerate(sorted_teams):
    #print(f"Место: {i+1} {team} {oh}")
    print(f"Место: {i+1} {sorted_teams[i][0]} {sorted_teams[i][1]}")
    #print(f"Место: {i + 1} {sorted_teams[i]} ")

