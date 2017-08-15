import unittest
import poker


class TestStringMethods(unittest.TestCase):
    def test_hand(self):
        a = poker.PokerHand('QH QS TH TD TS')
        self.assertEqual(a.evaluate(), ('FH', True, 7))

    def test_hand2(self):
        a = poker.PokerHand('2H 3C 4H 5D 6S')
        self.assertEqual(a.evaluate(), ('S', True, 5))

    def test_hand3(self):
        a = poker.PokerHand('QH AH KH TH JH')
        self.assertEqual(a.evaluate(), ('RF', True, 10))

    def test_hand4(self):
        a = poker.PokerHand('QH 3S 5H 7D 9S')
        self.assertEqual(a.evaluate(), ('HC', 'QH', 1))

    def test_hand5(self):
        a = poker.PokerHand('QH QS QH 5D TS')
        self.assertEqual(a.evaluate(), ('THREE', True, 4))

    def test_hand6(self):
        a = poker.PokerHand('QH QS 9H 9D TS')
        self.assertEqual(a.evaluate(), ('TP', True, 3))

    def test_hand7(self):
        a = poker.PokerHand('AH AS AC AD TS')
        self.assertEqual(a.evaluate(), ('FOUR', True, 8))

    def test_compare(self):
        a = poker.PokerHand('AH AS AC AD TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS 9H 9D TS'), 'Win')

    def test_compare2(self):
        a = poker.PokerHand('2H 4S 6C 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS 9H 9D TS'), 'Loss')

    def test_compare3(self):
        a = poker.PokerHand('AH AS AC AD TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('AH AS AD AC TS'), 'Tie')

    def test_compare4(self):
        a = poker.PokerHand('8H 8S 8C 3D 3S')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('TH JS QH KD AS'), 'Win')

    def test_compare5(self):
        a = poker.PokerHand('AH AS AC 8D TS')
        aval = a.evaluate()
        self.assertEqual(a.compare_with('QH QS QC QD TS'), 'Loss')


if __name__ == '__main__':
    unittest.main()
