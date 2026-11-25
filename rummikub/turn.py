

table = []
def read_player_move(hand, all_cards):
    flag = True
    c = 0
    while flag:
        if input("Choose tile positions or D to draw > ").lower().strip() == "d":
            draw(hand, all_cards)
            flag = False
        else:
            c1 = int(input("Enter index1: "))
            c2 = int(input("Enter index2: "))
            c3 = int(input("Enter index3: "))
            is_set_cards = is_valid_set([hand[c1], hand[c2] ,hand[c3]])
            if is_set_cards is True:
                print(f"You played: {hand[c1], hand[c2] ,hand[c3]}")
                hand.remove(hand[c3])
                hand.remove(hand[c2])
                hand.remove(hand[c1])
                # print_good_set()
                flag = False
            else:
                print("Invalid set. Try again")
                c += 1
                if c == 2:
                    draw(hand, all_cards)
                    break
                pass
                # print_bad_set()


def find_computer_move(hand, all_cards):
    print(hand)
    B = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
    K = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
    O = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
    R = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
    for i in hand:
        n = i[0]
        n = str(n)
        if i[1] == "B":
            B[n] = True
        elif i[1] == "O":
            O[n] = True
        elif i[1] == "K":
            K[n] = True
        elif i[1] == "R":
            R[n] = True
                # i[1][0] = True
        # print(B, K, O, R)
    # for i in range(len(hand)):
    #     for j in range(i, len(hand)):
    #         if hand[i] == hand[j]:
    #             continue
    #         for k in range(j, len(hand)):
    #             if hand[i] == hand[k] or hand[k] == hand[j]:
    #                 continue
    #             if is_valid_set([hand[i], hand[k] , hand[j]]) is True:
    #                 print(f"Computer played: {hand[i], hand[k] , hand[j]}")
    #                 hand.remove(hand[k])
    #                 hand.remove(hand[j])
    #                 hand.remove(hand[i])
    #                 return
    draw(hand, all_cards)
    return


def is_valid_set(tiles):
    tiles.sort(key=lambda t: t[0])
    if tiles[0][0] == tiles[1][0] == tiles[2][0] and tiles[0][1] != tiles[1][1] != tiles[2][1] or tiles[0][0] == tiles[1][0] - 1 == tiles[2][0] -2 and tiles[0][1] == tiles[1][1] == tiles[2][1]:
        table.append(tiles)
        return True
    return False


def draw(hand, all_cards):
    hand.append(all_cards.pop(0))

