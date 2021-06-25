import domino_handler
import train_builder


def train():
    # Up to 4 players take 15 dominoes each, 5 or 6 take 12 each, 7 or 8 take 10 each

    ds = domino_handler.MexicanTrain()

    station = ds.pull_station((12, 12))

    hand = ds.deal_hand(tiles=15)

    tree = train_builder.build_tree(station, hand)

    test_print(tree)


def test_print(_train):

    print(*_train.remaining_tiles, end='\n\n')

    train_builder.get_longest_train(_train)

    train_builder.get_highest_value_train(_train)

    train_builder.get_ending_double(_train)


if __name__ == '__main__':
    train()
