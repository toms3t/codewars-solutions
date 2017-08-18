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

    CARDMAP = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}

    def __init__(self, hand):
        self.hand = hand.split()
        self.straight = False
        self.straight_val = 0
        self.one_pair = False
        self.one_pair_val = 0
        self.two_pair = False
        self.two_pair_higher = 0
        self.two_pair_lower = 0
        self.three = False
        self.three_val = 0
        self.four = False
        self.four_val = 0
        self.result = 0
        self.high_card = None
        self.high_card_val = 0
        self.flush = False
        self.flush_val = 0
        self.full_house = False
        self.straight_flush = False
        self.royal_flush = False
        self.score = 0
        self.values = []
        self.single_values = []

    def __str__(self):
        return self.hand

    def get_card_values(self):
        for card in self.hand:
            if card[0] in PokerHand.CARDMAP:
                self.values.append(PokerHand.CARDMAP[card[0]])
        self.values.sort()
        return self.values

    def evaluate(self):
        self.values = self.get_card_values()
        self.single_values = sorted([x for x in self.values if self.values.count(x) == 1])
        print(self.single_values)
        prev = self.values[0]
        i = 0
        highest = 0
        highsuit = ''
        for card in self.hand:
            if PokerHand.CARDMAP[card[0]] > highest:
                highest = PokerHand.CARDMAP[card[0]]
                highsuit = card[-1]
        self.high_card = str(PokerHand.CARDMAP_REVERSED[highest]) + highsuit
        self.score = self.values[-1]
        for val in self.values[1:]:
            if prev + 1 == val:
                prev = val
                i += 1
        if prev == self.values[-1] and i == 4:
            self.straight = True
            self.score = self.values[-1]
        for val in self.values:
            if self.values.count(val) == 2:
                self.one_pair = True
                self.score = val
                # self.score = self.tiebreaker(val)
            elif self.values.count(val) == 3:
                self.three = True
                self.score = val
            elif self.values.count(val) == 4:
                # self.one_pair = False
                # self.three = False
                self.four = True
                self.score = val
        if self.values.count(self.values[1]) == 2 and self.values.count(self.values[3]) == 2:
            self.two_pair = True
            self.two_pair_higher = max(self.values[1], self.values[3])
            self.two_pair_lower = min(self.values[1], self.values[3])
            self.score = self.two_pair_higher
        if self.values.count(self.values[0]) == 3:
            if self.values.count(self.values[-1]) == 2:
                self.full_house = True
                # val = 0
                # self.score = self.tiebreaker(val)
        elif self.values.count(self.values[0]) == 2:
            if self.values.count(self.values[-1]) == 3:
                self.full_house = True
                # val = 0
                # self.score = self.tiebreaker(val)
        concat = ''.join(self.hand)
        if concat.count('C') == 5:
            self.flush = True
            self.score = self.values[-1]
        elif concat.count('D') == 5:
            self.flush = True
            self.score = self.values[-1]
        elif concat.count('H') == 5:
            self.flush = True
            self.score = self.values[-1]
        elif concat.count('S') == 5:
            self.flush = True
            self.score = self.values[-1]

        if self.straight == True and self.flush == True:
            self.straight_flush = True
            self.score = self.values[-1]
            if sum(self.values) == 60:
                self.royal_flush = True
                self.score = 100

        if self.royal_flush:
            self.result = 10
            return 'RF', self.royal_flush, self.result
        if self.straight_flush:
            self.result = 9
            return 'SF', self.straight_flush, self.result
        if self.four:
            self.result = 8
            return 'FOUR', self.four, self.result
        if self.full_house:
            self.result = 7
            return 'FH', self.full_house, self.result
        if self.flush:
            self.result = 6
            return 'F', self.flush, self.result
        if self.straight:
            self.result = 5
            return 'S', self.straight, self.result
        if self.three:
            self.result = 4
            return 'THREE', self.three, self.result
        if self.two_pair:
            self.result = 3
            return 'TP', self.two_pair, self.result
        if self.one_pair:
            self.result = 2
            return 'OP', self.one_pair, self.result
        if self.high_card:
            self.result = 1
            return 'HC', self.high_card, self.result

    def tiebreaker(self, other_hand):
        if self.one_pair:
            kicker = self.find_highest_kicker(other_hand)
            if 'self' in kicker:
                return 'Win'
            elif 'other' in kicker:
                return 'Loss'
            else:
                return 'Tie'
        if self.two_pair:
            if self.two_pair_lower > other_hand.two_pair_lower:
                return 'Win'
            elif self.two_pair_lower < other_hand.two_pair_lower:
                return 'Loss'
            else:
                kicker = self.find_highest_kicker(other_hand)
                if 'self' in kicker:
                    return 'Win'
                elif 'other' in kicker:
                    return 'Loss'
        if self.flush:
            kicker = self.find_highest_kicker(other_hand)
            if 'self' in kicker:
                return 'Win'
            elif 'other' in kicker:
                return 'Loss'
            else:
                return 'Tie'
        if self.score == other_hand.score:
            for val in self.values[::-1]:
                if val != self.score:
                    self.score = val
                    break
            for val in other_hand.values[::-1]:
                if val != other_hand.score:
                    other_hand.score = val
                    break
        if self.high_card:
            kicker = self.find_highest_kicker(other_hand)
            if 'self' in kicker:
                return 'Win'
            elif 'other' in kicker:
                return 'Loss'
            else:
                return 'Tie'
        if self.score > other_hand.score:
            return "Win"
        elif self.score < other_hand.score:
            return "Loss"
        return "Tie"

    def get_result(self):
        if self.result > other_hand.result:
            print(self.result)
            print(other_hand.result)
            return "Win"
        if self.result < other_hand.result:
            print(self.result)
            print(other_hand.result)
            return 'Loss'
        return 'Tie'

    def find_highest_kicker(self, other_hand):
        for x, y in list(zip(self.single_values, other_hand.single_values))[::-1]:
            if x > y:
                return 'self' + str(x)
            elif x < y:
                return 'other_hand' + str(y)
        return 'Tie'

    def compare_with(self, other_hand):
        other_hand = PokerHand(other_hand)
        other_result = other_hand.evaluate()
        if self.full_house:
            for val in self.values:
                if self.values.count(val) == 3:
                    self.score = val
            for val in other_hand.values:
                if other_hand.values.count(val) == 3:
                    other_hand.score = val
                    # if self.score == other_hand.score:
                    #     for val in self.values:
                    #         if self.values.count(val) == 2:
                    #             self.score = val
                    #     for val in other_hand.values:
                    #         if other_hand.values.count(val) == 2:
                    #             other_hand.score = val
        if self.result > other_hand.result:
            print(self.result)
            print(other_hand.result)
            return "Win"
        if self.result < other_hand.result:
            print(self.result)
            print(other_hand.result)
            return 'Loss'

        # Tiebreakers
        if self.result == other_hand.result:
            if self.score > other_hand.score:
                return 'Win'
            elif self.score < other_hand.score:
                return 'Loss'
            else:
                if self.high_card:
                    return self.tiebreaker(other_hand)
                if self.one_pair:
                    return self.tiebreaker(other_hand)
                if self.two_pair:
                    return self.tiebreaker(other_hand)
                if self.flush:
                    return self.tiebreaker(other_hand)

            print('self', self.score)
            print('other hand', other_hand.score)


a = PokerHand('AS KS QS JS TS')
print(a.evaluate())
print(a.compare_with('AD KD QD JD TD'))

# b = PokerHand('3H QS 3H TD TS')
# print(b.evaluate())
