import random
from collections import Counter
import threading
import time
import queue
import poker
import sys
import logging

logging.basicConfig(filename='Poker', level=logging.INFO)

suits = ['S', 'D', 'C', 'H']
nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDMAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

CARDMAP_REVERSED = {val: key for key, val in CARDMAP.items()}
COUNT = 0
SF = 0
RF = 0
FOUR = 0
THREE = 0
TP = 0
FLUSH = 0
STRAIGHT = 0
OP = 0
FH = 0
H = ''
HANDS = 0
BEST = 0
BHAND = ''


def hand_builder(q):
    SF = []
    o = 0
    for i in range(2030):
        name = threading.current_thread().getName()
        print('Thread: {0} start put hand into queue[current size = {1}] at time = {2} \n'.format(name,
                                                                                                  q.qsize(),
                                                                                                  time.strftime(
                                                                                                      '%H:%M:%S')))
        o += 1
        hand = []
        while len(hand) <= 4:
            if len(hand) == 5: break
            card = random.choice(nums) + random.choice(suits)
            if card not in hand:
                hand.append(card)
        q.put(hand)
        global HANDS
        HANDS += 1
        print("Thread: {0} successfully put hand {1} into queue[current size = {2}] at time = {3} \n"
              .format(name, hand, q.qsize(), time.strftime('%H:%M:%S')))

        q.join()


def identify_hand(q):
    while True:
        try:
            name = threading.currentThread().getName()
            print("Thread: {0} start get hand from queue[current size = {1}] at time = {2} \n"
                  .format(name, q.qsize(), time.strftime('%H:%M:%S')))
            hand = ' '.join(q.get())
            h = poker.PokerHand(hand)
            # print (h.result, h.hand, h.high_card)
            global BEST
            if int(h.result) > BEST:
                BEST = int(h.result)
                global BHAND
                BHAND = h.best_hand
                global H
                H = h.hand
            if h.straight_flush:
                global SF
                SF += 1
            if h.royal_flush:
                global RF
                RF += 1
            if h.four:
                global FOUR
                FOUR += 1
            if h.full_house:
                global FH
                FH += 1
            if h.three:
                global THREE
                THREE += 1
            if h.two_pair:
                global TP
                TP += 1
            if h.one_pair:
                global OP
                OP += 1
            if h.flush:
                global FLUSH
                FLUSH += 1
            if h.straight:
                global STRAIGHT
                STRAIGHT += 1
            print("Thread: {0} finish process hand {1} from queue[current size = {2}] at time = {3} \n"
                  .format(name, hand, q.qsize(), time.strftime('%H:%M:%S')))
        except:
            print('ERROR')
        finally:
            q.task_done()


if __name__ == '__main__':
    q = queue.Queue(maxsize=10000)

    t = threading.Thread(name="HandBuilderThread", target=hand_builder, args=(q,))
    t.start()

    threads_num = 2030  # three threads to consume
    for i in range(threads_num):
        t = threading.Thread(name="IdentifyHandThread-" + str(i), target=identify_hand, args=(q,))
        t.start()
    q.join()
    print(HANDS)
    print(BHAND, H)
    logging.info('Number of Royal Flush hands: {}'.format(RF))
    logging.info('Number of Straight Flush hands: {}'.format(SF))
    logging.info('Number of 4 of a Kind Hands: {}'.format(FOUR))
    logging.info('Number of Full House Hands: {}'.format(FH))
    logging.info('Number of Flush Hands: {}'.format(FLUSH))
    logging.info('Number of Straight Hands: {}'.format(STRAIGHT))
    logging.info('Number of 3 of a Kind Hands: {}'.format(THREE))
    logging.info('Number of Two Pair Hands: {}'.format(TP))
    logging.info('Number of One Pair Hands: {}'.format(OP))
    logging.info('Number of hands: {}'.format(HANDS))

    print('Queue is empty?', q.empty())
    sys.exit()
