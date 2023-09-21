# cards.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: my brother

import random

values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

clubs = "\u2663"
diamonds = "\u2666"
hearts = "\u2665"
spades = "\u2660"

suits = [clubs,diamonds,hearts,spades] #unicode symbols for suits



class playing_card:

    suits = {"clubs":"♣", "diamond":"♦","heart": "♥", "spade": "♠"}
    num_to_face = {1: "A", 11: "J", 12: "Q", 13: "K"}   #made dictionaries to translate letters to numbers, not implemented yet
    face_to_num = {"A": 1, "J": 11, "Q": 12, "K": 13}

    def __init__(self,face_value,suit):  #constructor, takes a face value and a suit
        self.face_value = face_value
        self.suit = suit

    def print_val(self):
        #return f"This card is the {self.face_value} of {self.suit}."
        return f"{self.face_value} {self.suit}."


    def compare(self, other):
        if self.face_value < other.face_value:
            return "<"
        elif self.face_value > other.face_value:
            return ">"
        else:
            return "=="


    def set_value(self,value):
        self.face_value = value

    def set_suit(self,suit):
        self.suit = suit

    def get_value(self):
        return self.face_value

    def get_suit(self):
        return self.suit

    def __str__(self):   #essentially toString in java
        return self.print_val()       

    def __add__(self,other):
        return self.face_value + other.face_value
    
    def __lt__(self,other):
        return self.face_value < other.face_value

    def __eq__(self,other):
        return self.face_value == other.face_value

    def __gt__(self, other):
        return self.face_value > other.face_value



class hand_of_cards:   

    def __init__(self):
        self.cards = []

    def add_card(self,playing_card, deck):
        self.cards.append(playing_card)
        deck.remove(playing_card)           #drawing a card from the deck to the hand means it gets removed from deck

    def remove_random(self, deck):
        random_choice = random.randrange(len(self.cards))
        self.cards.remove(random_choice)
        self.add_card(deck[0], deck)

    def print_hand(self):
        print("This hand has the following cards:")
        for card in self.cards:
            print(card)
        #print(self.cards)

    def __str__(self):
            print(self.cards)

    def has_match(self):
        match_count_master = 0

        for card in range(len(self.cards)):
            match_count = 1
            print(match_count,": per card")
            for next_card in range(card+1, len(self.cards)):
                
                if self.cards[card].compare(self.cards[next_card]) == "==":
                    match_count+= 1
                    print(match_count,"while counting")

                elif match_count > match_count_master:
                    match_count_master = match_count
        if match_count_master == 1:
            match_count_master = 0
        return match_count_master

    # each individual card that gets check needs a match counter
    # compare all match counts, return the highest one
    # if match_count is 1, then there is no match and you return 0



# Testing functions
card1 = playing_card("A", "spades")
card2 = playing_card("Q", "hearts")

card1.print_val()
print(card1.get_value())
print(card1.get_suit())
print(card2)
print(card1.compare(card2))

result = card1 + card2
print(result)


#create deck 
deck = [playing_card(value,suit) for value in values for suit in suits]

#my brother helped me write these two following functions to print out the deck neatly
def print_deck(deck):
    for card in deck:
        print(card, end=" ")
    print()

def print_deck_sorted(deck):
    for value in values:
        print(f"{value}: ", end=" ")
        for card in deck:
            if card.get_value()==value:
                print(card, end=" ")
        print()

print_deck_sorted(deck)

my_hand = hand_of_cards()

print("Shuffled deck:")
random.shuffle(deck)
print_deck(deck,)
print("\n")


for card in range(5):
    my_hand.add_card(deck[0],deck)      #pulls the top 5 cards in the list/deck. also removes those cards from the deck

my_hand.print_hand()

print("\nThe order of the shuffled deck is now:")
print_deck(deck)


#testing has_match

print("second deck: \n")
second_deck = [playing_card(value,suit) for value in values for suit in suits]
print_deck(second_deck)
new_hand = hand_of_cards()
new_hand.add_card(second_deck[0],second_deck)
new_hand.add_card(second_deck[0],second_deck)
new_hand.add_card(second_deck[0],second_deck)
new_hand.add_card(second_deck[0],second_deck)
new_hand.add_card(second_deck[28],second_deck)
new_hand.print_hand()

print(new_hand.has_match())

