from helpers import check_win

def create_team(team_name,team_id):
    team = {"id":team_id,"name":team_name,"played":0,"wins":0,"draws":0,
            "losses":0,"goals_for":0,"goals_against":0,"points":0}
    return team


def create_match(home_id,away_id,home_goals,away_goals):
    match = {"home_team_id":home_id,"away_team_id":away_id,
        "home_goals":home_goals,"away_goals":away_goals}
    return match

def add_match(match:dict,matches):
    matches.append(match)
    return matches 

def set_goals_against(team,match):
    if team["id"] == match["home_team_id"]:
        team["goals_against"] += int(match["away_goals"])
    else:
        team["goals_against"] += int(match["home_goals"])


def update_team_data(team_type,teams,match):
    winner,looser = check_win(match)
    for team in teams:
        set_goals_against(team,match)
        if team["id"] == match[f"{team_type}_team_id"]:
            team["played"] += 1
            team["goals_for"] += int(match[f"{team_type}_goals"])
        if winner == team_type:
            if team["id"] == match[f"{team_type}_team_id"]:
                team["wins"] += 1
                team["points"] += 3
        elif looser == team_type:
            if team["id"] == match[f"{team_type}_team_id"]:
                team["losses"] += 1
        else:
            if team["id"] == match[f"{team_type}_team_id"]:
                team["points"] += 1
                team["draws"] +=1

def add_played(home_id,away_id,played:list):
    played.append([home_id,away_id])
    return played


def sort_teams(teams:list):
    sorted_teams = sorted(teams,key=lambda t: (t["points"], int(t["goals_for"]) - int(t["goals_against"]),t["goals_for"],t["name"]),reverse=True)
    return sorted_teams

def add_goal_diff(sorted_teams):
    for team in sorted_teams:
        team["goals_diff"] = int(team["goals_for"]) - int(team["goals_against"])

