# A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?
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



class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        pass

    def compare_with(self, other):
        pass



