def check_win(match:dict):
    if int(match["home_goals"]) > int(match["away_goals"]):
        return "home","away"
    elif int(match["home_goals"]) < int(match["away_goals"]):
        return "away","home"
    else:
        return "drow"

def set_goals_against(team,match):
    if team["id"] == match["home_team_id"]:
        team["goals_against"] = match["away_goals"]
    else:
        team["goals_against"] = match["home_goals"]
