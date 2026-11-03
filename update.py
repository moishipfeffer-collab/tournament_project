from helpers import set_goals_against,check_win

def create_team(team_name,team_id):
    team = {"id":team_id,"name":team_name,"played":0,"wins":0,"draws":0,
            "losses":0,"goals_for":0,"goals_against":0,"points":0}
    return team

def add_team(team:dict,teams:list):
    teams.append(team)  
    return teams

def create_match(home_id,away_id,home_goals,away_goals):
    match = {"home_team_id":home_id,"away_team_id":away_id,
        "home_goals":home_goals,"away_goals":away_goals}
    return match

def add_match(match:dict,matches):
    matches.append(match)
    return matches 


def update_team_data(team_type,teams,match):
    winner,looser = check_win(match)
    for team in teams:
        set_goals_against(team,match)
        if team["id"] == match[f"{team_type}_team_id"]:
            team["played"] = 1
            team["goals_for"] = match[f"{team_type}_goals"]
        if winner == team_type:
            if team["id"] == match[f"{team_type}_team_id"]:
                team["wins"] = 1
                team["points"] = 3
        elif looser == team_type:
            if team["id"] == match[f"{team_type}_team_id"]:
                team["losses"] = 1
        else:
            team["points"] = 1
    


