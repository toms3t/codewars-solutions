import unittest
import poker

class TestStringMethods(unittest.TestCase):
    def test_compare(self):
        '''
        Testing 4 aces beats two pair
        '''
        hand = poker.PokerHand('AH AS AC AD TS')
        self.assertEqual(hand.compare_with('QH QS 9H 9D TS'), 'Win')

    def test_compare2(self):
        '''
        Testing high card loses to two pair
        '''
        hand = poker.PokerHand('2H 4S 6C 8D TS')
        self.assertEqual(hand.compare_with('QH QS 9H 9D TS'), 'Loss')

    def test_compare3(self):
        '''
        Testing higher 4 of a kind wins
        '''
        hand = poker.PokerHand('AH AS AC AD TS')
        self.assertEqual(hand.compare_with('KH KS KD KC TS'), 'Win')

    def test_compare4(self):
        '''
        Testing full house beats straight
        '''
        hand = poker.PokerHand('8H 8S 8C 3D 3S')
        self.assertEqual(hand.compare_with('TH JS QH KD AS'), 'Win')

    def test_compare5(self):
        '''
        Testing full house loses to 4 of a kind
        '''
        hand = poker.PokerHand('AH AS AC 8D TS')
        self.assertEqual(hand.compare_with('QH QS QC QD TS'), 'Loss')

    def test_compare6(self):
        '''
        Testing royal flush tie
        '''
        hand = poker.PokerHand('AS KS QS JS TS')
        self.assertEqual(hand.compare_with('AH KH QH JH TH'), 'Tie')

    def test_compare7(self):
        '''
        Testing higher straight wins
        '''
        hand = poker.PokerHand('3H 4S 5C 6D 7S')
        self.assertEqual(hand.compare_with('4H 5S 6C 7D 8S'), 'Loss')

    def test_compare8(self):
        '''
        Testing straight tie
        '''
        hand = poker.PokerHand('3H 4S 5C 6D 7S')
        self.assertEqual(hand.compare_with('3H 4S 5C 6D 7S'), 'Tie')

    def test_compare9(self):
        '''
        Testing higher pair of two pair wins
        '''
        hand = poker.PokerHand('KH KS 8C 8D TS')
        self.assertEqual(hand.compare_with('AH AS QC QD TS'), 'Loss')

    def test_compare10(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        hand = poker.PokerHand('AH AS AC 8D 8S')
        self.assertEqual(hand.compare_with('QH QS QC TD TS'), 'Win')

    def test_compare11(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        hand = poker.PokerHand('5H 5S 5C 8D 8S')
        self.assertEqual(hand.compare_with('QH QS QC 2D 2S'), 'Loss')

    def test_compare12(self):
        '''
        Testing higher card of a flush wins
        '''
        hand = poker.PokerHand('3H 5H 7H 8H TH')
        self.assertEqual(hand.compare_with('QS 4S 3S 7S TS'), 'Loss')

    def test_compare13(self):
        '''
        Testing higher card of hand 4 of a kind wins
        '''
        hand = poker.PokerHand('8H 8S 8C 8D TS')
        self.assertEqual(hand.compare_with('7H 7S 7C 7D TS'), 'Win')

    def test_compare14(self):
        '''
        Testing one pair beats high card
        '''
        hand = poker.PokerHand('8H 8S 4C 5D TS')
        self.assertEqual(hand.compare_with('3H 5S 7C 9D AS'), 'Win')

    def test_compare15(self):
        '''
        Testing higher card wins
        '''
        hand = poker.PokerHand('8H 5D 4C 2D TS')
        self.assertEqual(hand.compare_with('3H 5S 7C 9D AS'), 'Loss')

    def test_compare16(self):
        '''
        Testing two pair tie
        '''
        hand = poker.PokerHand('8H 8D 4C 4D TS')
        self.assertEqual(hand.compare_with('8S 8C 4S 4H TD'), 'Tie')

    def test_compare17(self):
        '''
        Testing one pair tie
        '''
        hand = poker.PokerHand('8H 8D 5C 4D TS')
        self.assertEqual(hand.compare_with('8S 8C 5S 4H TD'), 'Tie')

    def test_compare18(self):
        '''
        Testing high card tie
        '''
        hand = poker.PokerHand('2H 4D 6C 8D TS')
        self.assertEqual(hand.compare_with('2S 4C 6S 8H TD'), 'Tie')

if __name__ == '__main__':
    unittest.main()
