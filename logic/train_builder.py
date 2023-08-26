from dataclasses import dataclass, field

@dataclass
class TrainBranch:
    """ dataclass for keeping track of train branches in a game of Mexican Train """

    head_tile: tuple[int, int]
    remaining_tiles: list[tuple[int, int]]
    children: list['TrainBranch'] = field(default_factory=list)

    def __str__(self) -> str:
        return str(self.head_tile)

    @property
    def open_end(self) -> int:
        return self.head_tile[1]
    
    def set_child(self, node: 'TrainBranch') -> None:
        self.children.append(node)

    def get_open_end(self) -> int:
        return self.open_end
    
    def get_head_tile(self) -> tuple[int, int]:
        return self.head_tile
    
    def get_children(self) -> list['TrainBranch']:
        return self.children
    
    def get_remaining_tiles(self) -> list[tuple[int, int]]:
        return self.remaining_tiles
    
    def get_branch_end_nodes(self) -> list['TrainBranch']:

        if len(self.children) == 0:
            return [self]
        return [node for child in self.get_children() for node in child.get_branch_end_nodes()]


def build_tree(station: tuple, hand: list, data_class = TrainBranch) -> TrainBranch:
    """

    create tree with station as root, then build out all possible trains from hand.
    station is a tuple representing a tile.
    hand is a list of tuples representing a hand of dominoes, e.g. [(0,0), (0,1), ..., (2,12)].

    """

    tree = data_class(station, hand)

    for _ in range(len(hand)):

        for leaf in tree.get_branch_end_nodes():

            for tile in leaf.remaining_tiles:

                if leaf.open_end in tile:

                    # create tile Node with Node.face_value in proper
                    # orientation relative to parent tile

                    remaining_tiles = leaf.remaining_tiles[:]
                    remaining_tiles.remove(tile)

                    leaf.set_child(
                        data_class(
                            tile[::-1] if tile[1] == leaf.open_end else tile,
                            remaining_tiles
                        )
                    )

    return tree


def get_all_paths(node: TrainBranch) -> list[list[TrainBranch]]:
    """returns a list of all paths (e.g. [Tree, Node, Node, ...]) in data tree from node
        should be used with tree as input

    Args:
        node (train_builder.Node): a node of the tree representing a brance of the train

    Returns:
        list: returns a list of lists which contain the path of all possible trains from node
    """

    if len(node.children) == 0:

        return [[node]]

    return [

        [node] + path for child in node.children for path in get_all_paths(child)

    ]


def get_all_paths_face_value(train: TrainBranch, *, print_=False) -> list[list[tuple[int, int]]]:
    """used to get a list of of all trains from station by face falue

    Args:
        train (train_builder.Tree): Tree class representing all possible trains from station
        print_ (bool, optional): _description_. Defaults to False.

    Returns:
        list: returns a list of lists which contains tuples representing the face value of all tiles
        in a train for all trains
    """

    all_paths = get_all_paths(train)

    if print_:

        for list_nodes in all_paths:

            print(*[node for node in list_nodes])

    return [[node.get_head_tile() for node in list_nodes] for list_nodes in all_paths]


def get_longest_trains(train, *, print_=False) -> int:

    all_paths_face_value = get_all_paths_face_value(train)

    max_len = max(map(len, all_paths_face_value))

    if print_:

        longest_trains = [
            train for train in all_paths_face_value if len(train) == max_len]

        print(
            f'There are {len(longest_trains)} trains using {max_len - 1} tiles:')

        for train_path in longest_trains:
            print(*train_path)

    return max_len


def get_highest_value_trains(train, *, print_=False) -> int:
    """get trains with highest total pip value.  Returns highest pip count"""

    def _get_train_sum(path):
        return sum([a + b for (a, b) in path])

    all_paths_face_value = get_all_paths_face_value(train)

    max_sum = max([_get_train_sum(path) for path in all_paths_face_value])

    if print_:

        largest_trains = [
            train for train in all_paths_face_value if _get_train_sum(train) == max_sum]

        print(f'There are {len(largest_trains)} trains with {max_sum} pips:')

        for train_path in largest_trains:
            print(*train_path)

    return max_sum


def get_ending_doubles(train, *, print_=False) -> int:
    """get all trains ending in a double.  Returns the number of possible trains ending in double"""

    all_paths_face_value = get_all_paths_face_value(train)

    trains_ending_in_double = [
        path for path in all_paths_face_value if path[-1][0] == path[-1][1]]

    if print_:

        print(
            f'There are {len(trains_ending_in_double)} trains ending in a double:')

        for train_path in trains_ending_in_double:

            print(*train_path)

    return len(trains_ending_in_double)


def get_longest_train(train) -> list[tuple[int,int]]:

    all_paths_face_value = get_all_paths_face_value(train)

    max_len = max(map(len, all_paths_face_value))

    return [train for train in all_paths_face_value if len(train) == max_len]

def get_ending_double(train) -> list[tuple[int,int]]:
    """get all trains ending in a double."""

    all_paths_face_value = get_all_paths_face_value(train)

    return [path for path in all_paths_face_value if path[-1][0] == path[-1][1]]

def get_highest_value_train(train) -> list[tuple[int,int]]:
    """get trains with highest total pip value"""

    all_paths_face_value = get_all_paths_face_value(train)

    max_sum = max([sum([a + b for (a, b) in path]) for path in all_paths_face_value])

    return [train for train in all_paths_face_value if sum([a + b for (a, b) in train]) == max_sum]

