import numpy as np
import pandas as pd

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)


ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"
balls = pd.read_csv(ipl_ball)

ball_withmatch = balls.merge(matches, on='ID', how='inner').copy()
ball_withmatch['BowlingTeam'] = ball_withmatch.Team1 + ball_withmatch.Team2
ball_withmatch['BowlingTeam'] = ball_withmatch[['BowlingTeam', 'BattingTeam']].apply(lambda x: x.values[0].replace(x.values[1], ''), axis=1)
batter_data = ball_withmatch[np.append(balls.columns.values, ['BowlingTeam', 'Player_of_Match'])]


def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }
    return team_dict


def teamVSteamAPI(team1, team2):
    invalid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 in invalid_teams and team2 in invalid_teams:
        teams_played = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (
                    matches['Team2'] == team1)]
        total_matches = teams_played.shape[0]
        matches_won_team1 = teams_played['WinningTeam'].value_counts()[team1]
        matches_won_team2 = teams_played['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
                'total_matches': total_matches,
                team1: str(matches_won_team1),
                team2: str(matches_won_team2),
                'draws': str(draws)
        }
        return response
    else:
        return {"error": "Invalid Team name"}
