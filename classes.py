import random

class Card:
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
    
    def __repr__(self):
        return self.meaning
    
class TarotDeck:
    def __init__(self, cards):
        self.cards = [Card(card[0], card[1]) for card in cards]

    def shuffle(self):
        self.cards.shuffle()

    def pullCard(self):
        if len(self.cards) == 0:
            print("There's no more cards on the deck.")
            return None
        else:
            cardTaken = self.cards.pop()
            return cardTaken
        
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getCard(self,deck):
        self.hand.append(deck.pullCard())

    def showHand(self):
        for card in self.hand:
            print("{0}: {1}".format(card.name, card.meaning))