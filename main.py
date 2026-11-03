from run_program import add_new_team,show_menu,add_result

def main():
    teams = []
    results = []
    while True:
        choise = show_menu()
        if choise == "1":
            teams = add_new_team(teams)
        elif choise == "2":
            if teams:
                print(teams)
            else:
                print("the team list is empty")
        elif choise == "3":
            add_result(results,teams)
        elif choise == "4":
            pass
        elif choise == "0":
            break
main()
