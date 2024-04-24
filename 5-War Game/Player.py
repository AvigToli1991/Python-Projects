from Deck import Deck

class player:
    
    def __init__(self,name):
        self.name = name
        self.main_deck = Deck()
        self.sub_deck = Deck()

    def create_main(self,deck):
        for i in range(26):
             self.main_deck.add_cards(deck.draw())
        print(f"Create {self.name}'s main deck")

    def add_cards(self,cards):
        print(f"Adding cards to {self.name}'s sub deck")
        self.sub_deck.add_cards(cards)

    def suffle(self):
        self.main_deck.suffle()

    def ref_deck(self):
        print(f"refreshing {self.name}'s main deck")
        self.main_deck.add_cards(self.sub_deck.all_cards)
        self.suffle()
        self.sub_deck.rest_deck()

    def draw_one(self):
        if self.main_deck.is_empty():
            print(f"{self.name}'s deck empty! Check in sub deck...")
            if not self.sub_deck.is_empty():
                self.ref_deck()
            else:
                print(f"{self.name} have no cards left ")
                return 0
        print(f"{self.name}'s draw :")
        return self.main_deck.draw()

    def get_len_of_deck(self):
        return self.main_deck.get_len_of_deck() + self.sub_deck.get_len_of_deck()

    def is_empty(self):
        return self.get_len_of_deck() == 0

    def __str__(self):
        return f"{self.name} have {self.get_len_of_deck()} cards in total"