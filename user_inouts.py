from validations import check_empty,check_num

def get_input(message,user_input):
    while True:
        response = input(message)
        if check_empty(response):
            return response
        print(f"{user_input} can not be empty")

def get_team_name():
    while True:
        team_name = get_input("enter team name: ","name")
        if not check_num(team_name):
            return team_name.lower()
        print("name can not be a number")

def get_team_id(team_type:str | None = None):
    while True:
        if not team_type:
            team_id = get_input("enter team id: ","id")
        else:
            team_id = get_input(f"enter {team_type} team id: ","id")
        if check_num(team_id):
            return team_id
        print("id must be a positive number")

def get_goals(team_type):
    while True:
        goals_num = get_input(f"enter number of goals for {team_type}", "goals number")
        if check_num(goals_num):
            return goals_num
        print("the goals number must be a hole positive number")



