from random import shuffle


class DominoSet:

    def __init__(self, set_size=5):

        self._highest_pip = set_size

        self._domino_set = []

        self._build_set()

        # self.domino_ascii = [chr(i) for i in range(127025, 127124)]

    def _build_set(self) -> None:
        """builds list of tuples representing tiles in a domino set.  Set size determined by self.highest_pip (int) in

        class constructor.  Set is shuffled randomly."""

        self._domino_set = [(n, face) for n in range(
            self._highest_pip + 1) for face in range(n + 1)]

        shuffle(self._domino_set)

    def deal_hand(self, tiles=7) -> list:
        """returns list of tuples representing a hand of dominoes"""

        hand = []

        if len(self._domino_set) < tiles:

            raise IndexError(f'There are only {len(self._domino_set)} available tiles in self._domino_set.'

                             f'Called for {tiles} tiles.')

        for _ in range(tiles):

            hand.append(self._domino_set.pop())

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
