from _val_ import values_of_cards

values = values_of_cards()

class Card:
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"