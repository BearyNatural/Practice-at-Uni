# card game Class style

# program must have a 'deck' (Deck Class) which is a list of all 52 cards in a deck of playing cards
class Card:
    def __init__(self, value, points, colour):
        self.value = value
        self.points = points
        self.suit = colour
    def show(self):
        return f"{self.value} of {self.suit}"
    def points_value(self):
    #     if self.points == "King:":
    #         points = 13
    #     if self.points == "Queen":
    #         points = 12
    #     if self.points == "Jack":
    #         points = 11
    #     if self.points == "Ace":
    #         points = 1
        return f"equals {self.points} points"

class Deck:
    def __init__(self):
        self.cards = []
        self.build
    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for no in range(1, 14):
                self.cards.append(Card(s, no))
    def show(self):
        for c in self.cards:
            c.show

# Step 1 test:
c1 = Card("King", 13, "Hearts")
c1.show()
c1.points_value()

# Step 2 test:
deck = Deck()
deck.build()
deck.show()

# test
print(deck.build())
print(c1.show())
print(c1.points_value())