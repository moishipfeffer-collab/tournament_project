
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

def update_team_data(team_type,teams,matches):
    for team in teams:
        if team["id"] == matches[f"{team_type}_id"]:
            team["played"] = 1
            team["goals_for"] = matches[f"{team_type}_goals"]