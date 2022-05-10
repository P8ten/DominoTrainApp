import domino_handler
import train_builder


def train(starting_tile):

    # Up to 4 players take 15 dominoes each, 5 or 6 take 12 each, 7 or 8 take 10 each

    ds = domino_handler.MexicanTrain(set_size=12)

    return train_builder.build_tree(

        ds.pull_station(station=starting_tile),

        ds.deal_hand(tiles=15))


def test_print(_train):

    print(*_train.remaining_tiles, end='\n\n')

    train_builder.get_all_paths_face_value(_train, print_=False)

    train_builder.get_longest_train(_train, print_=True)

    train_builder.get_highest_value_train(_train, print_=True)

    train_builder.get_ending_double(_train, print_=True)


if __name__ == '__main__':

    train = train(starting_tile=(12, 12))

    test_print(train)
