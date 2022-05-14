class Tree:

    def __init__(self, face_value: tuple, hand: list):

        self.face_value = face_value

        self.remaining_tiles = hand

        self.open_end = face_value[1]

        self.children = []


    def add_child(self, domino_tree):

        self.children.append(domino_tree)


    def get_leaf_nodes(self):

        leaves = []

        def _get_leaf_nodes(node):

            if node is not None:

                if len(node.children) == 0:

                    leaves.append(node)

                for child in node.children:

                    _get_leaf_nodes(child)

        _get_leaf_nodes(self)

        return leaves


class Node(Tree):

    def __init__(self, face_value, hand):

        super().__init__(face_value, hand)

        self.pull_tile(self.face_value)

    def pull_tile(self, tile_to_pull):

        self.remaining_tiles.remove(
            tile_to_pull if tile_to_pull in self.remaining_tiles else (tile_to_pull[::-1])
        )


def build_tree(station: tuple, hand: list) -> type(Tree):
    """

    create tree with station as root, then build out all possible trains from hand.
    station is a tuple representing a tile.
    hand is a list of tuples representing a hand of dominoes, e.g. [(0,0), (0,1), ..., (2,12)].

    """

    tree = Tree(station, hand)

    for _ in range(len(hand)):

        for leaf in tree.get_leaf_nodes():

            for tile in leaf.remaining_tiles:

                if leaf.open_end in tile:

                    # create tile Node with Node.face_value in proper
                    # orientation relative to parent tile

                    tile = (tile[1], tile[0]) if tile[1] == leaf.open_end else (
                        tile[0], tile[1])

                    leaf.add_child(Node(tile, leaf.remaining_tiles[:]))

    return tree


def get_all_paths(node) -> list:
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


def get_all_paths_face_value(train, *, print_=False) -> list:
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

            print(*[node.face_value for node in list_nodes])

    return [[node.face_value for node in list_nodes] for list_nodes in all_paths]


def get_longest_train(train, *, print_=False) -> int:

    all_paths_face_value = get_all_paths_face_value(train)

    max_len = max(map(len, all_paths_face_value))

    if print_:

        longest_trains = [train for train in all_paths_face_value if len(train) == max_len]

        print(f'There are {len(longest_trains)} trains using {max_len - 1} tiles:')
     
        for train_path in longest_trains:
            print(*train_path)

    return max_len


def get_highest_value_train(train, *, print_=False) -> int:
    """get trains with highest total pip value.  Returns highest pip count"""

    all_paths_face_value = get_all_paths_face_value(train)

    list_index_sum = [

        (index, sum([a + b for (a, b) in path])) for (index, path) in enumerate(all_paths_face_value)

    ]

    _, largest_pip_count = max(list_index_sum, key=lambda x: x[1])

    # list of indexes for the largest trains by pip count

    largest_trains = [index for (index, pip_count) in list_index_sum if pip_count == largest_pip_count]

    if print_:

        print(
            f'There are {len(largest_trains)} trains with {largest_pip_count} pips:')

        for train_index in largest_trains:

            print(*all_paths_face_value[train_index])

    return largest_pip_count


def get_ending_double(train, *, print_=False) -> int:
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

