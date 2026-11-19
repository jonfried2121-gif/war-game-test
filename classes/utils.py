

def game_menu():
    print("""1. play turn 
2. exit """)
    return

def new_game():
    print("""
1.new game
2. exit""")

def get_input():
    pick = input("enter a valid number: ")
    return pick

def number_validation(number):
    try:
        number = int(number)
        if number > 0:
            return str(number)
        print("unvalid number")
        return
    except ValueError:
        print("plese enter a valid number")
        return