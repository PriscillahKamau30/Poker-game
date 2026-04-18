from Card import Card
import random

class Deck():
    
    def __init__(self):
        ranks = Card.RANK
        suites = Card.SUITE
        deck = []
        
        for rank in ranks:
            for suite in suites:
                deck.append(Card(suite,rank))
                
        self.deck = deck
                
    def shuffle(self):
        if not self.deck:
            print('Deck is empty')
            return
        
        random.shuffle(self.deck)
        print('Deck shuffled successfully')
        
    def printDeck(self):
        for card in self.deck:
            print(card.printCard())
            print('------------------')
                    
    def burnCard(self):
        print("Card burned: " + self.deck[0].printCard())
        topCard = self.deck[0]
        self.deck.pop(0)
        self.deck.append(topCard)
    
    def giveCard(self):
        topCard = self.deck[0]
        self.deck.pop(0)
        return topCard