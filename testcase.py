import unittest
import poker


class TestStringMethods(unittest.TestCase):
    def test_hand(self):
        '''
        Testing Full House
        '''
        a = poker.PokerHand('QH QS TH TD TS')
        self.assertEqual(a.evaluate(), ('FH', True, 7))

    def test_hand2(self):
        '''
        Testing Straight
        '''
        a = poker.PokerHand('2H 3C 4H 5D 6S')
        self.assertEqual(a.evaluate(), ('S', True, 5))

    def test_hand3(self):
        '''
        Testing Royal Flush
        '''
        a = poker.PokerHand('QH AH KH TH JH')
        self.assertEqual(a.evaluate(), ('RF', True, 10))

    def test_hand4(self):
        '''
        Testing High Card
        '''
        a = poker.PokerHand('QH 3S 5H 7D 9S')
        self.assertEqual(a.evaluate(), ('HC', 'QH', 1))

    def test_hand5(self):
        '''
        Testing three of a kind
        '''
        a = poker.PokerHand('QH QS QH 5D TS')
        self.assertEqual(a.evaluate(), ('THREE', True, 4))

    def test_hand6(self):
        '''
        Testing two pair
        '''
        a = poker.PokerHand('QH QS 9H 9D TS')
        self.assertEqual(a.evaluate(), ('TP', True, 3))

    def test_hand7(self):
        '''
        Testing four of a kind
        '''
        a = poker.PokerHand('AH AS AC AD TS')
        self.assertEqual(a.evaluate(), ('FOUR', True, 8))

    def test_hand8(self):
        '''
        Testing High Card
        '''
        a = poker.PokerHand('2H 4S 6C 9D TS')
        self.assertEqual(a.evaluate(), ('HC', 'TS', 1))

    def test_hand9(self):
        '''
        Testing one pair
        '''
        a = poker.PokerHand('9H 9S 2C 4D TS')
        self.assertEqual(a.evaluate(), ('OP', True, 2))

    def test_compare(self):
        '''
        Testing 4 aces beats two pair
        '''
        a = poker.PokerHand('AH AS AC AD TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS 9H 9D TS'), 'Win')

    def test_compare2(self):
        '''
        Testing high card loses to two pair
        '''
        a = poker.PokerHand('2H 4S 6C 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS 9H 9D TS'), 'Loss')

    def test_compare3(self):
        '''
        Testing higher 4 of a kind wins
        '''
        a = poker.PokerHand('AH AS AC AD TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('KH KS KD KC TS'), 'Win')

    def test_compare4(self):
        '''
        Testing full house beats straight
        '''
        a = poker.PokerHand('8H 8S 8C 3D 3S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('TH JS QH KD AS'), 'Win')

    def test_compare5(self):
        '''
        Testing full house loses to 4 of a kind
        '''
        a = poker.PokerHand('AH AS AC 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS QC QD TS'), 'Loss')

    def test_compare6(self):
        '''
        Testing royal flush tie
        '''
        a = poker.PokerHand('AS KS QS JS TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('AH KH QH JH TH'), 'Tie')

    def test_compare7(self):
        '''
        Testing higher straight wins
        '''
        a = poker.PokerHand('3H 4S 5C 6D 7S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('4H 5S 6C 7D 8S'), 'Loss')

    def test_compare8(self):
        '''
        Testing straight tie
        '''
        a = poker.PokerHand('3H 4S 5C 6D 7S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('3H 4S 5C 6D 7S'), 'Tie')

    def test_compare9(self):
        '''
        Testing higher pair of two pair wins
        '''
        a = poker.PokerHand('KH KS 8C 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('AH AS QC QD TS'), 'Loss')

    def test_compare10(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        a = poker.PokerHand('AH AS AC 8D 8S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS QC TD TS'), 'Win')

    def test_compare11(self):
        '''
        Testing higher 3 of a kind in a full house wins
        '''
        a = poker.PokerHand('5H 5S 5C 8D 8S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS QC 2D 2S'), 'Loss')

    def test_compare12(self):
        '''
        Testing higher card of a flush wins
        '''
        a = poker.PokerHand('3H 5H 7H 8H TH')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QS 4S 3S 7S TS'), 'Loss')

    def test_compare13(self):
        '''
        Testing higher card of a 4 of a kind wins
        '''
        a = poker.PokerHand('8H 8S 8C 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('7H 7S 7C 7D TS'), 'Win')

    def test_compare14(self):
        '''
        Testing one pair beats high card
        '''
        a = poker.PokerHand('8H 8S 4C 5D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('3H 5S 7C 9D AS'), 'Win')

    def test_compare15(self):
        '''
        Testing higher card wins
        '''
        a = poker.PokerHand('8H 5D 4C 2D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('3H 5S 7C 9D AS'), 'Loss')

if __name__ == '__main__':
    unittest.main()
