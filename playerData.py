import playerID as pID
import LeagueStat as ls
import pandas as pd

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)

player_id = pID.playerID
stat_name = ls.stat_name
stat_name_list = []
exp_stat_name_list = []
stat_mean_list = []
graph_label_list = []

active_players_data = pd.read_csv('active_nba_players_data.csv')
player_gamelog = active_players_data[active_players_data['Player_ID'] == player_id]

gamelog_player_2022_df = player_gamelog[player_gamelog['SEASON_ID'] == 22022]
gamelog_player_2022_df = gamelog_player_2022_df.drop(columns=['index']).reset_index()
gamelog_player_2022_df['FG2M'] = gamelog_player_2022_df['FGM'] - gamelog_player_2022_df['FG3M']
minutes_mean_2022 = round(gamelog_player_2022_df['MIN'].mean())

gamelog_player_2023_df = player_gamelog[player_gamelog['SEASON_ID'] == 22023]
gamelog_player_2023_df = gamelog_player_2023_df.drop(columns=['index'], axis=1).reset_index()
gamelog_player_2023_df['FG2M'] = gamelog_player_2023_df['FGM'] - gamelog_player_2023_df['FG3M']
gamelog_player_2023_df = gamelog_player_2023_df.iloc[:,1:]

for st in stat_name:
    stat = ls.leagueStats.get(st)
    expected_stat = ls.expectedStats.get(st)
    stat_mean_2022 = round(gamelog_player_2022_df[stat].mean())
    graph_label = ls.graphLabel.get(st)
    stat_name_list.append(stat)
    exp_stat_name_list.append(expected_stat)
    stat_mean_list.append(stat_mean_2022)
    graph_label_list.append(graph_label)
