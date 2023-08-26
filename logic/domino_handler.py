from random import shuffle


class DominoSet:

    def __init__(self, set_size=5):

        self._highest_pip = set_size

        self._domino_set = self.set_domino_set()

        self.shuffle_set()

    def set_domino_set(self) -> list[tuple[int, int]]:
        """builds list of tuples representing tiles in a domino set.  Set size determined by self.highest_pip (int) in

        class constructor.  Set is shuffled randomly."""

        return [(n, face) for n in range(self._highest_pip + 1) for face in range(n + 1)]

    def shuffle_set(self):
        shuffle(self._domino_set)
    
    def get_set(self) -> list[tuple[int, int]]:
        return self._domino_set

    def __str__(self):
        return ' '.join(self._domino_set)


class MexicanTrainSet(DominoSet):

    def __init__(self, set_size):
        super().__init__(set_size)
