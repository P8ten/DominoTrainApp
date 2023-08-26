from domino_handler import DominoSet, MexicanTrainSet
from train_builder import *


class Train:

    # Up to 4 players take 15 dominoes each,
    # 5 or 6 take 12 each, 7 or 8 take 10 each
    def __init__(self, domino_set: DominoSet, starting_tile: tuple[int, int], tiles: int=15) -> None:
        self.__starting_tile = starting_tile
        self.__ds = domino_set
        self.__tile_count = tiles
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
        return build_tree(self.pull_station(station=self.__starting_tile), hand=self.deal_hand(tiles=self.__tile_count))
    
    def get_tree(self):
        return self.__tree
    
    


def test_print(_train):

    print(*_train.remaining_tiles, end='\n\n')

    print(_train)

    get_all_paths_face_value(_train, print_=False)

    get_longest_trains(_train, print_=True)

    get_highest_value_trains(_train, print_=True)

    get_ending_doubles(_train, print_=True)


class ConsolePrinter:

    def __init__(self, tree: TrainBranch):
        self.__tree = tree

    def longest_train(self):
        longest_trains = get_longest_train(self.__tree)

        print(
            f'There are {len(longest_trains)} trains using {len(longest_trains[0]) - 1} tiles:')

        for train_path in longest_trains:
            print(*train_path)

    def ending_double(self):
        trains_ending_in_double = get_ending_double(self.__tree)

        print(
            f'There are {len(trains_ending_in_double)} trains ending in a double:')

        for train_path in trains_ending_in_double:

            print(*train_path)

    def highest_value_train(self):

        largest_trains = get_highest_value_train(self.__tree)

        print(f'There are {len(largest_trains)} trains with {sum([a + b for (a, b) in largest_trains[0]])} pips:')

        for train_path in largest_trains:
            print(*train_path)



if __name__ == '__main__':

    train = Train(domino_set=MexicanTrainSet(set_size=12).get_set(), starting_tile=(12, 12))
    printer = ConsolePrinter(tree=train.get_tree())

    printer.longest_train()
    printer.ending_double()
    printer.highest_value_train()
