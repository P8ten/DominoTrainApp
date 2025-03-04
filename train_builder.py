class Tree:
    """
    Represents a tree structure for building all possible domino trains.
    """

    def __init__(self, face_value: tuple, remaining_tiles: list):
        self.face_value = face_value  # Current tile (tuple)
        self.remaining_tiles = set(remaining_tiles)  # Use set for O(1) lookups
        self.open_end = face_value[1]  # The side of the tile open for connections
        self.children = []  # Child nodes representing next possible moves

    def add_child(self, child_node):
        """Adds a new child node to the tree."""
        self.children.append(child_node)

    def get_leaf_nodes(self):
        """Returns all leaf nodes in the tree (i.e., endpoints of valid trains)."""
        leaves = []

        def _traverse(node):
            if not node.children:
                leaves.append(node)
            for child in node.children:
                _traverse(child)

        _traverse(self)
        return leaves


def build_tree(station: tuple, hand: list) -> Tree:
    """
    Builds a tree of all possible domino train sequences from the given hand.

    Args:
        station (tuple): The starting domino (root of the tree).
        hand (list): List of domino tuples representing the player's hand.

    Returns:
        Tree: The root of the generated tree.
    """
    tree = Tree(station, hand)
    stack = [(tree, set(hand))]  # Use a stack for iterative DFS

    while stack:
        node, available_tiles = stack.pop()

        # Find playable tiles
        playable_tiles = [tile for tile in available_tiles if node.open_end in tile]

        for tile in playable_tiles:
            oriented_tile = tile[::-1] if tile[1] == node.open_end else tile
            new_hand = available_tiles - {tile}  # Create new hand without the used tile

            child_node = Tree(oriented_tile, new_hand)
            node.add_child(child_node)
            stack.append((child_node, new_hand))  # Continue expansion

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

        longest_trains = [
            train for train in all_paths_face_value if len(train) == max_len]

        print(
            f'There are {len(longest_trains)} trains using {max_len - 1} tiles:')

        for train_path in longest_trains:
            print(*train_path)

    return max_len


def get_highest_value_train(train, *, print_=False) -> int:
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
