stat_name = ["3pts"]
#,"freethrow","rebound","assist","block","steal","turnover"
#Dictionary for labels for columns name and graphics labels
#The dictionaries are also for the for loop
#stat_name will be passed to playerData.py
leagueStats = {
    "3pts": 'FG3M',
    "2pts": 'FG2M',
    "freethrow": 'FTM',
    "rebound": 'REB',
    "assist": 'AST',
    "block": 'BLK',
    "steal": 'STL',
    "turnover": 'TOV'
}

expectedStats = {
    "3pts": 'E_FG3M',
    "2pts": 'E_FG2M',
    "freethrow": 'E_FTM',
    "rebound": 'E_REB',
    "assist": 'E_AST',
    "block": 'E_BLK',
    "steal": 'E_STL',
    "turnover": 'E_TOV'
}

graphLabel = {
    "3pts": '3pt Shots Made',
    "2pts": '2pt Shots Made',
    "freethrow": 'Free Throws Made',
    "rebound": 'Rebounds Made',
    "assist": 'Assists Made',
    "block": 'Blocks Made',
    "steal": 'Steals Made',
    "turnover": 'Turnovers Commited'
}
