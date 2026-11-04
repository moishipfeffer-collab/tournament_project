def check_win(match:dict):
    if int(match["home_goals"]) > int(match["away_goals"]):
        return "home","away"
    elif int(match["home_goals"]) < int(match["away_goals"]):
        return "away","home"
    else:
        return "drow"






