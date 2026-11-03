from user_inouts import get_team_name,get_team_id,get_goals
from update import create_team,add_team,create_match,add_match,update_team_data
from validations import check_if_exists_id,check_if_exists_name,check_same_id,check_played

def show_menu():
    while True:
        choise = input("\n========== TOURNAMENT MANAGER ==========\n1.add taem\n2.show all teams\n3.add match result\n0. exit\nchoose an cption: ")
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
        if not check_same_id(home_team_id,away_team_id):
            print("the id nust be diffrent")
            continue
        if not check_played(home_team_id,teams) or not check_played(away_team_id,teams):
            print("one of the teams had playes already")
            continue
        if not check_if_exists_id(home_team_id,teams) and not check_if_exists_id(away_team_id,teams):
            print("id not found")
            continue
        home_goals = get_goals("home team")
        away_goals = get_goals("away team")
        match = create_match(home_team_id,away_team_id,home_goals,away_goals)
        matches = add_match(match,results)
        update_team_data("home",teams,match)
        update_team_data("away",teams,match)
        return matches












































        