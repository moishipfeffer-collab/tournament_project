import logging 

def check_win(match:dict):
    if int(match["home_goals"]) > int(match["away_goals"]):
        return "home","away"
    elif int(match["home_goals"]) < int(match["away_goals"]):
        return "away","home"
    else:
        return "drow","drow"

def get_best_attacking_team(teams):
    if not teams:
        print("no teams yet!")
    else:
        highest = 0
        best_team = ""
        for team in teams:
            if int(team["goals_for"]) >= int(highest):
                highest = team["goals_for"]
                best_team = team
        return best_team

def get_best_attacking_teams(best_team,teams):
    best_teams = []
    for team in teams:
        if team["goals_for"] == best_team["goals_for"]:
            best_teams.append(team)
    return best_teams







