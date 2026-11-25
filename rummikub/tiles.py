from random import randint


def create_pool():
    cards = []
    for q in range(1, 3):
        for i in range(1, 14):
            for j in ["B", "R", "O", "K"]:
                cards.append((i, j))
    for i in range(1, 1001):
        a = randint(0, len(cards)-1)
        b = randint(0, len(cards)-1)
        cards[a] , cards[b] = cards[b] , cards[a]
    return cards


def division(cards):
    return (cards[:9], cards[9:18], cards[18:])












