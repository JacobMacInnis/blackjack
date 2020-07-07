from deck import Deck
from hand import Hand
from chips import Chips
from functions import *

playing = True

while True:

    print('Welcome To BlackJack')

    # CREATE & SHUFFLE DECK
    deck = Deck()
    deck.shuffle()
    
    # DEAL TWO CARDS TO PLAYER AND DEALER
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # SET UP THE PLAYERS CHIPS
    player_chips = Chips()

    # PROMPT PLAYER FOR BET
    take_bet(player_chips)

    # SHOW CARDS (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # PROMPT PLAYER TO HIT OR STAND
        hit_or_stand(deck, player_hand)

        # SHOW CARDS (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # IF PLAYERS HAND EXCEEDS 21, RUN player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    # IF PLAYER HASN'T BUSTED, PLAY DEALER'S HAND UNTIL DEALER REACHES 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17: 
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # RUN DIFFERENT WINNING SCENARIOS
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        
        else:
            push(player_hand, dealer_hand)

    # INFORM PLAYER OF THEIR CHIPS TOTAL
    print("\nPlayer's winnings stand at ", player_chips.total)

    # ASK TO PLAY AGAIN
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing=True
        continue
    else:
        print('Thanks for playing!')
        break