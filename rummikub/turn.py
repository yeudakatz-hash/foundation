

# table = []
# def read_player_move(hand, all_cards):
#     flag = True
#     c = 0
#     while flag:
#         if input("Choose tile positions or D to draw > ").lower().strip() == "d":
#             draw(hand, all_cards)
#             flag = False
#         else:
#             c1 = int(input("Enter index1: "))
#             c2 = int(input("Enter index2: "))
#             c3 = int(input("Enter index3: "))
#             is_set_cards = is_valid_set([hand[c1], hand[c2] ,hand[c3]])
#             if is_set_cards is True:
#                 print(f"You played: {hand[c1], hand[c2] ,hand[c3]}")
#                 ans = input("you want add card to set? (y/n)")
#                 if ans =="y":
#                     more_card([hand[c1], hand[c2] ,hand[c3]], all_cards)
                
#                 hand.remove(hand[c3])
#                 hand.remove(hand[c2])
#                 hand.remove(hand[c1])
#                 flag = False
#             else:
#                 print("Invalid set. Try again")
#                 c += 1
#                 if c == 2:
#                     draw(hand, all_cards)
#                     break
#                 pass


# def find_computer_move(hand, all_cards):
#     for i in range(len(hand)):
#         for j in range(i, len(hand)):
#             if hand[i] == hand[j]:
#                 continue
#             for k in range(j, len(hand)):
#                 if hand[i] == hand[k] or hand[k] == hand[j]:
#                     continue
#                 if is_valid_set([hand[i], hand[k] , hand[j]]) is True:
#                     set = [hand[i], hand[k] , hand[j]]
#                     more_card(set, all_cards)
#                     print(f"Computer played: {hand[i], hand[k] , hand[j]}")
#                     hand.remove(hand[k])
#                     hand.remove(hand[j])
#                     hand.remove(hand[i])
#                     return
#     draw(hand, all_cards)
#     return
#     # B = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
#     # K = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
#     # O = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
#     # R = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False, "10": False, "11": False, "12": False, "13":False}
#     # for i in hand:
#     #     n = i[0]
#     #     n = str(n)
#     #     if i[1] == "B":
#     #         B[n] = True
#     #     elif i[1] == "O":
#     #         O[n] = True
#     #     elif i[1] == "K":
#     #         K[n] = True
#     #     elif i[1] == "R":
#     #         R[n] = True
        
#     #     is_valid_set(B, K, O, R)
        
#                 # i[1][0] = True
#         # print(B, K, O, R)
 


# def is_valid_set(tiles):
#     tiles.sort(key=lambda t: t[0])
#     col = tiles[0][1]
#     num = tiles[0][0]
#     for t in tiles[1:]:
#         if t[1] != col or t[0] 
#             break
#     sett = set(tiles)
#     for t in sett:
        
#     if tiles[0][0] == tiles[1][0] == tiles[2][0] and tiles[0][1] != tiles[1][1] != tiles[2][1] or tiles[0][0] == tiles[1][0] - 1 == tiles[2][0] -2 and tiles[0][1] == tiles[1][1] == tiles[2][1]:
#         table.append(tiles)
#         return True
#     return False
    
#     # count = 0
#     # max = 0
#     # retzef = []
#     # for i in [B, K, O, R]:
#     #     for j in range(1, 13):
#     #         if i[j] is True:
#     #             count += 1
#     #             if count >= 3:
#     #                 if count > retzef:
#     #                     retzef = i
#     #         else:
#     #             count = 0
#     # for i in range(1, 14):
#     #     if B[i] == K[i] == O[i] == R[i] == True     or B[i] == K[i] == O[i] == True       or B[i] == K[i] == R[i] == True       or R[i] == K[i] == O[i] == True      or R[i] == K[i] == B[i] == True:
#     #         if B[i] == K[i] == O[i] == R[i] == True:
#     #             count = 4
#     #         else:
#     #             count = i
            
            
            
            

# #לעשות שיכניס קלף למעלה ויעביר לכאן ואז כשזה יהיה עם המחשב אז זה יהיה בתוך לולאה

# def more_card(set, all_cards):
#     new = int(input("enter a new card"))
#     if set[0][0] == set[1][0] == set[2][0] == all_cards[new][0] and set[0][1] != set[1][1] != set[2][1] != all_cards[new][1]             or                        set[0][0] == set[1][0] - 1 == set[2][0] -2 == (all_cards[new][0] - 3 or all_cards[new][0] + 1)  and set[0][1] == set[1][1] == set[2][1] == all_cards[new][1]:
#         all_cards.remove(new)

























all_cards = []
table = []
def read_player_move(hand):
    choose = input("Enter list of indexes you choose or d to take card: ")
    if choose.lower().strip() == "d":
        hand.append(all_cards.pop(0))
    else:
        indexes = [int(x) for x in choose.split()]
        choosen = [hand[i] for i in indexes]
        choose.split(" ")
        if is_set(choosen):
            print("אההההה")
                
        

def is_set(choosen):
    if len(choosen) < 3:
        return False
    a = [i[0] for i in choosen]
    b = [i[1] for i in choosen]
    if len(set(a)) == 1 and len(set(b)) == len(choosen): return True
    choosen.sort()
    if len(set(b)) == 1:
        for i in range([1, len(choosen)]):
            if choosen[i][0] - choosen[i-1][0] !=1:
                return False
        return True
    return False

    
        
            
        
        








