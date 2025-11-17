import random

def build_standard_deck() -> list[dict]:
    """
    building a matrix of cards
    """
    deck = []
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [ {'suit' : suit, 'rank' : rank} for rank in ranks for suit in suits]
    return deck
    


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    
    while swaps > 0:
        idx_card_i = deck[random.randint(0,len(deck)-1)]
        idx_card_i = deck.index(idx_card_i)
        good_card = False
        while not good_card:
            idx_card_j = deck[random.randint(0,len(deck)-1)]
            idx_card_j = deck.index(idx_card_j)
            suit = deck[idx_card_i]['suit']
            match suit:
                case 'Hearts':
                    if idx_card_j % 5 != 0:
                        continue
                case 'Clubs':
                    if idx_card_j % 3 != 0:
                        continue
                case 'Diamonds':
                    if idx_card_j % 2 != 0:
                        continue
                case 'Spades':
                    if idx_card_j % 7 != 0:
                        continue
            good_card = True
        deck[idx_card_i], deck[idx_card_j] = deck[idx_card_j], deck[idx_card_i]
        swaps -= 1



    return deck

if __name__ == "__main__":
    print(build_standard_deck())
    deck = build_standard_deck()
    # my_deck = build_standard_deck()
    # print(build_standard_deck()[0]['suit'])
    # print(my_deck[0]['rank'])
    print(shuffle_by_suit(deck))