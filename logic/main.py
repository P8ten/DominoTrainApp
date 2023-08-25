import domino_handler
import train_builder


class Train:

    # Up to 4 players take 15 dominoes each,
    # 5 or 6 take 12 each, 7 or 8 take 10 each
    def __init__(self, starting_tile=None) -> None:
        self.__starting_tile = starting_tile
        self.__ds = domino_handler.MexicanTrainSet(set_size=12).get_set()
        self.__tree = self.build_tree()
        
    def deal_hand(self, hand=None, tiles=7) -> list:
        """returns list of tuples representing a hand of dominoes"""
        if hand is None:
            if len(self.__ds) < tiles:

                raise IndexError(f'There are only {len(self.__ds)} available tiles in self._domino_set.'

                                f'Called for {tiles} tiles.')

            hand = self.__ds[:tiles]

        self.__ds = [i for i in self.__ds if i not in hand]

        return hand
    
    def pull_station(self, station: tuple[int, int]) -> tuple[int, int]:
        """station is a tuple representing station tile, e.g. (12, 12)"""

        if station not in self.__ds:

            raise ValueError(f'The station {station} not in domino_set')

        return self.__ds.pop(self.__ds.index(station))

    def build_tree(self):
        return train_builder.build_tree(self.pull_station(station=self.__starting_tile),
        self.deal_hand(tiles=15))
    
    def get_tree(self):
        return self.__tree
    
    


def test_print(_train):

    print(*_train.remaining_tiles, end='\n\n')

    print(_train)

    train_builder.get_all_paths_face_value(_train, print_=False)

    train_builder.get_longest_train(_train, print_=True)

    train_builder.get_highest_value_train(_train, print_=True)

    train_builder.get_ending_double(_train, print_=True)


class ConsolePrinter:

    pass


if __name__ == '__main__':

    train = Train(starting_tile=(12, 12))

    test_print(train.get_tree())
