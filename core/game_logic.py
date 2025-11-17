from deck import build_standard_deck, shuffle_by_suit
from player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int: 
    sum = 0
    for i in hand["hand"]:
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
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())

     

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    """
    the dealer pley till he has sum of 17
    """
    sum = 0
    while sum <= 17:
        getting_a_new_card = dealer["hand"].append(deck.pop())
        sum += calculate_hand_value(getting_a_new_card)
    if 17 < sum <= 21:
        return True
    else:
        return False
        
    
def run_full_game(player: dict, dealer: dict) -> None: 
    deck = build_standard_deck()
    shufflled_deck = shuffle_by_suit(deck)
    deal_two_each(shufflled_deck, player, dealer)
    while calculate_hand_value(player) < 100000:
        print("you drow the", str(player["hand"]))
        if ask_player_action() == 'S':
            break
        else:
            player["hand"].append(deck.pop())
    print(player)
             




    # print(deck)
    # print(len(deck))

    # shuffle = shuffle_by_suit(deck)
player = {"hand": [ ] } 
dealer = {"hand": [ ] }
   
    # #print(calculate_hand_value([{'suit' : 'Diamonds' , 'rank' : 'K'}, {'suit' : 'Hearts' , 'rank' : 'K'},]))
    #print(deal_two_each(deck, player, dealer))
    # print(deck)
    # print(len(deck))
    # print(dealer_play(deck, dealer))
    #print(deal_two_each(deck, player, dealer ))
run_full_game(player, dealer)
    # py -m core.game_logic