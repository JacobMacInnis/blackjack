import random
from variables import suits, ranks
from card import Card

class Deck:
    
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks: 
                # Create the Card Object
                created_card = Card(suit,rank)
                self.deck.append(created_card)
    
    def __str__(self):
        return f'Deck of {len(self.deck)} Cards'

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()