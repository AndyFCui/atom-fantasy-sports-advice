import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import playerData
import playerID as pID

pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)

player_df = playerData.gamelog_player_2023_df
real_stat = playerData.stat_name_list
last_season_mean = playerData.stat_mean_list
pred_stat = playerData.exp_stat_name_list
graph_label = playerData.graph_label_list
min_mean = playerData.minutes_mean_2022
games = player_df.shape[0]
E_stat_exact_list = []
E_stat_pred_list = []

#We are going to create a prediction stat and a graph for each stat you wrote on stat_name in LeagueStat.py
for i in range(0, len(real_stat)):
    p_stat = pred_stat[i] #The labels for the new columns
    r_stat = real_stat[i]
    player_df[p_stat] = np.nan
    player_df[p_stat][0] = last_season_mean[i]
    pic_title = pID.player_name + ' ' + graph_label[i] + ' Prediction'

    #The prediction model
    for j in range(1, games):
        player_df[p_stat][j] = round(
            ((player_df[p_stat][j - 1] + player_df[r_stat][j - 1]) / (min_mean + player_df['MIN'][j - 1])) * min_mean)

    E_stat_exact = 0
    E_stat_pred = []

    #A counter of correct prediction for each stat
    for k in range(0, games):
        if player_df[r_stat][k] == player_df[p_stat][k]:
            E_stat_exact += 1
            E_stat_pred.append(k)

    #We append the prediction counter of all the stats written
    E_stat_exact_list.append(E_stat_exact)
    E_stat_pred_list.append(E_stat_pred)

    if player_df[p_stat].max() > player_df[r_stat].max():
        max_value = player_df[p_stat].max() + 6
    else:
        max_value = player_df[r_stat].max() + 6

    #The graph
    player_df.reset_index().plot(
        x="index", y=[r_stat, p_stat], linestyle='-', marker='o', color=['coral', 'limegreen'], figsize=(20, 7))  # ,'limegreen','silver','deepskyblue','coral'
    plt.title(pic_title)
    plt.xlabel("Game")
    plt.ylabel(graph_label[i])
    plt.xticks(np.arange(0, games, 2))
    plt.yticks(np.arange(0, max_value, 2))
    plt.grid()
    plt.show()
    #pic_title = pic_title.replace(' ','_')
    #plt.savefig(pic_title + '.png')

#Printing the game by game data for our player
player_df_print = player_df.drop(
    columns=['SEASON_ID', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'VIDEO_AVAILABLE'])
print('\n')
print(pID.player_name + " stats: ")
print('\n')
print(player_df_print)

#A summary of our data
for l in range(0, len(graph_label)):
    p_stat = pred_stat[l]
    r_stat = real_stat[l]
    r_stat_mean = round(player_df[r_stat].mean(), 2)
    p_stat_mean = round(player_df[p_stat].mean(), 2)
    mean_diff = round(abs(r_stat_mean - p_stat_mean), 2)
    p_success = round((E_stat_exact_list[l] / games) * 100, 2)

    print('\n')
    print(graph_label[l] + " mean: " + str(r_stat_mean))
    print(p_stat + " mean: " + str(p_stat_mean) + ". The difference with the mean is: " + str(mean_diff))

    print("Times " + p_stat + " prediction was correct: " + str(E_stat_exact_list[l]))
    print("For an efficiency of: " + str(p_success) + "%")
    print("Predictions of " + p_stat + ": " + str(E_stat_pred_list[l]))
'''
gamelog_corr_df = player_df.drop(columns=['SEASON_ID', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'VIDEO_AVAILABLE'])
fig2 = px.imshow(gamelog_corr_df.corr())
fig2.show()
#####models
(player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / 2
((player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / 96) * ((player_df['MIN'][i - 1] + min_mean)/2)
((player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / (player_df['MIN'][i - 1] * 2)) * min_mean
((player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / (player_df['MIN'][i - 1] * 2)) * ((player_df['MIN'][i - 1] + min_mean)/2)
((player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / player_df['MIN'][i - 1]) * (min_mean/2)#((player_df[pred_stat][i - 1] + player_df[real_stat][i - 1]) / (player_df['MIN'][i - 1] + min_mean)) * min_mean
'''
