import pandas as pd

def func_winner(home, away, home_score, away_score):
    if home_score > away_score:
        diff = home_score - away_score
        return home, away, diff
    elif home_score - away_score ==0:
        return home, away, 0
    else:
        diff = away_score - home_score
        return away, home, diff

def func_favorite(homeodds, awayodds,home, away, home_spread, away_spread):
    if homeodds < awayodds:
        favorite = home
        odds = home_spread
        return favorite, odds
    else:
        favorite = away
        odds = away_spread
        return favorite, odds

def bet_winner(winner, loser, favorite, point_diff, favorite_line):
    if winner == favorite and point_diff > (favorite_line * -1):
        return winner
    elif winner != favorite:
        return winner
    else:
        return loser


df = pd.read_excel('nfl.xlsx')
timestamp = pd.Timestamp('2022-09-08 00:00:00')
favorite_wins = 0
dog_win = 0
for index, row in df.iterrows():
    date = row['Date']

    home_team = row['Home Team']
    away_team = row['Away Team']
    home_odds_open = row['Home Odds Open']
    away_odds_open = row['Away Odds Open']
    home_spread = row['Home Line Open']
    away_spread = row['Away Line Open']

    home_score = row['Home Score']
    away_score = row['Away Score']

    winner, loser, pnt_diff = func_winner(home_team, away_team, home_score, away_score)

    favorite, favorite_spread = func_favorite(home_odds_open, away_odds_open, home_team, away_team,home_spread,away_spread)

    #did the favorite cover the spread(ie did the favorite win by more than the spread)
    betwinner = bet_winner(winner, loser, favorite, pnt_diff, favorite_spread)
    if betwinner == favorite:
        favorite_wins = 1 + favorite_wins
    else:
        dog_win = 1 + dog_win
    if date == timestamp:
        break



#home_wins = 155
#away_wins = 120

#average favorite odds = -189
#favorite won 46.93% of time

#average dog odds = 191
#dog won 53.06% of time

#ties = 2

#total_games = 277

#
#favorite wins = 180
#under dog wins = 95
#favorites win 64.98% of time.
#underdogs win 34.296% of time.
