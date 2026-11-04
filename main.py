from run_program import add_new_team_flow,show_menu,show_teams,add_result_flow

def main():
    teams = []
    results = []
    while True:
        choise = show_menu()
        if choise == "1":
            teams = add_new_team_flow(teams)
        elif choise == "2":
            show_teams(teams)
        elif choise == "3":
            add_result_flow(results,teams)
        elif choise == "4":
            pass
        elif choise == "0":
            break
main()
