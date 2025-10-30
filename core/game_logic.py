from core.deck import build_standard_deck, shuffle_by_suit

def calculate_hand_value(hand: list[dict]) -> int: 
    sum = 0
    for i in hand:
        if i['rank'] == 'A':
            sum +=1
        elif i['rank'] == 'J' or  i['rank'] == 'Q' or  i['rank'] == 'K':
            sum+= 10
        else:
            sum+= int(i['rank'])
            
    return sum

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    return 

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    sum = calculate_hand_value(dealer["hand"])
    while sum <= 17:
        new_card = dealer["hand"].append(deck.pop())
        sum += new_card['rank']
        
    return sum





def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None: 
    pass

if __name__ == "__main__":
    deck = build_standard_deck()

    print(deck)

    shuffle = shuffle_by_suit(deck)
    player = {"hand": [ ] } 
    dealer = {"hand": [ ] }
   
    print(calculate_hand_value([{'suit' : 'Diamonds' , 'rank' : 'K'}, {'suit' : 'Hearts' , 'rank' : 'K'},]))
    print(deal_two_each(deck, player, dealer))
    print(dealer_play(deck, dealer))

    # py -m core.game_logic