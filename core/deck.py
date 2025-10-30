def build_standard_deck() -> list[dict]:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [ {'suit' : suit, 'rank' : rank} for rank in ranks for suit in suits]
    return(deck)
    


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return deck

if __name__ == "__main__":
    print(build_standard_deck())