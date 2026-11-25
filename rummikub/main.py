from foundations.rummikub.tiles import *
from foundations.rummikub.turn import *
from foundations.rummikub.printer import *


def game():
    cards = create_pool()
    print(cards)
    player_cards, computer_cards, all_cards = division(cards)
    t = 0

    while True:
        if t % 2 == 0:
            find_computer_move(computer_cards, all_cards)
        else:
            print_details(table, computer_cards, player_cards)
            read_player_move(player_cards, all_cards)
        t += 1
game()