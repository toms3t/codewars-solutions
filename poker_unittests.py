import unittest
import poker

class TestStringMethods(unittest.TestCase):
    def test_compare(self):
        '''
        Testing 4 aces beats two pair
        '''
        hand = poker.PokerHand('AH AS AC AD TS')
        other = poker.PokerHand('QH QS 9H 9D TS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare2(self):
        '''
        Testing high card loses to two pair
        '''
        hand = poker.PokerHand('2H 4S 6C 8D TS')
        other = poker.PokerHand('QH QS 9H 9D TS')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare3(self):
        '''
        Testing higher 4 of a kind wins
        '''
        hand = poker.PokerHand('AH AS AC AD TS')
        other = poker.PokerHand('KH KS KD KC TS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare4(self):
        '''
        Testing full house beats straight
        '''
        hand = poker.PokerHand('8H 8S 8C 3D 3S')
        other = poker.PokerHand('TH JS QH KD AS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare5(self):
        '''
        Testing full house loses to 4 of a kind
        '''
        hand = poker.PokerHand('AH AS AC 8D TS')
        other = poker.PokerHand('QH QS QC QD TS')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare6(self):
        '''
        Testing royal flush tie
        '''
        hand = poker.PokerHand('AS KS QS JS TS')
        other = poker.PokerHand('AH KH QH JH TH')
        self.assertEqual(hand.compare_with(other), 'Tie')

    def test_compare7(self):
        '''
        Testing higher straight wins
        '''
        hand = poker.PokerHand('3H 4S 5C 6D 7S')
        other = poker.PokerHand('4H 5S 6C 7D 8S')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare8(self):
        '''
        Testing straight tie
        '''
        hand = poker.PokerHand('3H 4S 5C 6D 7S')
        other = poker.PokerHand('3H 4S 5C 6D 7S')
        self.assertEqual(hand.compare_with(other), 'Tie')

    def test_compare9(self):
        '''
        Testing higher pair of two pair wins
        '''
        hand = poker.PokerHand('KH KS 8C 8D TS')
        other = poker.PokerHand('AH AS QC QD TS')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare10(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        hand = poker.PokerHand('AH AS AC 8D 8S')
        other = poker.PokerHand('QH QS QC TD TS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare11(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        hand = poker.PokerHand('5H 5S 5C 8D 8S')
        other = poker.PokerHand('QH QS QC 2D 2S')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare12(self):
        '''
        Testing higher card of a flush wins
        '''
        hand = poker.PokerHand('3H 5H 7H 8H TH')
        other = poker.PokerHand('QS 4S 3S 7S TS')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare13(self):
        '''
        Testing higher card of hand 4 of a kind wins
        '''
        hand = poker.PokerHand('8H 8S 8C 8D TS')
        other = poker.PokerHand('7H 7S 7C 7D TS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare14(self):
        '''
        Testing one pair beats high card
        '''
        hand = poker.PokerHand('8H 8S 4C 5D TS')
        other = poker.PokerHand('3H 5S 7C 9D AS')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_compare15(self):
        '''
        Testing higher card wins
        '''
        hand = poker.PokerHand('8H 5D 4C 2D TS')
        other = poker.PokerHand('3H 5S 7C 9D AS')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_compare16(self):
        '''
        Testing two pair tie
        '''
        hand = poker.PokerHand('8H 8D 4C 4D TS')
        other = poker.PokerHand('8S 8C 4S 4H TD')
        self.assertEqual(hand.compare_with(other), 'Tie')

    def test_compare17(self):
        '''
        Testing one pair tie
        '''
        hand = poker.PokerHand('8H 8D 5C 4D TS')
        other = poker.PokerHand('8S 8C 5S 4H TD')
        self.assertEqual(hand.compare_with(other), 'Tie')

    def test_compare18(self):
        '''
        Testing high card tie
        '''
        hand = poker.PokerHand('2H 4D 6C 8D TS')
        other = poker.PokerHand('2S 4C 6S 8H TD')
        self.assertEqual(hand.compare_with(other), 'Tie')

    def test_ace_as_one(self):
        '''
        Testing ace used as a 1 in a straight
        '''
        hand = poker.PokerHand('AH 2D 3C 4D 5S')
        other = poker.PokerHand('2S 2C 6S 6H TD')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_ace_as_one_straight_flush(self):
        '''
        Testing ace used as a 1 in a straight flush
        '''
        hand = poker.PokerHand('AH 2H 3H 4H 5H')
        other = poker.PokerHand('2S 2C 6S 6H TD')
        self.assertEqual(hand.compare_with(other), 'Win')

    def test_ace_as_one_straight_flush_loses(self):
        '''
        Testing ace used as a 1 in a straight flush
        '''
        hand = poker.PokerHand('AH 2H 3H 4H 5H')
        other = poker.PokerHand('2S 3S 4S 5S 6S')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_ace_as_one_straight_loses(self):
        '''
        Testing ace used as a 1 in a straight flush
        '''
        hand = poker.PokerHand('AD 2C 3H 4C 5H')
        other = poker.PokerHand('2C 3H 4S 5S 6S')
        self.assertEqual(hand.compare_with(other), 'Loss')

    def test_full_house_tiebreaker(self):
        '''
        Testing ace used as a 1 in a straight flush
        '''
        hand = poker.PokerHand('KH KC 3S 3H 3D')
        other = poker.PokerHand('2H 2C 3S 3H 3D')
        self.assertEqual(hand.compare_with(other), 'Win')

if __name__ == '__main__':
    unittest.main()
