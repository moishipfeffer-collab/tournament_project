def check_empty(variable: str):
    if variable.strip():
        return True
    return False

def check_num(num):
    try:
        return int(num) >= 1
    except ValueError:
        return False

          
def check_if_exists_id(id,teams:list):
    for team in teams:
        if team["id"] == id:
            return False
    return True

def check_if_exists_name(name:str,teams:list):
    for team in teams:
        if team["name"] == name:
            return False
    return True

    
def check_same_id(home,away):
    if home == away:
        return False
    return True

def check_played(id,teams):
    for team in teams:
        if team["id"] == id:
            if team["played"] > 0:
                return False
    return True



