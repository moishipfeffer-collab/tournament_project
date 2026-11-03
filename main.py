from menu import add_new_team,show_menu

def main():
    teams = []
    while True:
        choise = show_menu()
        if choise == "1":
            teams = add_new_team(teams)
        elif choise == "2":
            if teams:
                print(teams)
            else:
                print("the team list is empty")
        elif choise == "0":
            break
main()
