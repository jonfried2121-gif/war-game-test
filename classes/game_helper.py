from classes.class_card import Card
from classes.class_player import Player




def game_printer(user:Player,user_card:Card,computer:Player,computer_card:Card,winner:Player):
    print("-------- TURN -------")
    print(user ," : ", user_card)
    print(computer , " : " , computer_card)
    if winner == "Draw":
        print("its a Draw")
    else:
        print(winner," has won the game")
    print(f"player cards: {len(user.cards)} | computer cards : {len(computer.cards)}")
    print("================")
    


