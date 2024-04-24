import random
from _ranks_ import ranks_of_cards
from _suits_ import suits_of_cards
from Card import Card

class Deck:
    
    def __init__(self,all = False):
        self.all_cards = []
        if all:
            for suit in suits_of_cards():
                for rank in ranks_of_cards():
                    self.all_cards.append(Card(rank,suit))

    def draw(self):
        return self.all_cards.pop(0)

    def suffle(self):
        random.shuffle(self.all_cards)

    def add_cards(self,cards):
        if type(cards) is list:
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
    
    def get_cards(self):
        return self.all_cards

    def rest_deck(self):
        self.all_cards = []

    def is_empty (self):
        return not self.all_cards 

    def get_len_of_deck(self):
        return len(self.all_cards)