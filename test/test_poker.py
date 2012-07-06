import os
import re
import sys
import unittest


curdir = os.path.dirname(os.path.abspath(sys.argv[0]))
top = os.path.normpath(os.path.join(curdir, os.pardir))
sys.path.append(os.path.join(top, 'src'))

import poker


class PokerTestCase(unittest.TestCase):

    def setUp(self):
        self.cards = poker.Poker().play()

    def test_card_uniqueness(self):
        mismatched = False
        for card in self.cards:
            count = len([x for x in self.cards if x == card])
            if count > 1:
                mismatched = True
        self.assertFalse(mismatched)

    def test_card_suits(self):
        mismatched = False
        for card in self.cards:
            suit = card.split('-')[1]
            if suit not in ['S', 'D', 'C', 'H']:
                mismatched = True
        self.assertFalse(mismatched)

    def test_card_values(self):
        mismatched = False
        for card in self.cards:
            value = card.split('-')[0]
            if value not in ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                             '10', 'J', 'Q', 'K']:
                mismatched = True
        self.assertFalse(mismatched)

if __name__ == '__main__':
    unittest.main()

