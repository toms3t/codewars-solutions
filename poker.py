# A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also
# online. Can you help them by writing an algorithm that can rank poker hands?
#
# Task:
#
# Create a poker hand that has a method to compare itself to another poker hand:
#     compare_with(self, other_hand)
# A poker hand has a constructor that accepts a string containing 5 cards:
#     PokerHand(hand)
# The characteristics of the string of cards are:
# A space is used as card seperator
# Each card consists of two characters
# The first character is the value of the card, valid characters are:
# 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
# The second character represents the suit, valid characters are:
# S(pades), H(earts), D(iamonds), C(lubs)
#
# The result of your poker hand compare can be one of these 3 options:
#     RESULT = ["Loss", "Tie", "Win"]
# Apply the Texas Hold'em rules for ranking the cards.
# There is no ranking for the suits.

# '2C 3H 4D 5S QH'


# 1. Royal Flush
# The best hand in poker, a "royal flush" is extremely rare, consisting of the highest possible straight (ace to ten)
# with all cards being the same suit.
# {A-Spades}{K-Spades}{Q-Spades}{J-Spades}{10-Spades} would represent a royal flush.
#
# 2. Straight Flush
# A straight flush is a five-card straight (that is, five cards of consecutive rank) with all five being the same suit.
# (A royal flush is an example of a straight flush — the highest one.)
# For example, {9-Hearts}{8-Hearts}{7-Hearts}{6-Hearts}{5-Hearts} is a straight flush and would beat even an ace-high
# flush.
#
# 3. Four of a kind
# Next comes four of a kind or "quads," that is, four cards of the same rank.
# A hand like {Q-Spades}{Q-Hearts}{Q-Clubs}{Q-Diamonds}{2-Clubs} is four of a kind and would beat any hand other than
# a straight flush or royal flush.
#
# 4. Full house
# A full house consists of three cards of the same rank along with two more cards of the same rank (in other words,
# three of a kind plus a pair). {J-Hearts}{J-Clubs}{J-Diamonds}{10-Clubs}{10-Diamonds} is an example of a full house
# and beats a flush, a straight, and all lesser-ranked hands.
#
# 5. Flush
# A flush consists of any five cards of the same suit, such as
# {K-Diamonds}{J-Diamonds}{7-Diamonds}{5-Diamonds}{2-Diamonds}. When comparing two flushes, the one containing the
# highest-ranked card is best. Therefore a flush containing an ace (an "ace-high flush") would beat this king-high flush
#
# 6. Straight
# A straight is made from any five cards consecutive in rank that are not all the same suit, such as
# {J-Hearts}{10-Clubs}{9-Diamonds}{8-Hearts}{7-Spades}. When comparing two straights, the one with the highest-ranking
# card is best, so this jack-high straight would beat a ten-high straight (going from ten to six) and all lower ones.
#
# 7. Three of a kind
# Making three of a kind or "trips" requires having three cards of the same rank among your five —
# for example, {6-Hearts}{6-Clubs}{6-Diamonds}{K-Spades}{9-Clubs}. Three aces is the best possible three of a kind to
# make, followed by three kings, three queens, and so forth.
#
# 8. Two pair
# Two pair involves having two cards of the same rank plus two more cards of the same rank among the five in your hand,
# such as {A-Clubs}{A-Diamonds}{5-Spades}{5-Hearts}{3-Clubs}. The best possible two-pair hand is aces and kings.
#
# 9. One pair
# Making one pair means having two cards of the same rank in your five-card poker hand, with the other three cards being
#  unpaired. For example, {K-Spades}{K-Hearts}{8-Spades}{7-Diamonds}{2-Clubs} would constitute a one-pair hand.
#
# 10. High card
# A "high card" hand consists of five unpaired cards that make neither a straight nor a flush, such as
# {A-Clubs}{K-Hearts}{J-Diamonds}{10-Spades}{8-Hearts}. The highest-ranked of the five cards determines its value, so
# an "ace-high" hand (such as this example) would beat a "king-high" hand, and so forth.


class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.hand = hand

    def evaluate(self):
        result = {'HC': 1,'OP': 2, 'TP': 3, 'TK': 4, 'S': 5, 'F': 6, 'FH': 7, 'FK': 8, 'SF': 9, 'RF': 10}
        royals = {'K': 12, 'J': 10, 'Q': 11, 'A': 13}
        hand = self.hand.split()
        values = [int(x[0]) for x in hand if x[0].isdigit()]
        suits = [x[1] for x in hand]
        print (suits)
        for value in self.hand:
            if value[0] in royals:
                values.append(royals[value])
        if
        print (values)


    def compare_with(self, other):
        pass



a = PokerHand('2C 3H 4D 5S QH')
print (a.evaluate())