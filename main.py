from classes.class_game import Game
from classes.class_player import Player
from classes.utils import game_menu,get_input,number_validation,new_game



def game_manager():
    
    first = True
    while first:
        flag = True
        user = Player("Player")
        computer = Player("Computer")
        game = Game(user,computer)
        game.deck_creater()
        game.shuffle()
        game.hand_deck()
        new_game()
        pick = get_input()
    
        if not number_validation(pick):
            continue
        if pick =="1":
            while flag:
                game_menu()
                pick2 = get_input()
                if not number_validation(pick):
                    continue
                if pick2 == "1":
                    game.play_turn()
                    continue
                if pick2 == "2":
                    flag = False
                else:
                    print("please enter a valid number")
                    continue
                
        if pick == "2":
            first = False
        else:
            print("please pick a valid number")
        
        
game_manager()
