import json
from pathlib import Path

teams_file = Path(__file__).parent / "teams.json"

def load_teams():
    if not teams_file.exists():
        return []
    with open(teams_file,"r") as file:
        return json.load(file)
    
def save_teams(teams):
    with open(teams_file,"w") as file:
        json.dump(teams,file,indent=4)

def add_team(teams:list,team):
    teams.append(team)
    return teams

def add_team_flow(team):
    team_list = load_teams()
    teams = add_team(team_list,team)
    save_teams(teams)


    
    



