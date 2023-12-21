import random

class Card:
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
    
    def __repr__(self):
        return '{0}: {1}'.format(self.name, self.meaning)
    
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

cards = [
    ['The Fool', 'Represents new beginnings, adventures, and a carefree approach.'],
    ['The Magician', 'Symbolizes creative power, manifestation, and unlimited potential.'],
    ['The High Priestess', 'Represents intuition, hidden mysteries, and inner knowledge.'],
    ['The Empress', 'Symbolizes femininity, fertility, and creativity.'],
    ['The Emperor', 'Represents authority, stability, and structure.'],
    ['The Hierophant', 'Symbolizes spirituality, tradition, and connection to the divine.'],
    ['The Lovers', 'Represents significant choices, relationships, and duality.'],
    ['Justice', 'Symbolizes fairness, balance, and making just decisions.'],
    ['The Hermit', 'Represents inner search, wisdom, and spiritual retreat.'],
    ['Wheel of Fortune', 'Symbolizes the cycle of life, change, and evolution.'],
    ['Strenght', 'Represents inner strength, courage, and controlling impulses.'],
    ['The Hanged Man', 'Symbolizes surrender, letting go, and gaining a new perspective.'],
    ['Death', 'Represents transformation, change, and rebirth.'],
    ['Temperance', 'Symbolizes harmony, moderation, and seeking balance.'],
    ['The Devil', 'Represents temptation, material bondage, and liberation.'],
    ['The Tower', 'Symbolizes the destruction of outdated structures to allow change.'],
    ['The Star', 'Represents hope, inspiration, and spiritual connection.'],
    ['The Moon', 'Symbolizes intuition, confusion, and illusion.'],
    ['The Sun', 'Represents clarity, joy, and vitality.'],
    ['Judgement', 'Symbolizes evaluation, renewal, and accepting consequences.'],
    ['The World', 'Represents fulfillment, integration, and complete success.']
]

mainDeck = TarotDeck(cards)