import random


class DominoSet:

    def __init__(self, set_size=5):

        self._highest_pip = set_size

        self._domino_set = set(_build_set())

        # self.domino_ascii = [chr(i) for i in range(127025, 127124)]

    def _build_set(self) -> list[tuple[int, int]]:
        """builds list of tuples representing tiles in a domino set.  Set size determined by self.highest_pip (int) in

        class constructor.  Set is shuffled randomly."""

        return [(n, face) for n in range(self._highest_pip + 1) for face in range(n + 1)]

    def deal_hand(self, tiles=7) -> list:
        """returns list of tuples representing a hand of dominoes"""

        if len(self._domino_set) < tiles:

            raise IndexError(f'There are only {len(self._domino_set)} available tiles in self._domino_set.'

                             f'Called for {tiles} tiles.')

        hand = random.sample(list(self._domino_set), tiles)
        
        self._domino_set -= set(hand)

        return hand

    def print_set(self):

        print(*self._domino_set)


class MexicanTrain(DominoSet):

    def __init__(self, set_size):

        super().__init__(set_size)

    def pull_station(self, station):
        """station is a tuple representing station tile, e.g. (12, 12)"""

        if station not in self._domino_set:

            raise ValueError(f'The station {station} not in domino_set')

        return self._domino_set.pop(self._domino_set.index(station))
