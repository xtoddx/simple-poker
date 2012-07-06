import random


class Poker(object):
    def play(self):
        name_map = {
                0: 'A-S',
                1: '2-S',
                2: '3-S',
                3: '4-S',
                4: '5-S',
                5: '6-S',
                6: '7-S',
                7: '8-S',
                8: '9-S',
                9: '10-S',
                10: 'J-S',
                11: 'Q-S',
                12: 'K-S',

                13: 'A-D',
                14: '2-D',
                15: '3-D',
                16: '4-D',
                17: '5-D',
                18: '6-D',
                19: '7-D',
                20: '8-D',
                21: '9-D',
                22: '10-D',
                23: 'J-D',
                24: 'Q-D',
                25: 'K-D',

                26: 'A-C',
                27: '2-C',
                28: '3-C',
                29: '4-C',
                30: '5-C',
                31: '6-C',
                32: '7-C',
                33: '8-C',
                34: '9-C',
                35: '10-C',
                36: 'J-C',
                37: 'Q-C',
                38: 'K-C',

                39: 'A-H',
                40: '2-H',
                41: '3-H',
                42: '4-H',
                43: '5-H',
                44: '6-H',
                45: '7-H',
                46: '8-H',
                47: '9-H',
                48: '10-H',
                49: 'J-H',
                50: 'Q-H',
                51: 'K-H'}
        deck =  [0, 1, 2, 3, 4, 5, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33,
                 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                 49, 50, 51]
        hand = [-1, -1, -1, -1, -1]
        for i in range(len(hand)):
            pick = random.choice(deck)
            while pick in hand:
                pick = random.choice(deck)
            hand[i] = pick
        for i in range(len(hand)):
            hand[i] = name_map[hand[i]]
        return hand

if __name__ == '__main__':
    pick5 = Poker().play()
    for card in pick5:
        print card
