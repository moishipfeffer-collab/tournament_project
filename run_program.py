from user_inouts import get_team_name,get_team_id,get_goals
from update import create_team,create_match,add_match,update_team_data,sort_teams,add_goal_diff,set_goals_against
from validations import check_if_exists_id,check_if_exists_name,check_same_id,check_played
from storage import save_to_json,add_to_json,played_file,teams_file
from helpers import get_best_attacking_teams,get_best_attacking_team
import logging

logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")



def show_menu():
    while True:
        choise = input("\n========== TOURNAMENT MANAGER ==========\n1. add taem\n2. show all teams\n3. add match result\n4. show sorted teams\n"
        "5. show leading team\n6. show best attacking team\n7. show team succes rate\n8. show teams without wins\n9. show touenament summary\n0. exit\nchoose an option: ")
        if choise in ["1","2","3","4","5","6","7","8","9","0"]:
            return choise
        logging.error("nor valid choise")


# option 1 add team

def add_new_team_flow(teams):
    while True:
        team_name = get_team_name()
        team_id = get_team_id()
        if check_if_exists_id(team_id,teams) and check_if_exists_name(team_name,teams):
            team = create_team(team_name,team_id)
            add_to_json(teams,team)
            save_to_json(teams_file,teams)
            return teams
        print("name or id already exists")

# option 2 show all teams

def show_teams(teams):
    if teams:
        print(f"the teams are:\n{teams}")
    else:
        print("no teams yet!")

# option 3 add match

def add_result_flow(results,teams,played):
    if not teams:
        print("no teams yet!")
        return
    while True:
        home_team_id = get_team_id("home")
        away_team_id = get_team_id("away")
        if not check_same_id(home_team_id,away_team_id):
            print("the id nust be diffrent")
            continue
        if not check_played(home_team_id,away_team_id,played):
            print("the teams hade played already")
            return
        if check_if_exists_id(home_team_id,teams) or check_if_exists_id(away_team_id,teams):
            print("id not found")
            continue
        home_goals = get_goals("home team")
        away_goals = get_goals("away team")
        match = create_match(home_team_id,away_team_id,home_goals,away_goals)
        add_match(match,results)
        update_team_data("home",teams,match)
        update_team_data("away",teams,match)
        set_goals_against(teams,match)
        save_to_json(teams_file,teams)
        add_to_json(played,[home_team_id,away_team_id])
        save_to_json(played_file,played)
        return 

# option 4 show sorted teams
  
def show_sort_team_flow(teams):
    if not teams:
        print("no teams yet!")
    else:
        sorted_teams = sort_teams(teams)
        add_goal_diff(sorted_teams)
        print(f"\nthe sorted teams are:\n{sorted_teams}")

# option 5 show best team 

def show_liding_team(teams):
    if not teams:
        print("no teams yet!")
    else:
        sorted_teams = sort_teams(teams)
        add_goal_diff(sorted_teams)
        print(f"\nthe leading team is:\n{sorted_teams[0]}")

# option 6 show best attack 

def show_best_teams(teams):
    best_team = get_best_attacking_team(teams)
    best_teams = get_best_attacking_teams(best_team,teams)
    print(f"\nthe best teams are:\n{best_teams}")

# option 7 show succes rate

def show_no_games(teams):
    for team in teams:
        print(f"{team}: no games")

def show_succes_rate(teams):
    print("\n=== succes rate ===")
    no_games = []
    for team in teams:
        if int(team["played"]) > 0:
            print(f"{team['name']}: {int(team['points']) / int((team['played'] * 3)) * 100} %")
        else:
            no_games.append(team["name"])
        show_no_games(no_games)

# option 8 show teams without wins 

def show_losseres(teams):
    losseres = []
    for team in teams:
        if team["played"] > 0 and team["wins"] == 0:
            losseres.append(team)
    print(f"\nthe losseres:\n{losseres}")

# option 9 show fame summary 

def get_game_summary(teams):
    teams_num = len(teams)
    games_num = 0
    goals_num = 0
    drow = 0
    for team in teams:
        games_num += int(team["played"])
        goals_num += int(team["goals_for"])
        drow += int(team["draws"])
    try:
        goals_avg = goals_num / (games_num / 2)
    except ZeroDivisionError:
        return False
    return [teams_num,games_num / 2,goals_num,drow / 2,goals_avg]

def show_game_summary(teams):
    if not teams:
        print("no teams yet! ")
    summary = get_game_summary(teams)
    if not summary:
        print("no games yet!")
    else:
        print()
        print("=== the game summary is: ===")
        print(f"teams: {summary[0]}")
        print(f"games: {int(summary[1])}")
        print(f"goals: {summary[2]}")
        print(f"drows: {int(summary[3])}")
        print(f"goals avg: {summary[4]}")
        sorted_teams = sort_teams(teams)
        print(f"the leading team:\n{sorted_teams[0]['name']} with {sorted_teams[0]['points']} points")















































        