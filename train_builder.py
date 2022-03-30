# mexican train train builder
# get station and hand then build longest possible train

# naming: tile is a domino is a tile


def build_tree(station, hand):
    # create tree with station as root, then build out all possible trains
    tree = Tree(station, hand, station[0])

    for i in range(len(hand)):

        for leaf in tree.get_leaf_nodes():
            for domino in leaf.remaining_tiles:
                if domino[0] == leaf.open_end or domino[1] == leaf.open_end:
                    open_end = domino[0] if domino[1] == leaf.open_end else domino[1]
                    leaf.add_child(Node(domino, leaf.remaining_tiles[:], open_end))

    return tree


def get_all_paths(node):
    # returns a list of all paths (e.g. [Tree, Node, Node, ...]) in data tree from node
    if len(node.children) == 0:
        return [[node]]
    return [
        [node] + path for child in node.children for path in get_all_paths(child)
    ]


def view_all_paths(_train):
    all_paths = get_all_paths(_train)

    for list_nodes in all_paths:
        print(*[node.name for node in list_nodes])


def get_longest_train(_train):
    all_paths = get_all_paths(_train)

    list_index_len = [(node_list[0], len(node_list[1]) - 1) for node_list in enumerate(all_paths)]

    longest = max(list_index_len, key=lambda x: x[1])

    # list of indexes for the longest trains
    longest_trains = [train[0] for train in list_index_len if train[1] == longest[1]]

    print(f'There are {len(longest_trains)} trains {longest[1]} tiles long:')
    for train in longest_trains:
        print(*[tile.name for tile in all_paths[train]])


def get_highest_value_train(_train):
    all_paths = get_all_paths(_train)

    list_index_sum = [(node_list[0], sum([sum(node.name) for node in node_list[1][1:]]))
                      for node_list in enumerate(all_paths)]

    largest = max(list_index_sum, key=lambda x: x[1])

    # list of indexes for the largest trains by pip count
    largest_trains = [train[0] for train in list_index_sum if train[1] == largest[1]]

    print(f'There are {len(largest_trains)} trains with {largest[1]} pips:')
    for train in largest_trains:
        print(*[tile.name for tile in all_paths[train]])


def get_ending_double(_train):
    all_paths = get_all_paths(_train)

    ending_double = [path for path in all_paths if path[-1].name[0] == path[-1].name[1]]

    print(f'There are {len(ending_double)} trains ending in a double:')
    for train in ending_double:
        print(*[tile.name for tile in train])


class Tree:
    def __init__(self, name, hand, open_end):
        self.name = name
        self.remaining_tiles = hand
        self.open_end = open_end
        self.children = []
        self.nodes = []

    def add_child(self, domino_tree):
        assert isinstance(domino_tree, Tree)
        self.children.append(domino_tree)

    def get_leaf_nodes(self):
        leafs = []

        def _get_leaf_nodes(node):
            if node is not None:
                if len(node.children) == 0:
                    leafs.append(node)
                for n in node.children:
                    _get_leaf_nodes(n)

        _get_leaf_nodes(self)
        return leafs


class Node(Tree):
    def __init__(self, name, hand, open_end):
        super().__init__(name, hand, open_end)
        self.pull_tile(self.name)

    def pull_tile(self, tile):
        self.remaining_tiles.remove(tile)

    def get_children(self, tree):
        for child in self.children:
            if child.children:
                child.get_children(tree)
                tree.append(child.name)
            else:
                tree.append(child.name)
