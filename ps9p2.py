def calcbatavg(hits, atbats):
    if atbats == 0:
        return 0.0
    else:
        return hits / atbats

players = []
count = 0

try:
    while True:
        lname = input("Enter player's last name (or press Ctrl+Z to stop): ")
        if lname == '':
            break

        hits = int(input("Enter number of hits: "))
        atbats = int(input("Enter number of at bats: "))

        batavg = calcbatavg(hits, atbats)

        players.append((lname, batavg))
        count += 1

except EOFError:
    pass

print("\nPlayer Data:")
for player in players:
    lname, batavg = player
    print(f"Player Last Name: {lname}, Batting Average: {batavg:.3f}")

print(f"Total number of players entered: {count}")
