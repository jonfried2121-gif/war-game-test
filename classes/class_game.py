from classes.class_card import Card
from classes.class_player import Player 
import random
from classes.game_helper import game_printer

class Game:
    def __init__(self,user:Player,computer:Player):
        self.user = user
        self.computer = computer
        self.deck = []

    
    def deck_creater(self):
        for i in range(2,15):
            for char in ["H","D","S","C"]:
                new = Card(i,char)
                self.deck.append(new)
        return
            
    def get_dec(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        for i in range(1000):
            index_start = random.randint(0,51)
            index_end = random.randint(0,51)
            if index_start == index_end:
                continue
            card_one = self.deck.pop(index_start)
            self.deck.insert(index_end,card_one)

        return

    def hand_deck(self):
        for i in range(0,len(self.deck),2):
            self.user.add_card(self.deck[i])
            self.computer.add_card(self.deck[i+1])
        return

    def play_turn(self):
        user_card = self.user.do_turn()
        computer_card = self.computer.do_turn()
        winner = self.get_winner(user_card,computer_card)
        self.card_selector(winner,computer_card,user_card)
        game_printer(self.user,user_card,self.computer,computer_card,winner)
        

    def get_winner(self,user_card:Card,computer_card:Card):
        if user_card.value == computer_card.value:
            winer = "Draw"
        else:
            winer = self.user if user_card.value > computer_card.value else self.computer
        return winer

    def card_selector(self,winner,computer_card,user_card):
        if winner == self.user:
            self.user.add_card(computer_card)
            self.user.add_card(user_card)
        elif winner == self.computer:
            self.computer.add_card(user_card)
            self.computer.add_card(computer_card)
        else:
            self.user.add_card(user_card)
            self.computer.add_card(computer_card)
        
    

        

    
        




    


            


