#!/usr/bin/env python3
"""
Poker hands

Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    
    The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD          Player 2
                Pair of Fives           Pair of Eights
	 	
2	 	5D 8C 9S JS AC          2C 5C 7D 8S QH          Player 1
                Highest card Ace        Highest card Queen
	 	
3	 	2D 9C AS AH AC          3D 6D 7D TD QD          Player 2
                Three Aces              Flush with Diamonds
	 	
4	 	4D 6S 9H QH QC          3D 6D 7H QD QS          Player 1
                Pair of Queens          Pair of Queens
                Highest card Nine	Highest card Seven
	 	
5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D          Player 1
                Full House              Full House
                With Three Fours        with Three Threes
	 	
                 
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import Counter


class Card:
    suit = None
    value = None
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    def __init__(self, card):
        self.suit = card[1]
        self.value = card[0]        
        
    @property
    def card_value(self):
        i = 0
        while i < len(Card.VALUES):
            if self.value == Card.VALUES[i]:
                return i + 1
            i += 1
        
    
class Hand:
    cards = None
    
    def get_cards(self, cards):
        self.cards = []
        for card in cards:
            self.cards.append(Card(card))
    
    def has_cards(self):
        return len(self.cards) == 5
    
    def values(self):
        return [card.value for card in self.cards]
    
    def suits(self):
        return [card.suit for card in self.cards]
    
    def has_royal_flush(self):
        values = self.values()
        return self.has_flush() and \
               ('A' in values) and \
               ('K' in values) and \
               ('Q' in values) and \
               ('J' in values) and \
               ('10' in values)
    
    def has_flush(self):
        suits = self.suits()
        return len(list(set(suits))) == 1
    
    def has_straight(self):
        values = sorted([card.card_value for card in self.cards])
        d = []
        i = 0
        while i < 4:
            d.append(values[i + 1] - values[i])
            i += 1
        return len(list(set(d))) == 1
    
    def has_straight_flush(self):
        return self.has_straight() and self.has_flush()
    
    def has_four_of_kind(self):
        counter = Counter(self.values())
        for key in counter:
            if counter[key] == 4:
                return True
        return False
        
    def has_full_house(self):
        counter = Counter(self.values())
        return sorted([x[1] for x in counter.items()]) == [2, 3]
    
    def has_three_of_kind(self):
        counter = Counter(self.values())
        for key in counter:
            if counter[key] == 3:
                return True
        return False
            
    def has_two_pairs(self):
        counter = Counter(self.values())
        return sorted([x[1] for x in counter.items()]) == [1, 2, 2]
    
    def has_pair(self):
        counter = Counter(self.values())
        return 2 in [x[1] for x in counter.items()]
    
    def high_card(self):
        return max([card.card_value for card in self.cards])

    def pair_card(self):
        cards = sorted([card.card_value for card in self.cards])
        i = 0
        while i < len(cards) + 1:
            if cards[i] == cards[i + 1]:
                return cards[i]
            i += 1
        
    def rank(self):
        if self.has_royal_flush():
            return 10
        if self.has_straight_flush():
            return 9
        if self.has_four_of_kind():
            return 8
        if self.has_full_house():
            return 7
        if self.has_flush():
            return 6
        if self.has_straight():
            return 5
        if self.has_three_of_kind():
            return 4
        if self.has_two_pairs():
            return 3
        if self.has_pair():
            return 2
        return 1


def win_by_senior_card(hand1, hand2):
    high1 = hand1.high_card()
    high2 = hand2.high_card()
    if high1 > high2:
        return 1
    if high1 < high2:
        return 2
    # ==
    cards1 = sorted(
        [card.card_value for card in hand1.cards], reverse=True)
    cards2 = sorted(
        [card.card_value for card in hand2.cards], reverse=True)
    if cards1 > cards2:
        return 1
    if cards1 < cards2:
        return 2
    return 0

def win_by_pair(hand1, hand2):
    card1 = hand1.pair_card()
    card2 = hand2.pair_card()
    if card1 > card2:
        return 1
    if card1 < card2:
        return 2
    # ==
    cards1 = sorted(
        [card.card_value for card in hand1.cards if card.card_value != card1], 
        reverse=True)
    cards2 = sorted(
        [card.card_value for card in hand2.cards if card.card_value != card1], 
        reverse=True)
    if cards1 > cards2:
        return 1
    if cards1 < cards2:
        return 2
    return 0
    
def who_win(hand1, hand2):
    # rank1 == rank2
    rank = hand1.rank()
    if rank == 1:
        return win_by_senior_card(hand1, hand2)
    if rank == 2:
        return win_by_pair(hand1, hand2)
    return None


with open('p054_poker.txt') as f:
    lines = f.readlines()

hand1 = Hand()
hand2 = Hand()
win = {
    2: 0, 
    0: 0, 
    1: 0
}
ranks = {}
for i in range(1, 11):
    ranks[i] = 0
    
for line in lines:
    # print(line)
    cards = line.split()
    one_cards = cards[:5]
    two_cards = cards[5:]
    print(one_cards, two_cards)
    hand1.get_cards(one_cards) 
    hand2.get_cards(two_cards) 

    rank1 = hand1.rank()
    rank2 = hand2.rank()
    print(rank1, rank2)
    if rank1 > rank2:
        win[1] += 1
    if rank1 < rank2:
        win[2] += 1
    if rank1 == rank2:
        ranks[rank1] += 1
        result = who_win(hand1, hand2)
        print(f'game result {result}')
        win[result] += 1

    
    
print(len(lines))
print(win)
print(ranks)




