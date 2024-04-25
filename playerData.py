import playerID as pID
import LeagueStat as ls

player_id = pID.playerID
stat_name = ls.stat_name
stat_name_list = []
exp_stat_name_list = []
stat_mean_list = []
graph_label_list = []
#All this variables are going to be passed to basketball.py

#All the data used was obtained from the nba_api package
#To access the player data on the API, we use his player ID
from nba_api.stats.endpoints import playergamelog
#Creating a dataframe from last season in order to obtain the main values required to start the
#simulation
gamelog_player_2022 = playergamelog.PlayerGameLog(player_id=str(player_id), season='2022')
gamelog_player_2022_df = gamelog_player_2022.get_data_frames()[0]
gamelog_player_2022_df['FG2M'] = gamelog_player_2022_df['FGM'] - gamelog_player_2022_df['FG3M']

#Creating the current season dataframe
gamelog_player_2023 = playergamelog.PlayerGameLog(player_id=str(player_id), season='2023')
gamelog_player_2023_df = gamelog_player_2023.get_data_frames()[0].iloc[::-1].reset_index()
gamelog_player_2023_df = gamelog_player_2023_df.drop(columns=['index'])
gamelog_player_2023_df['FG2M'] = gamelog_player_2023_df['FGM'] - gamelog_player_2023_df['FG3M']

#For my simulation formula I will be using the average minutes from the previous season
minutes_mean_2022 = round(gamelog_player_2022_df['MIN'].mean())
#minutes_mean_2023 = round(gamelog_player_2023_df['MIN'].mean())

#We create a mean value as well as the labels we are going to use according to the
#stats you put on stat_name
for st in stat_name:
    stat = ls.leagueStats.get(st)
    expected_stat = ls.expectedStats.get(st)
    stat_mean_2022 = round(gamelog_player_2022_df[stat].mean())
    graph_label = ls.graphLabel.get(st)
    stat_name_list.append(stat)
    exp_stat_name_list.append(expected_stat)
    stat_mean_list.append(stat_mean_2022)
    graph_label_list.append(graph_label)

'''
print(stat_name_list)
print(exp_stat_name_list)
print(stat_mean_list)
print(graph_label_list)
'''
