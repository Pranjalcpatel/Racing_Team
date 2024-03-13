# Design a class called Deck that represents a standard deck of playing cards.  The class should:

# Have an initializer __init__(self) that creates a full deck of 52 cards (4 suits: Spades, Hearts, Diamonds, Clubs; 13 ranks: Ace, 2-10, Jack, Queen, King). You can represent a card as a tuple containing (suit, rank).
# Include methods:
# shuffle(self): This method shuffles the deck randomly. (Hint: Use the random module).
# deal_card(self): This method removes and returns the top card from the deck. If the deck is empty, raise a ValueError exception.
# Consider implementing additional methods (optional):
# cards_remaining(self): This method returns the number of cards remaining in the deck.
# deal_n_cards(self, n): This method deals a specified number of cards (n) from the deck and returns them as a list. Raise a ValueError if there are not enough cards remaining.

import random
class Deck:
    def __init__(self):
        suits=["Spades","Hearts","Diamond","Clubs"]
        self.deck=[]
        for i in range(1,14):
            for j in range(4):
                self.deck.append((suits[j],i))

    def shuffle(self):
        random.shuffle(self.deck)
    def deal_card(self):
        if len(self.deck)==0:
            print("DECK IS EMPTY")
            return
        else:
            card=self.deck[0]
            self.deck.remove(self.deck[0])
            return card
    def cards_remaining(self):
        return len(self.deck)
    def deal_n_cards(self,n):
        if self.cards_remaining()<n:
            print(f"The deck contains less than {n} cards")
            return
        else:
            for i in range(n):
                print(self.deal_card())
        return
        
my_deck=Deck()
my_deck.shuffle()
print(my_deck.deal_n_cards(45))
print(my_deck.cards_remaining())

    