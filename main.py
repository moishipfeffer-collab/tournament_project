from run_program import add_new_team_flow,show_menu,show_teams,add_result_flow,show_sort_team_flow,show_liding_team
from run_program import show_best_teams,show_succes_rate,show_losseres,show_game_summary
from storage import load_from_json,teams_file,played_file

def main():
    results = []
    while True:
        teams = load_from_json(teams_file)
        played = load_from_json(played_file)
        choise = show_menu()
        if choise == "1":
            teams = add_new_team_flow(teams) 
        elif choise == "2":
            show_teams(teams)
        elif choise == "3":
            add_result_flow(results,teams,played)
        elif choise == "4":
           show_sort_team_flow(teams) 
        elif choise == "5":
            show_liding_team(teams)
        elif choise == "6":
            show_best_teams(teams)
        elif choise == "7":
            show_succes_rate(teams)
        elif choise == "8":
            show_losseres(teams)
        elif choise == "9":
            show_game_summary(teams)
        elif choise == "0":
            print("goodby!")
            break

if __name__ == "__main__":
    main()
