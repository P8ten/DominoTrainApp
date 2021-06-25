import random


class DominoSet:
    def __init__(self, s=5):
        self.num_pips = s
        self.domino_set = []
        self.build_set()

    def build_set(self):
        for n in range(self.num_pips + 1):
            for face in range(n + 1):
                self.domino_set.append((n, face))

    def deal_hand(self, tiles=7):
        hand = []
        for _ in range(tiles):
            hand.append(self.domino_set.pop(random.randrange(len(self.domino_set))))
        return hand

    def print_set(self):
        print(*self.domino_set)


class MexicanTrain(DominoSet):
    def __init__(self):
        DominoSet.__init__(self, 12)

    def pull_station(self, station):
        return self.domino_set.pop(self.domino_set.index(station))
