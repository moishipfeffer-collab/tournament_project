import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")

teams_file = Path(__file__).parent / "teams.json"
played_file = Path(__file__).parent / "players.json"

def load_from_json(file_type):
    if not file_type.exists():
        return []
    try:
        with open(file_type,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        logging.error("the json file is empty")
        return []

    
def save_to_json(file_type,json_save):
    with open(file_type,"w") as file:
        json.dump(json_save,file,indent=4)

def add_to_json(json_oiginal,json_add):
    json_oiginal.append(json_add)
    return json_oiginal

def add_team_flow(team):
    team_list = load_from_json(teams_file)
    teams = add_to_json(team_list,team)
    save_to_json(teams_file,teams)


    
    



