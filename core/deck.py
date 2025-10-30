def build_standard_deck() -> list[dict]:
    deck = [] 
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        deck.append(suit)
        for rank in ranks:
            deck[rank] = {rank: f"{rank} of {suit}"}
    return(deck)
    


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return [{}]

# if __name__ == "__main__":
#     print(build_standard_deck())