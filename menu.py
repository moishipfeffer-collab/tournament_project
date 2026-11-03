from user_inouts import get_team_name,get_team_id,get_goals
from run_program import create_team,add_team,create_match,add_match
from validations import check_if_exists_id,check_if_exists_name

def show_menu():
    while True:
        choise = input("\n========== TOURNAMENT MANAGER ==========\n1.add taem\n2.show all teams\n3.add match result\n0. exit\nhoose an cption: ")
        if choise in ["1","2","3","4","5","6","7","8","9","10","0"]:
            return choise
        print("not valid choise")

def add_new_team(teams):
    while True:
        team_name = get_team_name()
        team_id = get_team_id()
        if check_if_exists_id(team_id,teams) and check_if_exists_name(team_name,teams):
            team = create_team(team_name,team_id)
            teams = add_team(team,teams)
            return teams
        print("name or id already exists")

def add_result(results,teams):
    while True:
        home_team_id = get_team_id("home")
        away_team_id = get_team_id("away")
        if away_team_id == home_team_id:
            print("the id nust be diffrent")
            continue
        home_goals = get_goals("home team")
        away_goals = get_goals("away team")
        if not check_if_exists_id(home_team_id,teams) and not check_if_exists_id(away_team_id,teams):
            match = create_match(home_team_id,away_team_id,home_goals,away_goals)
            matches = add_match(match,results)
            return matches
        print("id not found")
        