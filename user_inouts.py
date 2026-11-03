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
            return team_name
        print("name can not be a number")

def get_team_id():
    while True:
        team_id = get_input("enter team id: ","id")
        if check_num(team_id):
            return team_id
        print("id must be a positive number")



