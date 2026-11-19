from classes.class_card import Card

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []

    def add_card(self,card:Card):
        self.cards.insert(0,card)

    def do_turn(self)->Card:
        return self.cards.pop()

    def show_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        return f"{self.name}"

        