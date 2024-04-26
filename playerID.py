player_name = 'Nikola Jokic' #Use the name of any current player

#Obtaining the player ID of the player of your choose, using his name as input
#playerID will be passed to playerData.py
from nba_api.stats.static import players
player_dict = players.get_players()

playerList = []

for i in range(0, len(player_dict)):
    name = player_dict[i].get('full_name')
    id = player_dict[i].get('id')
    active = player_dict[i].get('is_active')
    if active:
        player = (name, id)
        playerList.append(player)
        print(player)

for player in playerList:
    if player[0] == player_name:
        playerID = player[1]

#print(playerID)
'''
#Nikola Jokic Luka Doncic LeBron James Giannis Antetokounmpo Jamal Murray Kawhi Leonard
['Luka Doncic','Nikola Jokic']
playerIDList = []
for j in range(0, len(player_name)):
    for player in playerList:
        if player[0] == player_name[j]:
            playerID = player[1]
            playerIDList.append(playerID)

print(playerIDList)
'''
